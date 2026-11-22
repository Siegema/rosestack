---
name: benchmark
description: Audit performance claims for correct work, comparable tuning, bottlenecks, repeatability, and end-to-end relevance
---

# Benchmark

Use before reporting or acting on a performance measurement. Stay within scope
and host permissions. A request to assess a number does not authorize a long
benchmark, spending, infrastructure changes, or production load.

1. State the claim, unit, workload, baseline, environment, and intended consumer.
   Read what the harness times, counts, excludes, and actually awaits or consumes.
2. Confirm correct outputs, errors, retries, and completed work. Fast rejection,
   cached/no-op execution, lazy work outside the timer, or an overloaded load
   generator must not masquerade as a speedup.
3. Compare representative, equally tuned configurations: release settings, versions,
   data, concurrency, batching, pools, and warm/cold caches. If a side is untuned,
   do not select an implementation winner from that comparison.
4. Identify the limiter from evidence. Keep profiling separate from reported timing.
   Check results against physical throughput and the changed component's share of
   total time. Explain unexpected gains rather than accepting impossible numbers.
5. When measurement is authorized, alternate comparable runs to reduce drift.
   For a real comparison, aim for at least five runs per side; report run count,
   median, range, variability, hardware, and interference. A single requested
   ballpark is acceptable only when labeled as one run, not a comparative verdict.
6. Relate microbenchmarks to the end-to-end business task. Do not generalize past
   the measured workload, supported environment, or exercised failure behavior.

Output faster, slower, no measurable difference, or inconclusive, with evidence,
limiter, configuration, correctness/error counts, reproducibility, and gaps.
If no measurements were run, report an audit or measurement plan, not a measured
result. Unknown correctness, missing completed-work evidence, or incomparable
tuning makes the adoption verdict inconclusive.
