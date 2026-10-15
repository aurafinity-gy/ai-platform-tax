# Proposed delivery sequence

These labels are descriptive **planning** names; no canonical tracked ID is allocated without the Handbook registry.

| Phase | Deliverable | Gate |
| --- | --- | --- |
| Tax architecture | domain identity, legal-subject delegation, data/privacy model, baseline contracts | ADR + review |
| Offline workflow | synthetic intake, specialized roles, fail-closed verifier | unit/negative tests |
| Canadian rule catalog | authoritative federal/provincial source snapshots, effective dates, statuses | independent legal review |
| Deterministic T1/T2 | tax-year-specific validated calculations (no guessed rates) | golden scenarios and professional review |
| Evidence/document ingestion | generic Foundation document-intelligence + Tax schemas | source/field proof |
| Foundation consumer integration | authenticated retrieval, orchestration and governed tools | contract/RLS/staging conformance |
| Accountant review | immutable snapshot-bound decision with authorized approver | revocation/change negative tests |
| GST/HST, payroll | domain calculators and deadlines | tax-year/jurisdiction acceptance |
| Filing | approved CRA-compatible adapter | vendor/certification/authorization, human sign-off |

## Current limitations

This bootstrap does not include a deployed API, database schema, real Foundation client, real LLM agents, tax rates or CRA integrations. It is a safe baseline, not a finished tax accountant. Keep production and sensitive-data processing disabled.
