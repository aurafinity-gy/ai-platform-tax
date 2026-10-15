"""Fail-closed synthetic offline workflow; intentionally no models or providers."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Protocol

from tax_domain.models import AgentFinding, AgentRole, SourceEvidence, TaxCase


class TaxRuleEvidencePort(Protocol):
    def lookup(self, case: TaxCase) -> tuple[SourceEvidence, ...]: ...


class Outcome(str, Enum):
    NEEDS_REVIEW = "needs_review"
    BLOCKED = "blocked"


@dataclass(frozen=True, slots=True)
class ReviewPackage:
    case: TaxCase
    findings: tuple[AgentFinding, ...]
    sources: tuple[SourceEvidence, ...]
    outcome: Outcome
    blockers: tuple[str, ...]


class OfflineTaxWorkflow:
    """Not authorized to calculate or file returns; supports safe intake/research."""

    def __init__(self, rules: TaxRuleEvidencePort) -> None:
        self._rules = rules

    def prepare(self, case: TaxCase) -> ReviewPackage:
        sources = self._rules.lookup(case)
        source_ids = {source.source_id for source in sources}
        blockers: list[str] = []
        if not sources:
            blockers.append("No independently checked legislation or guidance supplied")
        if len(source_ids) != len(sources):
            blockers.append("Duplicate source identifiers")
        for source in sources:
            if source.effective_year != case.tax_year:
                blockers.append(f"Source {source.source_id} is for another tax year")
            if not (source.enacted and source.independently_verified):
                blockers.append(f"Source {source.source_id} is not verified enacted authority")

        findings = (
            AgentFinding(AgentRole.INTAKE, "Tax case identity and year captured", ()),
            AgentFinding(
                AgentRole.RESEARCH,
                "Only source provenance is collected; no tax interpretation asserted",
                tuple(sorted(source_ids)),
            ),
            AgentFinding(
                AgentRole.VERIFICATION,
                "Deterministic calculations and authorized human review remain required",
                tuple(sorted(source_ids)),
            ),
        )
        blockers.append("No verified tax-year calculation or accountant approval")
        return ReviewPackage(
            case=case,
            findings=findings,
            sources=sources,
            outcome=Outcome.BLOCKED,
            blockers=tuple(blockers),
        )
