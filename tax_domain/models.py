"""Synthetic-ready tax domain contracts; no taxpayer identifiers or provider SDKs."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Final


class SubjectKind(str, Enum):
    INDIVIDUAL = "individual"
    CORPORATION = "corporation"


class AgentRole(str, Enum):
    INTAKE = "intake"
    DOCUMENT = "document"
    RESEARCH = "research"
    PREPARATION = "preparation"
    CALCULATION = "calculation"
    VERIFICATION = "verification"
    ADVISORY = "advisory"


ORDERED_ROLES: Final[tuple[AgentRole, ...]] = tuple(AgentRole)


@dataclass(frozen=True, slots=True)
class TaxCase:
    case_id: str
    tenant_id: str
    subject_id: str
    subject_kind: SubjectKind
    tax_year: int
    jurisdiction: str

    def __post_init__(self) -> None:
        if not all((self.case_id, self.tenant_id, self.subject_id, self.jurisdiction)):
            raise ValueError("Case identity and jurisdiction are required")
        if not 1900 <= self.tax_year <= 2200:
            raise ValueError("Invalid taxation year")


@dataclass(frozen=True, slots=True)
class SourceEvidence:
    source_id: str
    authority: str
    citation: str
    effective_year: int
    enacted: bool
    independently_verified: bool

    def __post_init__(self) -> None:
        if not all((self.source_id, self.authority, self.citation)):
            raise ValueError("Evidence requires provenance")


@dataclass(frozen=True, slots=True)
class AgentFinding:
    role: AgentRole
    statement: str
    source_ids: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.statement.strip():
            raise ValueError("Findings must include a statement")
