---
name: why
description: Investigate the evidence behind a design decision, policy, workaround, or threshold without inventing historical intent
---

# Why

Explain why a system took its current shape, not merely how it works. Stay within
the user's scope and host permissions. This is investigation, not a fix request.
Do not search unrelated sessions, private services, or secret stores.

1. Name the target decision and question. Anchor it in relevant code, comments,
   tests, and existing evidence. Distinguish current behavior from historical intent.
2. Inspect focused history and linked design records or PR discussion when available
   and permitted. A last-touch commit is not necessarily the originating decision.
   Follow only sources that can answer this question; do not open every service.
3. Keep narrow questions inline. For broad discovery, use at most one focused
   read-only child initially if allowed. Ask for concise cited evidence and reuse
   it. Additional launches need a specific evidence gap. Never require an upstream
   investigator fleet, separate synthesizer, or particular model.
4. Separate documented rationale, evidence-backed inference, competing hypotheses,
   and unknowns. Cite file/line, commit, or a source actually inspected. Missing
   history is a limitation, not permission to invent a convincing explanation.
5. If this precedes a change, identify constraints to preserve, behavior that can
   change, approaches to avoid, and risks needing verification. Do not make the
   change unless implementation was also requested.

Output the question, strongest evidence, supported explanation, uncertainty,
sources consulted, and cheapest next check. Scale the answer to the question;
skip a long report when one cited decision record answers it.
