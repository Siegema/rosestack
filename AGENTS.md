# Working on rosestack

Rosestack is a portable, editable development toolkit. Backend APIs, web apps,
and mobile apps are the first supported workflows. OpenCode is the first adapter.

- Keep core skills self-contained and independent of provider-specific tools,
  model names, absolute paths, and this machine's configuration.
- Keep runtime integration in adapters. Do not install into active configuration,
  change a default agent, or load plugins as a side effect of development.
- Preserve the user's scope and host permissions. Skills are methods, not grants
  of authority. Design and review requests do not authorize implementation.
- New skills belong in `skills/<rose-id>/SKILL.md` and `stack.json`.
- Update the upstream notice when adapting upstream material. No automatic fetches
  or execution of upstream code.
- Treat workflow improvements as proposals until explicitly approved.

Run `python3 tools/stack.py check` and `python3 -m unittest discover -s tests -v`.
These check structure and installer behavior, not the quality of model reasoning.
Use `docs/evaluation.md` for behavior evaluations before promoting skill changes.
