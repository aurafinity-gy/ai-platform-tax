import unittest

from tax_domain.models import AgentRole, SourceEvidence, SubjectKind, TaxCase
from tax_workflow.offline import OfflineTaxWorkflow, Outcome


class FixedRules:
    def __init__(self, sources=()):
        self.sources = sources

    def lookup(self, case):
        return self.sources


class OfflineWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.case = TaxCase(
            case_id="synthetic-case",
            tenant_id="synthetic-tenant",
            subject_id="synthetic-subject",
            subject_kind=SubjectKind.CORPORATION,
            tax_year=2025,
            jurisdiction="CA-AB",
        )

    def test_missing_sources_fail_closed(self):
        result = OfflineTaxWorkflow(FixedRules()).prepare(self.case)
        self.assertEqual(result.outcome, Outcome.BLOCKED)
        self.assertTrue(any("No independently" in x for x in result.blockers))

    def test_verified_source_still_requires_calculation_and_review(self):
        e = SourceEvidence("source-test", "synthetic authority", "fixture", 2025, True, True)
        result = OfflineTaxWorkflow(FixedRules((e,))).prepare(self.case)
        self.assertEqual(result.outcome, Outcome.BLOCKED)
        self.assertEqual(result.findings[-1].role, AgentRole.VERIFICATION)
        self.assertEqual(result.findings[1].source_ids, ("source-test",))

    def test_unverified_and_wrong_year_sources_fail(self):
        e = SourceEvidence("source-test", "synthetic", "fixture", 2024, False, False)
        result = OfflineTaxWorkflow(FixedRules((e,))).prepare(self.case)
        self.assertTrue(any("another tax year" in x for x in result.blockers))
        self.assertTrue(any("not verified" in x for x in result.blockers))

    def test_duplicate_source_identity_fails(self):
        e = SourceEvidence("same", "synthetic", "fixture", 2025, True, True)
        result = OfflineTaxWorkflow(FixedRules((e, e))).prepare(self.case)
        self.assertIn("Duplicate source identifiers", result.blockers)

    def test_missing_tenant_is_invalid(self):
        with self.assertRaises(ValueError):
            TaxCase("case", "", "subject", SubjectKind.INDIVIDUAL, 2025, "CA-ON")


if __name__ == "__main__":
    unittest.main()
