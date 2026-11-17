# Sources and intentional adaptations

Rosestack's architect, arena, blast-radius, correct, how, interrogate, and
verification methods are adapted from Lauren Tan's pstack. Reference snapshot:

- Repository: https://github.com/cursor/plugins
- Revision: `3dbd22ff12742fb28c9700b9760baa29ed41dc13`
- Source plugin: pstack, including `skills/architect`, `skills/arena`,
  `skills/blast-radius`, `skills/correct`, `skills/how`, `skills/interrogate`,
  `skills/create-verification-skill`, and `skills/maintain-verification-skill`.
- The upstream MIT notice is retained at `licenses/pstack-MIT.txt`.

No upstream scripts, dependencies, automatic updater, or moving snapshot ships.
Rosestack's contract workflow is newly authored for the user's business-first API
workflow. Broader licensing of newly authored material is left for the repository
owner to choose; the upstream notice does not license the entire repository.

Intentional differences:

- Portable core skills, with platform-specific behavior in adapters.
- Skills never expand permission, publish, deploy, change defaults, mine unrelated
  sessions, or modify their own installation without an explicit user request.
- Architect is design-only unless implementation is separately requested.
- Arena is selective, bounded, and honest about same-model or single-agent work.
- Interrogate separates reproduced defects, evidence-backed risks, and hypotheses.
  Static security findings are not discarded for lack of runtime reproduction.
- Correct stays within the requested correction. New policy and unrelated
  refactoring require approval; it is not automatic self-modification.
- Verification combines runbook creation, execution, evidence, and drift checks,
  with concrete recipes discovered from each target project.
- No automatic comment deletion, model pinning, merge, deployment, or force-push.
