# Development workflow

## Route by uncertainty

| Question | Method | Deliverable |
| --- | --- | --- |
| What business task are we supporting? | contract | Outcomes, invariants, API behavior, acceptance map. |
| What exists today? | how | Cited flow and ownership map. |
| What should own this behavior? | architect | Usage sketch, types, boundaries, tradeoffs. |
| Is the design choice costly and uncertain? | arena | Compared candidates and one coherent recommendation. |
| What else could break? | blast-radius | Contract/caller map and safety evidence. |
| Did it actually work? | verification | Commands, observations, artifacts, gaps. |
| What are we overlooking? | interrogate | Defects, risks, and hypotheses by severity. |
| Why does the same mistake recur? | correct | Scoped enforcement and negative proof. |

This is not a mandatory pipeline. Start with the user's scope, reuse evidence,
and skip irrelevant work. A narrow bug fix can need only a repro and verification.
For new API behavior, map a business task to an operation before choosing routes
or implementation structure. Security and authorization are part of that contract.

## OpenCode adapter

The optional Build dispatcher may edit tiny certain single-file changes directly;
it routes broad discovery to Explore, external documentation to Docs, and multi-file
or uncertain implementation to Editor. Nontrivial integrated changes require a
fresh Reviewer and final child reports before completion. These adapter instructions
do not mandate delegation in portable skills or other hosts.

## Design workflow

Select the optional `design` primary manually for a scoped presentation or layout
task. It may use `design-scout`, `design-editor`, and `design-reviewer`; Build's
delegation allowlist remains unchanged. Preserve behavior, APIs, and data, and use
the existing visual language by default. Creating a new page requires explicit user
scope. Document observed behavior rather than guessing.

Before edits, establish the requested or agreed visual direction, using the existing
visual language by default; ask if a material direction is unsettled, not when it is
already clear. Implementation authorization is required for source edits, launching
`design-editor`, and creating or updating the inventory. Design-only discussion may
read, scout, and propose direction and inventory entries, but not edit. Once direction
and authorization are established, maintain the inventory without another permission
prompt.

During a Design task, explicitly read the project-root, exact-case
`Agents-Design.md`. It is not `AGENTS.md` and is not auto-loaded: do not add it to
config instructions or global `AGENTS.md`. Start consumer applications with the
[unpopulated template](templates/Agents-Design.md), not a toolkit page inventory.
Reconcile stale entries against code and read only entries relevant to the task to
reduce context. For authorized implementation, add entries for new or edited pages
and undocumented pages newly discovered within the task. The primary is the sole
inventory writer; children report documentation changes and the reviewer verifies them.

Agent prompts are isolated on invocation, but descriptions of available children
may appear in catalogs. This is not a security sandbox or a claim of zero context
overhead. The optional Design agents have not been runtime or browser evaluated;
registration does not establish design quality or effective semantic isolation.

## Ownership and budget

The primary owns scope, evidence, integration, and final verification. Use direct
work for small tasks. If the host permits delegation, default to two concurrent
children and six total launches, counting retries and reviews. Reserve one launch
for fresh final review and one for a possible follow-up on nontrivial changes.
Do not nest fan-out. These are workflow limits, not a security or billing sandbox.

Before each launch, state used/remaining budget, purpose, and output ownership.
Brief every child with the user goal, exact scope/base, owned paths or worktree,
success criteria, checks, permission boundaries, and no-publication restriction.
Writers use disjoint paths or isolated worktrees. Reviewers do not edit sources.
The parent inspects the integrated diff and reruns important checks. An old review
does not cover a material repair. Report same-model review explicitly.

When delegation is unavailable, work proportionally in the current context.
Do not call self-review independent review or describe serial alternatives as an
arena with independent candidates. Report any essential unavailable check.

## Decision boundaries

Observe facts from the repository before asking the user. Ask only material
business, product, or permission questions that evidence cannot settle. Do not
invent business rules, SLOs, supported versions, budgets, or scale requirements.
Mark assumptions and keep unresolved decisions separate from accepted contracts.

No skill permits bypassing host restrictions. Read project instructions before
running project code. Do not access unrelated sessions, secret stores, production
systems, or external communications without explicit scope and authorization.
Do not silently change this stack, default agents, models, permissions, or plugins.
Never auto-merge, force-push, deploy, or delete production data.

## Handoff

Report the business outcome, changed behavior, checks actually run, observed
results, evidence locations, assumptions, remaining risks, and branch/publication
status. Missing infrastructure is a blocker, not a pass. Keep rationale, legal
headers, public contracts, tooling directives, and justified suppressions.
