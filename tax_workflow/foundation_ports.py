"""Tax-owned contracts for later integration with authenticated Foundation services.

These are consumer ports, NOT implementations or claims about current Foundation wire schemas.
Adapters must map to verified public Foundation contract versions.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from tax_domain.models import TaxCase


@dataclass(frozen=True, slots=True)
class ExecutionIdentity:
    tenant_id: str
    actor_id: str
    authorization_reference: str

    def __post_init__(self) -> None:
        if not all((self.tenant_id, self.actor_id, self.authorization_reference)):
            raise ValueError("Explicit authorization context is required")


@dataclass(frozen=True, slots=True)
class FoundationKnowledgeRequest:
    case_id: str
    tenant_id: str
    jurisdiction: str
    tax_year: int
    question: str


@dataclass(frozen=True, slots=True)
class CitedContext:
    source_references: tuple[str, ...]
    text: str
    contract_version: str


class FoundationKnowledgePort(Protocol):
    def retrieve(
        self, request: FoundationKnowledgeRequest, identity: ExecutionIdentity
    ) -> CitedContext: ...


class FoundationOrchestrationPort(Protocol):
    def submit_case(
        self, case: TaxCase, identity: ExecutionIdentity, release_reference: str
    ) -> str: ...


class FoundationUseAuthorityPort(Protocol):
    def assert_current_use(
        self, identity: ExecutionIdentity, source_references: tuple[str, ...]
    ) -> None: ...
