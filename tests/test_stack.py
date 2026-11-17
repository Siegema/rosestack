import contextlib
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from tools import stack


class StackTests(unittest.TestCase):
    def setUp(self):
        scratch = Path("/tmp/opencode")
        self.temp = tempfile.TemporaryDirectory(dir=scratch if scratch.is_dir() else None)
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.target = self.directory / "app" / ".opencode"

    def manage(self, action="install", apply=True, agents=True):
        planner = stack.planned_links if action == "install" else stack.uninstall_links
        links = planner(stack.ROOT, self.target, agents)
        with contextlib.redirect_stdout(io.StringIO()):
            stack.manage(links, action, apply)
        return links

    def fixture(self):
        root = self.directory / "fixture"
        shutil.copytree(stack.ROOT, root,
                        ignore=shutil.ignore_patterns(".git", "__pycache__", ".opencode"))
        return root

    def test_real_inventory_validates(self):
        data = stack.validate(stack.ROOT)
        self.assertEqual(len(data["skills"]), 8)
        self.assertEqual(len(data["opencode_agents"]), 3)

    def test_preview_has_no_side_effects(self):
        self.manage(apply=False)
        self.assertFalse(self.target.exists())

    def test_install_exposes_real_skills_and_agents(self):
        links = self.manage()
        self.assertEqual(len(links), 11)
        for link in links:
            self.assertTrue(link.destination.is_symlink())
            self.assertEqual(link.destination.resolve(), link.source.resolve())
        contract = self.target / "skills" / "rose-contract"
        self.assertIn("# Contract", (contract / "SKILL.md").read_text())
        self.assertTrue((contract / "references" / "contract-template.md").is_file())

    def test_install_is_idempotent(self):
        links = self.manage()
        before = [link.destination.lstat().st_ino for link in links]
        self.manage()
        self.assertEqual(before, [link.destination.lstat().st_ino for link in links])

    def test_agents_are_opt_in_and_configuration_is_untouched(self):
        self.target.mkdir(parents=True)
        config = self.target / "opencode.json"
        config.write_text('{"default_agent":"existing"}\n')
        links = self.manage(agents=False)
        self.assertEqual(len(links), 8)
        self.assertFalse((self.target / "agents").exists())
        self.assertEqual(config.read_text(), '{"default_agent":"existing"}\n')

    def test_conflict_aborts_before_any_links_are_created(self):
        conflict = self.target / "skills" / "rose-interrogate"
        conflict.mkdir(parents=True)
        (conflict / "owned.txt").write_text("keep")
        with self.assertRaisesRegex(ValueError, "Refusing existing"):
            self.manage()
        self.assertFalse((self.target / "skills" / "rose-contract").exists())
        self.assertEqual((conflict / "owned.txt").read_text(), "keep")

    def test_dangling_foreign_link_is_not_overwritten(self):
        conflict = self.target / "skills" / "rose-contract"
        conflict.parent.mkdir(parents=True)
        conflict.symlink_to(self.directory / "missing")
        with self.assertRaisesRegex(ValueError, "foreign link"):
            self.manage()
        self.assertTrue(conflict.is_symlink())

    def test_symlinked_target_parent_is_rejected(self):
        shared = self.directory / "shared"
        shared.mkdir()
        self.target.mkdir(parents=True)
        (self.target / "skills").symlink_to(shared, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "symlinked target"):
            self.manage()
        self.assertEqual(list(shared.iterdir()), [])

    def test_uninstall_preview_and_apply_preserve_unrelated_files(self):
        links = self.manage()
        keep = self.target / "skills" / "other.md"
        keep.write_text("keep")
        self.manage(action="uninstall", apply=False)
        self.assertTrue(all(link.destination.is_symlink() for link in links))
        self.manage(action="uninstall")
        self.assertTrue(all(not link.destination.is_symlink() for link in links))
        self.assertEqual(keep.read_text(), "keep")
        self.manage(action="uninstall")

    def test_uninstall_rejects_replaced_link(self):
        links = self.manage()
        replaced = links[-1].destination
        replaced.unlink()
        replaced.write_text("user replacement")
        with self.assertRaisesRegex(ValueError, "Refusing existing"):
            self.manage(action="uninstall")
        self.assertTrue(links[0].destination.is_symlink())
        self.assertEqual(replaced.read_text(), "user replacement")

    def test_symlinked_source_ancestors_are_rejected(self):
        root = self.fixture()
        for relative in ("adapters/opencode/agents", "skills"):
            with self.subTest(relative=relative):
                source = root / relative
                external = self.directory / source.name
                source.rename(external)
                source.symlink_to(external, target_is_directory=True)
                with self.assertRaisesRegex(ValueError, "Source escapes checkout"):
                    stack.validate(root)
                source.unlink()
                external.rename(source)

    def test_internal_source_symlink_is_rejected(self):
        root = self.fixture()
        source = root / "adapters" / "opencode" / "agents"
        internal = root / "moved-agents"
        source.rename(internal)
        source.symlink_to(internal, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "Source must not contain symlinks"):
            stack.validate(root)

    def test_uninstall_works_after_invalid_edits_and_deleted_sources(self):
        root = self.fixture()
        links = stack.planned_links(root, self.target, True)
        with contextlib.redirect_stdout(io.StringIO()):
            stack.manage(links, "install", True)
        (root / "skills" / "rose-how" / "SKILL.md").write_text("invalid metadata")
        (root / "stack.json").write_text("invalid JSON")
        shutil.rmtree(root / "skills" / "rose-contract")
        discovered = stack.uninstall_links(root, self.target, True)
        self.assertEqual(len(discovered), 11)
        with contextlib.redirect_stdout(io.StringIO()):
            stack.manage(discovered, "uninstall", True)
        self.assertTrue(all(not link.destination.is_symlink() for link in links))

    def test_uninstall_does_not_treat_indirect_source_alias_as_owned(self):
        self.manage()
        destination = self.target / "skills" / "rose-how"
        destination.unlink()
        alias = self.directory / "alias"
        alias.symlink_to(stack.ROOT / "skills" / "rose-how", target_is_directory=True)
        destination.symlink_to(alias, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "foreign link"):
            self.manage(action="uninstall")
        self.assertTrue(destination.is_symlink())

    def test_reviewer_does_not_override_host_shell_rules(self):
        path = stack.ROOT / "adapters" / "opencode" / "agents" / "rose-reviewer.md"
        self.assertNotIn("action: shell", path.read_text())

    def test_invalid_manifest_id_is_rejected(self):
        root = self.fixture()
        data = json.loads((root / "stack.json").read_text())
        data["skills"][0] = "../../escape"
        (root / "stack.json").write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, "Invalid skills ID"):
            stack.validate(root)

    def test_duplicate_manifest_id_is_rejected(self):
        root = self.fixture()
        data = json.loads((root / "stack.json").read_text())
        data["skills"].append(data["skills"][0])
        (root / "stack.json").write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, "Duplicate IDs"):
            stack.validate(root)

    def test_unlisted_skill_is_rejected(self):
        root = self.fixture()
        extra = root / "skills" / "rose-extra"
        extra.mkdir()
        (extra / "SKILL.md").write_text("# Not inventoried")
        with self.assertRaisesRegex(ValueError, "inventory mismatch"):
            stack.validate(root)

    def test_missing_description_is_rejected(self):
        root = self.fixture()
        path = root / "skills" / "rose-how" / "SKILL.md"
        path.write_text("---\nname: rose-how\n---\n# How\n")
        with self.assertRaisesRegex(ValueError, "matching name and a description"):
            stack.validate(root)

    def test_broken_reference_is_rejected(self):
        root = self.fixture()
        path = root / "skills" / "rose-how" / "SKILL.md"
        path.write_text(path.read_text() + "\n[Missing](references/missing.md)\n")
        with self.assertRaisesRegex(ValueError, "Broken or escaping link"):
            stack.validate(root)

    def test_skill_cannot_depend_on_another_directory(self):
        root = self.fixture()
        path = root / "skills" / "rose-how" / "SKILL.md"
        path.write_text(path.read_text() + "\n[External](../../README.md)\n")
        with self.assertRaisesRegex(ValueError, "not self-contained"):
            stack.validate(root)

    def test_cli_requires_explicit_target(self):
        result = subprocess.run([sys.executable, str(stack.ROOT / "tools" / "stack.py"),
                                 "install"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn("--target", result.stderr)

    def test_cli_round_trip_and_check(self):
        command = [sys.executable, str(stack.ROOT / "tools" / "stack.py")]
        result = subprocess.run(command + ["check"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        for action in ("install", "uninstall"):
            result = subprocess.run(command + [action, "--target", str(self.target),
                                               "--agents", "--apply"],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse((self.target / "skills" / "rose-contract").exists())


if __name__ == "__main__":
    unittest.main()
