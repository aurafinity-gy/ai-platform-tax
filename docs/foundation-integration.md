# Foundation consumer integration contract (planned)

The Tax domain must consume independently verified published Foundation contracts; it must not import Foundation server internals. The Python `tax_workflow.foundation_ports` package defines local *intent*, not a deployed Foundation API.

## Consumer binding checklist

- Authenticate workload/service principal; establish tenant and originating-actor delegation independently of untrusted headers.
- Select an immutable orchestration release, reviewed agent/tool bindings and bounded execution profile.
- Supply tenant-safe, jurisdiction-aware knowledge queries; preserve official-source citations and effective dates.
- Fail closed on missing or stale evidence, untrusted agent text, use-time revocation and authorization uncertainty.
- Enforce Foundation lifecycle read/use fencing for sensitive documents before knowledge context or external send.
- Keep tool invocations and model calls within the authorized budget; no outbound filing or financial mutations.
- Validate request/response shapes against the exact published versions and immutable release.
- Test negative cases: cross-tenant, revoked actor, invalid effective year, injection, missing citations, duplicate evidence, model timeout, replay and crash recovery.

## Implementation requirement

Before producing a real client adapter, read current Foundation API schemas, service authorization and lifecycle contracts on `main`, capture exact refs and version pins, implement a conformance fake, run cross-repository integration tests and obtain authorized staging acceptance. Absence of those steps means this remains offline-only.
