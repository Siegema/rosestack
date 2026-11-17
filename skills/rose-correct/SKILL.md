---
name: rose-correct
description: Prevent explicitly scoped recurring mistakes with architecture, types, actionable checks, and behavior tests rather than more instructions
---

# Correct

Use when the user asks to prevent a recurring mistake or explicitly requests
enforcement while correcting it. Do not turn feedback into permission to modify
the stack, mine transcripts, add repository policy, or refactor unrelated code.
If only analysis is requested, return an enforcement proposal without edits.

1. Gather scoped evidence from the supplied examples, relevant commits, tests,
   review feedback, and project rules. Count distinct occurrences. Do not call a
   single example a demonstrated recurring class or search unrelated sessions.
2. Identify the root cause and current owner. Prefer, in order, eliminating the
   wrong path through architecture, making it invalid through types, an actionable
   lint/CI check, then a behavior test. Use docs only for residual judgment calls.
   Choose the highest effective level that fits the authorized change size.
3. Explain the proposed enforcement, false-positive risks, migration burden, and
   why a higher level is unsuitable. New policy, unrelated cleanup, or a broad
   ownership redesign needs approval; it is not implied by a narrow correction.
4. If implementation is authorized, add enforcement and fix the assigned case.
   Prove the check fails on a known bad example and passes on correct behavior.
   Use a fixture or isolated worktree; do not reintroduce the bug into the user's
   active sources. Use the same command in CI when CI integration is in scope.
5. Remove obsolete duplicated instructions only when the replacement is proven
   and removal is authorized. Preserve legal text, rationale, public contracts,
   tooling directives, and justified suppressions. Do not silently weaken gates.

Output each mistake class with evidence, root cause, chosen enforcement, negative
and positive proof, residual limitations, and any policy approval still needed.
If policy tracking is requested, map each rule to its enforcing artifact; do not
create an ever-growing instruction file as a substitute for executable checks.
