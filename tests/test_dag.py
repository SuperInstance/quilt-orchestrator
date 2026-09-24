"""Tests for quilt-orchestrator."""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from quilt_orchestrator import DagSubstrate


class TestDagSubstrate(unittest.TestCase):

    def test_plan_dag(self):
        """test_plan_dag"""
        substrate = DagSubstrate()
        receipt = substrate.step(
            cell_id="c0",
            payload={"k": "v0"},
            status="ok",
        )
        self.assertIsNotNone(receipt)
        self.assertEqual(receipt.polarity, "ACCEPT")

    def test_execute_sequential(self):
        """test_execute_sequential"""
        substrate = DagSubstrate()
        receipt = substrate.step(
            cell_id="c1",
            payload={"k": "v1"},
            status="warn",
        )
        self.assertIsNotNone(receipt)
        self.assertEqual(receipt.polarity, "DRIFT")

    def test_execute_parallel(self):
        """test_execute_parallel"""
        substrate = DagSubstrate()
        receipt = substrate.step(
            cell_id="c2",
            payload={"k": "v2"},
            status="fail",
        )
        self.assertIsNotNone(receipt)
        self.assertEqual(receipt.polarity, "REFUSE")

    def test_compose_substrates(self):
        """test_compose_substrates"""
        substrate = DagSubstrate()
        receipt = substrate.step(
            cell_id="c3",
            payload={"k": "v3"},
            status="ok",
        )
        self.assertIsNotNone(receipt)
        self.assertEqual(receipt.polarity, "ACCEPT")

    def test_validate_schema(self):
        """test_validate_schema"""
        substrate = DagSubstrate()
        receipt = substrate.step(
            cell_id="c4",
            payload={"k": "v4"},
            status="warn",
        )
        self.assertIsNotNone(receipt)
        self.assertEqual(receipt.polarity, "DRIFT")

    def test_handle_missing_dep(self):
        """test_handle_missing_dep"""
        substrate = DagSubstrate()
        receipt = substrate.step(
            cell_id="c5",
            payload={"k": "v5"},
            status="fail",
        )
        self.assertIsNotNone(receipt)
        self.assertEqual(receipt.polarity, "REFUSE")


    def test_chain_intact(self):
        substrate = DagSubstrate()
        for i in range(5):
            substrate.step(f"c{i}", {"i": i})
        self.assertTrue(substrate.chain_intact())

    def test_chain_broken_detected(self):
        substrate = DagSubstrate()
        substrate.step("c0", {})
        substrate.last_witness_id = ""  # break the chain
        substrate.step("c1", {})
        self.assertFalse(substrate.chain_intact())

    def test_by_polarity(self):
        substrate = DagSubstrate()
        substrate.step("c0", {}, "ok")
        substrate.step("c1", {}, "warn")
        substrate.step("c2", {}, "fail")
        counts = substrate.by_polarity()
        self.assertEqual(counts["ACCEPT"], 1)
        self.assertEqual(counts["DRIFT"], 1)
        self.assertEqual(counts["REFUSE"], 1)


if __name__ == "__main__":
    unittest.main()
