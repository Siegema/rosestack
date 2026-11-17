# rosestack

Your development toolkit, built around business outcomes, explicit API contracts,
small changes, and observable proof. Portable skills come first. OpenCode is the
first adapter. Nothing here changes your default agent automatically.

## Skills

| Skill ID | Use it for |
| --- | --- |
| `rose-contract` | Translate business tasks into domain rules, API behavior, and acceptance evidence. |
| `rose-how` | Understand current behavior, request flow, and ownership. |
| `rose-architect` | Sketch types, interfaces, and boundaries before implementation. |
| `rose-arena` | Compare isolated candidates for a consequential decision. |
| `rose-blast-radius` | Find effects beyond the diff and test safety assumptions. |
| `rose-correct` | Prevent repeated mistakes with structure and executable checks. |
| `rose-verification` | Exercise real API, web, or mobile journeys and preserve evidence. |
| `rose-interrogate` | Challenge designs and changes without silently fixing them. |

Start a feature with `rose-contract`. Use only the other skills the task needs.
Small edits do not need an arena or a full architectural exercise.

## OpenCode quickstart

Requires Python 3.10+ and an OpenCode V2 installation. The installer supports
symlinks on Linux and macOS. Other hosts can copy individual self-contained skill
directories into their skill discovery location. Other host adapters are not yet
implemented or tested.

From this checkout, inspect the installation plan for a project:

```sh
python3 tools/stack.py check
python3 -m unittest discover -s tests -v
python3 tools/stack.py install --target /absolute/path/to/app/.opencode
```

Add `--apply` to create links. Add `--agents` if you also want the optional
`rose`, `rose-worker`, and `rose-reviewer` OpenCode agents. Select `rose` manually;
the installer never edits `opencode.json`, chooses a model, or changes defaults.
For a global installation, explicitly pass `--target ~/.config/opencode`.

Keep this checkout in place. Links track your local edits immediately. To update,
review and integrate changes into this checkout using your normal Git workflow,
rerun checks, then rerun the installer to link any new skills. There is no automatic
download or updater. Do not combine this with another source defining the same IDs.

Undo the same selection with:

```sh
python3 tools/stack.py uninstall --target /absolute/path/to/app/.opencode --agents
```

Uninstall also defaults to preview. Add `--apply` to remove only links whose stored
paths point directly to this checkout. It does not require valid skill contents
or a valid inventory, so a broken local edit does not prevent removal. Existing
files or foreign links in the selected `rose-*` namespace abort the operation;
they are never overwritten or recursively deleted. Symlinked target ancestors
and source trees are rejected. If an install fails partway through, it may
leave owned links; rerunning install converges, or uninstall removes those links.

## Layout and customization

- `skills/` contains the portable instructions and their local templates.
- `adapters/opencode/` contains optional native agents and integration notes.
- `docs/workflow.md` explains routing and delegation defaults.
- `docs/evaluation.md` defines behavior evaluations and their current status.
- `docs/skill-backlog.md` lists useful additions, not installed capabilities.
- `plugins/README.md` records plugin ideas. No runtime plugin ships in this version.
- `stack.json` is the inventory consumed by the checker and installer.
- `tools/stack.py` checks the inventory and manages explicit local links.

Edit skills in this repo rather than editing installed copies. Start by revising
contract examples to match your own business vocabulary. Targets for latency,
availability, volume, and recovery must come from project evidence or a product
decision, never from rosestack defaults.

The pstack-derived methods have been adapted rather than copied wholesale. See
[the provenance notice](NOTICE.md) for sources, licensing, and intentional changes.

Status: first-version skills and a deterministic installer test suite. Live
OpenCode discovery and agent reasoning evaluations must be recorded separately;
passing structural checks is not evidence that a skill produces good designs.
