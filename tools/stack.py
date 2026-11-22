"""Validate rosestack and explicitly manage local OpenCode discovery links."""

import argparse
from dataclasses import dataclass
import json
import os
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
ID = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


@dataclass(frozen=True)
class Link:
    source: Path
    destination: Path


def frontmatter(path):
    """Read the simple scalar metadata used by this repo, not arbitrary YAML."""
    lines = path.read_text().splitlines()
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        raise ValueError(f"Missing frontmatter: {path}")
    end = lines.index("---", 1)
    fields = {}
    for line in lines[1:end]:
        match = re.fullmatch(r"([a-z][a-z0-9_-]*):\s*(.*)", line)
        if match:
            key, value = match.groups()
            if key in fields:
                raise ValueError(f"Duplicate metadata field {key}: {path}")
            fields[key] = value.strip().strip('\"\'')
    return fields


def inventory(root):
    data = json.loads((root / "stack.json").read_text())
    if not isinstance(data, dict) or data.get("version") != 1:
        raise ValueError("stack.json must be an object with version 1")
    for key in ("skills", "opencode_agents"):
        values = data.get(key)
        if not isinstance(values, list) or not values:
            raise ValueError(f"{key} must be a nonempty list")
        if any(not isinstance(value, str) for value in values):
            raise ValueError(f"{key} IDs must be strings")
        if len(set(values)) != len(values):
            raise ValueError(f"Duplicate IDs in {key}")
        for value in values:
            if len(value) > 64 or not ID.fullmatch(value):
                raise ValueError(f"Invalid {key} ID: {value}")
    return data


def check_source(root, path):
    if not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"Source escapes checkout: {path}")
    for item in (path, *path.parents):
        if item == root:
            break
        if item.is_symlink():
            raise ValueError(f"Source must not contain symlinks: {item}")


def validate(root):
    for name in ("skills", "adapters", "docs", "plugins", "licenses", "stack.json",
                 "README.md", "NOTICE.md", "AGENTS.md"):
        path = root / name
        check_source(root, path)
        if path.is_dir():
            for item in path.rglob("*"):
                check_source(root, item)
    data = inventory(root)
    expected = set(data["skills"])
    actual = {path.parent.name for path in (root / "skills").glob("*/SKILL.md")}
    if actual != expected:
        raise ValueError(f"Skill inventory mismatch: listed={sorted(expected)}, found={sorted(actual)}")
    for skill in data["skills"]:
        directory = root / "skills" / skill
        path = directory / "SKILL.md"
        fields = frontmatter(path)
        if fields.get("name") != skill or not fields.get("description"):
            raise ValueError(f"Skill needs matching name and a description: {path}")
    agent_root = root / "adapters" / "opencode" / "agents"
    actual_agents = {path.stem for path in agent_root.glob("*.md")}
    if actual_agents != set(data["opencode_agents"]):
        raise ValueError("OpenCode agent inventory mismatch")
    for agent in data["opencode_agents"]:
        path = agent_root / f"{agent}.md"
        fields = frontmatter(path)
        mode = "primary" if agent in ("rose", "build", "design") else "subagent"
        if fields.get("mode") != mode or not fields.get("description"):
            raise ValueError(f"Agent needs description and mode {mode}: {path}")
    paths = [root / "README.md", root / "NOTICE.md", root / "AGENTS.md"]
    for directory in ("skills", "docs", "adapters", "plugins"):
        paths.extend((root / directory).rglob("*.md"))
    for path in paths:
        for destination in LINK.findall(path.read_text()):
            if "://" in destination or destination.startswith(("#", "mailto:")):
                continue
            relative = destination.split("#", 1)[0]
            target = (path.parent / relative).resolve()
            if not target.is_relative_to(root.resolve()) or not target.exists():
                raise ValueError(f"Broken or escaping link {destination}: {path}")
            if path.is_relative_to(root / "skills"):
                skill_root = root / "skills" / path.relative_to(root / "skills").parts[0]
                if not target.is_relative_to(skill_root.resolve()):
                    raise ValueError(f"Skill link is not self-contained {destination}: {path}")
    return data


