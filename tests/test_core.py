import unittest
 
from analyser.core import generate_report, generate_summary
 
ROWS = [
    ["Train ticket", "40.00", "travel"],
    ["Laptop stand", "25.50", "equipment"],
    ["Coffee", "3.20", "travel"],
    ["Broken row", "12.00"],
    ["Bad amount", "not-a-number", "travel"],
    ["Refund", "-5.00", "travel"],
]
 
 
class TestReport(unittest.TestCase):
 
    def test_report_lists_valid_rows_only(self):
        output = generate_report(ROWS, include_tax=False)
        self.assertIn("Train ticket: 40.0", output)
        self.assertNotIn("Broken row", output)
        self.assertNotIn("Bad amount", output)
        self.assertNotIn("Refund", output)
 
    def test_report_totals_without_tax(self):
        output = generate_report(ROWS, include_tax=False)
        self.assertIn("TOTAL: 68.7", output)
 
    def test_report_applies_tax(self):
        output = generate_report(ROWS, include_tax=True)
        self.assertIn("TOTAL: 82.44", output)
 
    def test_report_filters_by_category(self):
        output = generate_report(ROWS, category="travel", include_tax=False)
        self.assertIn("Train ticket", output)
        self.assertNotIn("Laptop stand", output)
 
    def test_summary_counts_and_totals(self):
        self.assertEqual(generate_summary(ROWS, include_tax=False), "3 items, total 68.7")
 
    def test_summary_respects_category(self):
        self.assertEqual(
            generate_summary(ROWS, category="equipment", include_tax=False),
            "1 items, total 25.5",
        )
 
 
if __name__ == "__main__":
    unittest.main()
