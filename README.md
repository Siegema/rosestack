# rosestack

Your development toolkit, built around business outcomes, explicit API contracts,
small changes, and observable proof. Portable skills come first. OpenCode is the
first adapter. Nothing here changes your default agent automatically.

## Skills

| Skill ID | Use it for |
| --- | --- |
| `contract` | Translate business tasks into domain rules, API behavior, and acceptance evidence. |
| `how` | Understand current behavior, request flow, and ownership. |
| `architect` | Sketch types, interfaces, and boundaries before implementation. |
| `arena` | Compare isolated candidates for a consequential decision. |
| `blast-radius` | Find effects beyond the diff and test safety assumptions. |
| `correct` | Prevent repeated mistakes with structure and executable checks. |
| `verification` | Exercise real API, web, or mobile journeys and preserve evidence. |
| `interrogate` | Challenge designs and changes without silently fixing them. |
| `why` | Investigate the evidence behind decisions without inventing history. |
| `benchmark` | Audit performance claims and plan comparable measurements. |

Start a feature with `contract`. Use only the other skills the task needs.
Small edits do not need an arena or a full architectural exercise.
This is the single editable source for the combined pstack/rosestack methods.
The global OpenCode `skills/` directory exposes these directories through links;
there are no duplicate prefixed aliases. The former `pstack-review` method is
consolidated into `interrogate`. The `/review` command uses the dedicated reviewer when installed.

## OpenCode quickstart

Requires Python 3.10+ and an OpenCode V2 installation. The installer supports
symlinks on Linux and macOS. Other hosts can copy individual self-contained skill
directories into their skill discovery location. Other host adapters are not yet
implemented or tested.
Redistribution of adapted skills must retain `NOTICE.md` and `licenses/pstack-MIT.txt`.

From this checkout, inspect the installation plan for a project:

```sh
python3 tools/stack.py check
python3 tools/stack.py install --target /absolute/path/to/app/.opencode
```

Add `--apply` to create links. Add `--agents` if you also want the optional
`rose`, `rose-worker`, `rose-reviewer`, and generic `build`, `editor`, `docs`,
and `reviewer` OpenCode agents. Select `rose` manually. Explicit installation of
`build` replaces the built-in role when discovered; loaded agent files carry their
permission rules. The installer never edits `opencode.json`, chooses a model, or
changes defaults. Existing files and foreign links still cause a conflict. A
one-time replacement of an existing file requires explicit user authorization;
relative links follow this canonical checkout.
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
paths point directly to this checkout. Both relative and absolute owned links are
recognized, including dangling links with retired prefixed names. It does not
require valid skill contents or a valid inventory, so a broken local edit does not
prevent removal. Unrelated files, replacement files, and foreign links are ignored
by uninstall. Install still refuses conflicts before creating any links. Neither
operation overwrites files or recursively deletes directories. Symlinked target
ancestors and source trees are rejected. If an install fails partway through, it may
leave owned links; rerunning install converges, or uninstall removes those links.

When upgrading an older prefixed installation, preview and apply uninstall first,
then preview and apply install to expose the new IDs. The uninstaller removes only
owned links, not old pstack wrapper files or another installation's definitions.
Those require an explicitly scoped migration rather than silent replacement.

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

Status: the combined 10 methods were discovered through global OpenCode links,
and `why` was smoke-loaded through the native skill tool. Structural and installer
checks pass. Agent reasoning evaluations and optional adapter-agent execution
remain unverified; registration is not evidence that a skill produces good designs.