def planned_links(root, target, include_agents):
    data = validate(root)
    target = target.expanduser().absolute()
    result = [Link(root / "skills" / skill, target / "skills" / skill)
              for skill in data["skills"]]
    if include_agents:
        result.extend(Link(root / "adapters" / "opencode" / "agents" / f"{agent}.md",
                           target / "agents" / f"{agent}.md")
                      for agent in data["opencode_agents"])
    return result


def uninstall_links(root, target, include_agents):
    """Find only owned links, including retired IDs, without validating sources."""
    target = target.expanduser().absolute()
    groups = [(target / "skills", root / "skills", False)]
    if include_agents:
        groups.append((target / "agents", root / "adapters" / "opencode" / "agents", True))
    result = []
    for directory, source, agents in groups:
        check_target_parents(directory / "placeholder")
        if not directory.exists():
            continue
        for destination in sorted(directory.iterdir()):
            name = destination.stem if agents else destination.name
            if agents and destination.suffix != ".md":
                continue
            if len(name) <= 64 and ID.fullmatch(name):
                link = Link(source / destination.name, destination)
                if link_state(link) == "owned":
                    result.append(link)
    return result


def link_state(link):
    destination = link.destination
    if destination.is_symlink():
        source = destination.readlink()
        if not source.is_absolute():
            source = destination.parent / source
        return "owned" if os.path.abspath(source) == os.path.abspath(link.source) else "foreign"
    return "foreign" if destination.exists() else "missing"


def check_target_parents(destination):
    for parent in destination.parents:
        if parent.is_symlink():
            raise ValueError(f"Refusing symlinked target ancestor: {parent}")
        if parent.exists() and not parent.is_dir():
            raise ValueError(f"Target ancestor is not a directory: {parent}")


def preflight(links):
    for link in links:
        check_target_parents(link.destination)
        if link_state(link) == "foreign":
            raise ValueError(f"Refusing existing file or foreign link: {link.destination}")


def manage(links, action, apply):
    """Preflight the whole selection; never overwrite or recursively delete."""
    preflight(links)
    for link in links:
        state = link_state(link)
        change = (action == "install" and state == "missing") or (
            action == "uninstall" and state == "owned")
        label = action if change else "unchanged"
        print(f"{label}: {link.destination} -> {link.source}")
        if not apply or not change:
            continue
        preflight([link])
        if action == "install":
            link.destination.parent.mkdir(parents=True, exist_ok=True)
            relative = os.path.relpath(link.source, link.destination.parent)
            link.destination.symlink_to(relative, target_is_directory=link.source.is_dir())
        else:
            if link_state(link) != "owned":
                raise ValueError(f"Link changed during uninstall: {link.destination}")
            link.destination.unlink()
    print("Applied selection." if apply else "Preview only. Pass --apply to change links.")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("check", help="validate inventory, metadata, and local Markdown links")
    for action in ("install", "uninstall"):
        command = commands.add_parser(action, help=f"preview {action}; requires --apply to write")
        command.add_argument("--target", required=True, type=Path,
                             help="explicit OpenCode directory, such as /path/to/app/.opencode")
        command.add_argument("--agents", action="store_true", help="include optional OpenCode agents")
        command.add_argument("--apply", action="store_true", help="perform the previewed link changes")
    args = parser.parse_args(argv)
    try:
        if args.command == "check":
            data = validate(ROOT)
            print(f"Validated {len(data['skills'])} skills and {len(data['opencode_agents'])} agents.")
        else:
            planner = planned_links if args.command == "install" else uninstall_links
            links = planner(ROOT, args.target, args.agents)
            manage(links, args.command, args.apply)
    except (OSError, ValueError, RuntimeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
