# Contract template

Keep only relevant sections. Replace prompts with evidence, an accepted decision,
or an explicit unknown. Do not fill gaps with plausible business policy.

## Status and intent

- Status, owner, date, sources, and who can accept unresolved product decisions.
- Current behavior, desired business result, actors, and non-goals.
- Accepted decisions, constraints, provisional assumptions, and blocking questions.

## Business task map

| Task ID | Actor and trigger | Desired outcome | Rule/invariant | Operation | Acceptance evidence |
| --- | --- | --- | --- | --- | --- |
| TASK-001 | Who needs what, when? | Observable business result | What must remain true? | Capability, not necessarily a route | Named scenario/test and observable result |

## Domain and permissions

- Vocabulary, authoritative entities, ownership, and lifecycle transitions.
- Preconditions and invariants, including invalid transitions.
- Actor/object permissions, tenancy, sensitive data, and audit obligations.

## Operations

For each operation record:

- Task ID, consumer, protocol, preconditions, and permission checks.
- Input shape, validation, output shape, and schema source of truth.
- Success/rejection semantics, errors callers can act on, and side effects.
- Idempotency keys, scope, retention, payload mismatch, and duplicate outcome.
- Concurrent updates, ordering, consistency, cancellation, and uncertain outcomes.
- Version compatibility, deprecation/migration, and older mobile/web clients.

## Quality requirements

| Concern | Business risk | Requirement/target and source | Verification | Unknowns/tradeoff |
| --- | --- | --- | --- | --- |
| Reliability | Lost, duplicate, or inconsistent result | Explicit failure/recovery semantics | Fault/retry journey | Policy or infrastructure gaps |
| Scalability | Work exceeds capacity | Workload, payload, boundedness, latency, limits | Representative measurement | No invented target values |
| Maintainability | Changes break consumers or become hard to own | Ownership, schema, compatibility, diagnostics | Change/compatibility checks | Dependencies and migration costs |
| Security | Unauthorized action or disclosure | Actor/object/tenant rules and data handling | Positive and negative authorization cases | Threat assumptions |

## Client journeys and acceptance

- Happy path and observable durable outcome.
- Business rejection, validation, and unauthorized requests without side effects.
- Duplicate submission, timeout after commit, concurrent updates, and recovery.
- Relevant web accessibility and mobile offline/reconnect/stale-client behavior.
- Test location or planned evidence, fixture ownership, and unavailable checks.

## Decisions and handoff

List accepted decisions separately from open questions. Identify blockers,
responsible decision owners, risks accepted by whom, and the smallest next step.
