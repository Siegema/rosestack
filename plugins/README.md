# Plugin candidates

No executable plugin ships in version one. Skills describe the process; plugins
should be added only when runtime integration solves an observed problem.

1. Evidence index. Record verification commands, sanitized artifact paths, and
   outcomes. Never collect transcripts or credentials implicitly.
2. Contract coverage. Map accepted task IDs to API operations and test evidence.
   Missing links should produce useful diagnostics, not invented coverage.
3. Scoped handoff. Produce a review packet from explicitly selected project
   evidence without mining unrelated sessions.

Each plugin needs its own approved contract, permission model, failure behavior,
tests, pinned supported host versions, and explicit installation. Runtime hooks
are platform-specific and belong in adapters, not in portable core skills.
