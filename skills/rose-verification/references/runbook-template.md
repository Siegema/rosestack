# Project verification runbook

Status: draft until run end to end. Replace every prompt below with project facts
or an explicit blocker. Do not treat these prompts as executable instructions.

## Target and safety

Record build/revision, surface, environment, fixture accounts, authorization,
data isolation, ports/device ownership, dependencies, and side effects that must
not escape the test environment. Record what any mock or stand-in cannot prove.

## Launch and doctor

Provide exact trusted setup/start commands, readiness conditions, migrations and
seed requirements, process handles, and a read-only identity/health check. Identify
the failure cleanup command before launching. Do not print secrets in commands.

## Feature map

| Task ID / journey | Entry point and preconditions | Driver / exact check | Expected state and side effects | Evidence | Status |
| --- | --- | --- | --- | --- | --- |
| Accepted business task | API operation, web path, or mobile flow | Real harness and assertions | User-visible and durable result | Sanitized artifact path | Passed, failed, blocked, or not run |

## Failure and compatibility cases

Record business rejection, invalid input, unauthorized/other-tenant access,
duplicate/retried requests, partial failure, concurrency, and relevant web/mobile
offline, permissions, reconnect, and old-client behavior. Explain irrelevant cases.

## Evidence and teardown

Specify where action traces, assertions, screenshots/responses, and observed side
effects are captured. Redact credentials and personal data at capture time. Keep
evidence separate from disposable runtime state. Stop only owned processes and
remove only owned fixtures. Confirm evidence exists after cleanup. Record cleanup
failures rather than hiding them behind a successful journey.

## Run record

Record date, build, environment, exact commands, exit codes, observed results,
artifact paths, gaps, and next checks. Distinguish a draft recipe from one executed
against the actual target.
