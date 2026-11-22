---
name: interrogate
description: Adversarially review a scoped design or patch, separating reproduced defects, evidence-backed risks, and hypotheses without applying fixes
---

# Interrogate

Challenge the change against its intended business/API contract. Review is not
permission to fix, publish, read unrelated sessions, or probe production systems.
Use the host's permitted tools and the primary's remaining launch budget.

1. Establish exact scope/base, intent, accepted invariants, and affected surfaces.
   Read the final integrated artifact, not only an author's summary. Identify what
   is excluded. For a design, focus on assumptions, ownership, failure paths, and
   compatibility rather than inventing implementation defects.
2. If independent adversaries are justified and permitted, give each the same
   scope/intent and an isolated repro location. Ask them to break authorization,
   tenancy, state transitions, retry/concurrency, compatibility, and operational
   assumptions that matter here. No edits to application sources, publication,
   nested delegation, or unsafe production probes. The primary owns integration.
3. Seek runnable counterexamples. Record exact commands, output, expected behavior,
   and why the difference violates intent. Rerun important repros when feasible.
   Keep credible static/security risks even when a runtime is unavailable; state
   the evidence and missing check instead of claiming proof or discarding them.
4. Deduplicate by root cause and reject findings contradicted by evidence. Do not
   promote style preferences, speculative future consumers, or ungrounded risks
   into defects. Prioritize by severity and confidence without invented precision.

Output intent and coverage, then separate reproduced defects, evidence-backed
risks, and unverified hypotheses. Each finding needs location, impact, evidence,
confidence, and the cheapest next check. Report cleared/dropped claims and why,
checks not run, reviewer independence, and same-model limitations. If no defects
were reproduced, say so; do not equate that with proven safety. Do not apply fixes.
