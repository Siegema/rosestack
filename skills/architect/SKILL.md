---
name: architect
description: Design usage, domain types, API signatures, ownership, and module boundaries for consequential changes without implementing by default
---

# Architect

Use when implementation would lock in an important interface, state model, or
ownership decision. Stay in the user's scope and host permissions. Produce a
design unless implementation was also explicitly requested. A function boundary
alone does not justify a design exercise.

1. Ground the design in accepted business tasks and contract invariants. Inspect
   current flow, callers, compatibility constraints, and existing rationale.
   If the contract is unclear, name blocking product questions before designing
   around invented policies.
2. Write the caller's usage first, including error/retry behavior. Derive domain
   types and state transitions from it. Name authoritative state and its owner.
3. Sketch signatures, boundaries, validation, dependencies, and side effects.
   Parse untrusted input at system boundaries. Encode invalid states out of the
   model when practical; do not add wrappers that merely forward one call.
4. Compare a smaller/default design against a structurally different alternative
   when the tradeoff matters. Use an arena only for costly uncertainty. If both
   alternatives are yours, label them as one author's exploration, not independent
   perspectives. Do not claim different models without establishing that fact.
5. Evaluate contract coverage, interface simplicity, failure semantics, security,
   compatibility, operational cost, and maintainability. Tie scale choices to
   stated workloads. Prefer fewer owners and less hidden shared mutable state.

Output the usage sketch, domain/types, module map, important signatures, accepted
tradeoffs, rejected alternatives, migration needs, and verification plan. Mark
unresolved assumptions and stop at a draft where policy is blocking.

If implementation is authorized, follow the chosen shape and surface meaningful
deviations. Repeated workarounds, unchecked casts, or callers needing internals
signal a design problem. Re-ground and simplify rather than patching around a
wrong model. Do not delete or rewrite working code merely because a sketch changed.
