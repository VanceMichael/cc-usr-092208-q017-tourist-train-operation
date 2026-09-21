import unittest
from pathlib import Path
from src.domain import load_domain

class DomainTest(unittest.TestCase):
    def test_fixture_matches_domain(self):
        value = load_domain(Path("fixtures/domain.json"))
        self.assertEqual(value["domain"], "tourist-train-operation")
        self.assertGreaterEqual(len(value["constraints"]), 2)

    def test_fixture_keeps_train_categories(self):
        value = load_domain(Path("fixtures/domain.json"))
        facts = "".join(value["facts"])
        self.assertIn("旅游专列", facts)
        self.assertIn("旅游专线", facts)

    def test_fixture_covers_segment_adjustment_and_traceability(self):
        value = load_domain(Path("fixtures/domain.json"))
        facts = "".join(value["facts"])
        self.assertIn("受影响段", facts)
        self.assertIn("方案版本", facts)
        self.assertIn("受影响段局部调整", value["constraints"])
        self.assertIn("方案版本与责任来源可追溯", value["constraints"])

if __name__ == "__main__":
    unittest.main()
