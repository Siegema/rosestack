---
name: rose-how
description: Explain existing subsystem behavior, runtime flow, ownership, and integration boundaries from repository evidence
---

# How

Build a working mental model before changing unfamiliar behavior. Use the current
host's permitted tools. This is an explanation, not an implementation request.
Do not mine unrelated sessions or assume private services are available.

1. State the subsystem and question. Reuse current evidence and inspect project
   instructions, entry points, callers, domain types, and relevant tests.
2. Trace one representative input from entry to validation, business decisions,
   persistence/external effects, and response or UI state. Follow asynchronous
   boundaries and failure handling; do not stop at an interface declaration.
3. Identify authoritative state, owners, public contracts, dependencies, and
   relevant web/mobile/API differences. Separate observed behavior from intended
   behavior and inference.
4. Cite file locations for key claims. Run a safe focused probe only when the task
   permits it and static evidence is insufficient. Never call unrun code observed.
5. Use scoped independent exploration only when complexity justifies it and the
   host allows it. The primary owns budget and synthesis; no nested fan-out.

Output a concise overview, key concepts, runtime flow, file/ownership map, and
gotchas. Omit irrelevant sections. State unknowns and the cheapest next check.
For historical motivation, identify the missing rationale rather than inventing
it from the current implementation. Do not require every small edit to run a full
subsystem investigation.
