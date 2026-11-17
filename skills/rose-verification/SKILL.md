---
name: rose-verification
description: Create or maintain a project-grounded verification runbook, exercise real API, web, and mobile behavior, and preserve evidence with honest gaps
---

# Verification

Prove the business behavior against the actual artifact. A build, passing unit
tests, a candidate's report, and a successful health check are not substitutes for
the user journey. Stay within scope and host permissions. Inspect project code
before running it. Never use production data or send real messages/payments just
to obtain proof. A method does not authorize environment installation or deployment.

## Discover and plan

Read the accepted task/API contract, project instructions, run commands, test
harnesses, auth/seed requirements, and existing verification docs. Identify surfaces
and fixtures. Reuse existing tools before introducing dependencies. Determine how
to isolate ports, data, accounts, device/simulator, and process ownership.

Use [the runbook template](references/runbook-template.md) if no reliable runbook
exists. Replace placeholders with observed project commands before calling it
executable. A runbook that has not been run is a draft. Missing infrastructure
or permissions are explicit blockers, not passing checks.

Map business task IDs to journeys, entry points, expected state and side effects,
negative cases, and evidence. API success does not establish mobile/web behavior.
For a cross-client flow, include its affected clients or state the coverage gap.

## Run

1. Launch an isolated target using the project's supported recipe. Readiness means
   usable fixtures, auth, migrations, and dependencies, not just a listening port.
2. Doctor the target: confirm build/version, owned process or endpoint, environment,
   and safe fixture identity before sending actions. Never drive an unknown shared
   instance or assume a dry-run avoids network calls and side effects.
3. Exercise the real entry point. For APIs, verify response/error contracts,
   authorization/tenancy, durable side effects, retry/idempotency, and relevant
   concurrency. For web, use semantic selectors and verify interaction, state,
   errors, and accessibility where affected. For mobile, use the project's device
   harness and include relevant platform permissions, offline/reconnect behavior,
   stale clients, and lifecycle transitions. Do not invent harness commands.
4. Capture the action and resulting observable state, not just a final screenshot
   or status code. Assert invariants and important negative cases. Label mocks,
   emulators, and stand-ins with what real behavior they do not establish.
5. Clean up after both success and failure. Stop only processes and fixtures this
   run owns. Preserve evidence outside scratch teardown. Redact secrets and
   personal data before recording or sharing artifacts; raw credentials must not
   enter committed logs, screenshots, or reports.

## Report and maintain

Report task IDs, surface/build/environment, exact checks, expected versus observed
results, sanitized artifact paths, cleanup outcome, assumptions, and gaps. Confirm
evidence survives cleanup. Do not claim a load test proves scale beyond its actual
workload or hardware. Separate deterministic tests from live integration checks.

When behavior changes, compare affected routes/features to the runbook and update
stale commands and expected results only within authorized scope. Never weaken
the expected journey to make a broken implementation pass. For broad work, keep a
feature map and state which mapped journeys were and were not exercised.
