# Tax domain architecture (bootstrap)

## Purpose
Build a Canadian personal and corporate tax assistant via **domain-owned specialized agents** under Foundation orchestration. This bootstrap deliberately avoids fabricating live Foundation connectivity or CRA authorization.

## Ownership and data flow

```text
Tax web/BFF (future)
  -> Tax API + tenant/actor authorization (future)
  -> Tax case/workflow domain
     -> intake -> document evidence -> research -> preparation
     -> deterministic calculation -> verification -> advisory
     -> explicit accountant/client approval (future)
  -> Foundation published versioned services:
       orchestration/checkpoints, knowledge context/citations,
       model gateway, tool runtime, durable audit and data lifecycle
```

Tax application controls which agents can access which legal subjects, records, tools and rules. Neither model text nor a peer-agent response grants authority. Foundation authenticates service workload and executes only approved capabilities.

## First local vertical slice

The first Python package contains strict value objects, named workflow stages, a fail-closed deterministic offline orchestrator, and injectable ports for knowledge and calculation. It uses synthetic cases and never calls providers. It is **not** a running seven-LLM-agent system: role definitions are intended for a later Foundation-orchestrated workflow after published-contract conformance.

## Agent roles

- Intake: identify legal subject, jurisdiction, taxation year, missing prerequisites.
- Document: normalize source evidence, never invent tax slip fields.
- Research: return versioned legal-source references, dates and status.
- Preparation: construct tax facts and identify missing material evidence.
- Calculation: invoke audited, deterministic, jurisdiction- and tax-year-specific functions.
- Verification: reconcile totals, evidence references, rule versions and unresolved assumptions.
- Advisory: prepare explanations/scenarios, never authorize filing.

## Tax-owned modules

`tax_domain`: legal-subject/case and agent data contracts; no adapters.
`tax_workflow`: orchestration-facing domain service and provider-neutral ports.
Future modules: T1, T2, GST/HST, payroll, document parsers, verified rule catalogs, approvals and filings.

## Trust and financial safety

Require versioned rule definitions with official law citations, enactment status, valid dates, jurisdiction, independent verification, and a bounded effective period. Retain uncertainty on contested tax interpretation. A return with missing evidence or unresolved calculations is not approvable. Model responses are advisory drafts only.

This public repository may only contain synthetic fixtures and non-secret configuration. Taxpayer records, account tokens, scans and identifiable tax documents are prohibited from source control.

## Integration gates

Do not wire real Foundation calls until interface signatures, workload authentication, tenant scoping, query privileges, use-time derivative authority, replay behavior, provider admission, and cost boundaries have been proven with current Foundation contracts in integration/staging. Do not assume that a draft or merged PR has activated a capability.
