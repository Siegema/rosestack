---
name: rose-contract
description: Align business tasks, domain rules, and API behavior with testable reliability, scalability, and maintainability needs before implementation
---

# Contract

Use when defining or changing business-facing behavior, an API, or a cross-client
workflow. Start with what the business and its users need to accomplish, not CRUD
routes or an infrastructure choice. A contract is an observable agreement, not
just an OpenAPI schema. Stay within the user's scope and host permissions.
Contract discovery does not itself authorize implementation or production access.

## Discover

1. Read the task, relevant product material, existing domain types, API schemas,
   callers, tests, and operational constraints. Distinguish current from desired
   behavior. Cite sources; do not treat existing code as proof of business intent.
2. Identify actors and their tasks. For each, record the trigger, desired outcome,
   business value, failure cost, and explicit non-goals.
3. Establish domain language, ownership, lifecycle states, legal transitions,
   invariants, authorization, tenancy, and data classification. Ask about unknown
   business policies only when the answer materially changes behavior.
4. Separate accepted decisions, evidence-backed constraints, provisional
   assumptions, and unresolved questions. Do not silently promote assumptions.

## Specify behavior

Use [the contract template](references/contract-template.md). Give each business
task a stable ID and map it to an operation, business rule, and acceptance test.
Describe preconditions, inputs, outputs, error semantics, side effects, and what
the caller can observe after success, rejection, timeout, or partial failure.
Choose the protocol from project needs; do not force HTTP or REST.

- Reliability: define duplicate/retry handling, idempotency scope and retention,
  concurrency, ordering, consistency, dependency failures, and recovery. Specify
  who owns reconciliation when a response is lost after a committed operation.
- Scalability: establish observed or expected workload, payloads, hot keys, latency
  percentiles, pagination, bounded work, rate limits, and backpressure where
  relevant. Record unknown targets and a measurement plan. Never invent numbers
  or choose queues, caches, or services merely because scale is mentioned.
- Maintainability: define ownership boundaries, source-of-truth schemas, version
  compatibility, migration strategy, dependency assumptions, and observability.
  Include safe diagnostics without exposing personal data or credentials.
- Security: define actor/object authorization, tenant isolation, sensitive-field
  handling, abuse cases, and audit requirements. Do not equate authentication with
  permission to perform a business operation.
- Web/mobile: consider repeated submissions, stale clients, offline retries,
  reconnect/reconciliation, permission denial, and accessible failure/recovery
  states. Separate device-local intent from server-authoritative state.

For each quality requirement, specify a measurable acceptance criterion or mark
it unresolved. Explain tradeoffs in terms of business risk and maintenance cost.
Avoid implementation detail unless it is required to guarantee the contract.

## Check and hand off

Walk one happy path, one business rejection, one unauthorized request, and the
important retry/failure path. Check each invariant across those paths. For a tiny
change, keep only relevant sections and explain omissions. Use
[the booking example](references/booking-example.md) as a shape, not policy.

Output the task-to-operation acceptance map, contract, open decisions, assumptions,
and the smallest next design or verification step. A blocking policy question
means the affected contract is a draft. Do not present a draft as accepted, write
implementation to guess the answer, or claim a schema alone proves alignment.
