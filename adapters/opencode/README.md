# OpenCode V2 adapter

The installer links portable skill directories into `<target>/skills` and, only
with `--agents`, links these agent files into `<target>/agents`. It never writes
configuration, permissions, model selections, or default-agent settings.

Use a project's `.opencode` directory for project-local discovery or explicitly
choose `~/.config/opencode` for global discovery. Both are documented V2 locations.
Select `rose` manually. Individual skills remain usable from another permitted
agent, without switching agents or expanding its authority.

Agent models inherit the current session. Worker and reviewer roles cannot launch
children. The reviewer denies edit tools and inherits shell permissions without
adding overrides that could relax a host denial. This is not a filesystem
sandbox: permitted shell commands can still write files, so the prompt
prohibits source edits and requires isolated scratch paths for repro artifacts.
The primary and worker do not add broad allow rules over inherited permissions.

References consulted for this first adapter:

- https://opencode.ai/v2/docs/skills
- https://opencode.ai/v2/docs/agents
- https://opencode.ai/v2/docs/config
- https://opencode.ai/v2/docs/build/plugins

Config changes are watched by OpenCode. Do not recommend restarting its background
service merely to discover these files. Use `/reload` if a forced reload is needed.
Runtime loading has not yet been smoke-tested by this repository's test suite.
