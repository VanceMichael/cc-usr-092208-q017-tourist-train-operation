import unittest
from pathlib import Path
from src.domain import load_domain

class DomainTest(unittest.TestCase):
    def test_fixture_matches_domain(self):
        value = load_domain(Path("fixtures/domain.json"))
        self.assertEqual(value["domain"], "tourist-train-operation")
        self.assertGreaterEqual(len(value["constraints"]), 2)

    def test_fixture_covers_collaboration_rules(self):
        value = load_domain(Path("fixtures/domain.json"))
        self.assertGreaterEqual(value["version"], 2)
        self.assertIn("铁路调度人员", value["actors"])
        self.assertIn("平台客服人员", value["actors"])
        self.assertTrue(any("旅游专列" in fact and "旅游专线" in fact for fact in value["facts"]))
        for rule in ("受影响段局部调整", "旅客同步通知", "方案版本溯源", "开行后兑现核对"):
            self.assertIn(rule, value["constraints"])

if __name__ == "__main__":
    unittest.main()
