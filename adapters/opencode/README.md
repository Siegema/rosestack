# OpenCode V2 adapter

The installer links unprefixed portable skill directories into `<target>/skills` and, only
with `--agents`, links these agent files into `<target>/agents`. It never edits
JSON configuration, model selections, or default-agent settings; linked agent
files carry permissions that apply when loaded.

Use a project's `.opencode` directory for project-local discovery or explicitly
choose `~/.config/opencode` for global discovery. Both are documented V2 locations.
Select `rose` manually. Optional generic `build`, `editor`, `docs`, and `reviewer`
roles are also included; explicitly installing `build` replaces the built-in role
when discovered. Agent files supply permissions when loaded. The installer refuses
existing files and foreign links; a one-time migration needs explicit user approval.
Relative links follow this checkout. No model or default is changed by installation.
Individual skills remain usable without switching agents or expanding authority.

Agent models inherit the current session unless configured locally. The legacy
rose worker and rose-reviewer cannot launch children; rose-reviewer denies edits
and inherits shell permissions. The generic reviewer asks for shell approval;
generic docs defaults to deny. These rules are not a filesystem sandbox: prompts
also prohibit source edits and require isolated scratch paths for repro artifacts.
The rose primary and worker do not add broad allow rules over inherited permissions.

References consulted for this first adapter:

- https://opencode.ai/v2/docs/skills
- https://opencode.ai/v2/docs/agents
- https://opencode.ai/v2/docs/config
- https://opencode.ai/v2/docs/build/plugins

Config changes are watched by OpenCode. Do not recommend restarting its background
service merely to discover these files. Use `/reload` if a forced reload is needed.
Global discovery links have been checked against the native skill registry for
all 10 combined methods, and `why` was smoke-loaded. Optional agent execution and
model-behavior evaluations remain unverified.
