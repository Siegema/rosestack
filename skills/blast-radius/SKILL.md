---
name: blast-radius
description: Trace contracts and downstream effects beyond a change and test the key assumptions that make it safe
---

# Blast radius

Find breakage outside the visible diff. Preserve task scope and host permissions.
An assessment does not authorize production probes, source edits, or a refactor.

1. Establish the exact diff and intended business behavior. Identify changes to
   runtime timing, defaults, failure handling, serialization, and state ownership,
   not just changed symbols.
2. Trace direct callers and hidden consumers: wire schemas, stored data, generated
   clients, jobs, caches, feature flags, older web/mobile versions, and operational
   processes. Inspect relevant pinned dependency behavior when it matters.
3. Name the one or two assumptions that most strongly support safety. For each,
   identify evidence, a plausible counterexample, and the cheapest meaningful
   check. A caller list or absence of grep matches is not proof of compatibility.
4. Run safe focused checks when authorized. Prefer the real function, consumer,
   or application over a stand-in. Record exact commands and observed results.
   Mark static reasoning and unavailable runtime proof separately.
5. Prioritize risks by consequence and evidence. Distinguish reproduced breaks,
   credible static risks, hypotheses, and cases actually checked and cleared.
   Do not invent a numeric probability or claim untested consumers are safe.

Output intended behavior, affected contracts/consumers, key safety assumptions
with evidence level, prioritized risks, cleared cases, and remaining pre-merge
checks. If no runnable target exists, say what remains unproven. A small diff can
have a large contract impact; a long risk list is not a substitute for evidence.
