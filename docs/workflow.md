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
