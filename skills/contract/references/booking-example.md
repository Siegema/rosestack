# Example: booking across web and mobile

This is a hypothetical discovery example, not a production-ready policy or design.
No refund, capacity, response-time, or uptime rule is implied.

## Known user intent

TASK-001: An authenticated customer submits a booking and can determine whether
it was accepted, even if the network drops before they receive the response.
Web and mobile use the same server-authoritative booking state.

## Draft acceptance map

| Task | Proposed operation | Observable acceptance |
| --- | --- | --- |
| TASK-001 | Submit booking intent | The customer can find the resulting booking after response loss. |
| TASK-001 | Retry the same intent | If idempotency is accepted, the retry refers to the original result rather than creating a second booking. |
| TASK-002 | Read booking status | The owning customer can read status; another customer's access is rejected without disclosure. |

## Questions before acceptance

- Who can reserve capacity, and when is a booking binding?
- What constitutes the same intent, and how long can an offline client retry it?
- What happens if a key is reused with a different payload?
- Can a customer cancel, and what refund or cutoff rules apply?
- How should concurrent bookings compete for the same capacity?
- Which client versions must remain compatible, and what workload is expected?

## Candidate failure journey

The server commits the booking, but the response is lost. The mobile client shows
an uncertain outcome rather than claiming failure. After reconnect, it reconciles
the original intent through an agreed retry or lookup mechanism. A test must
observe durable bookings, not merely successful response codes. The chosen
mechanism remains a design decision until the relevant policies are accepted.
