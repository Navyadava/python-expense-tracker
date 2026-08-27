import unittest

from main import calculate_total
from main import filter_by_category
from main import validate_amount


class TestExpenseTracker(unittest.TestCase):

    def test_calculate_total(self):
        expenses = [
            {
                "Date": "2026-08-27",
                "Category": "Food",
                "Amount": "25.00",
                "Note": "Lunch"
            },
            {
                "Date": "2026-08-27",
                "Category": "Travel",
                "Amount": "40.00",
                "Note": "Uber"
            }
        ]

        result = calculate_total(expenses)

        self.assertEqual(result, 65.00)


    def test_empty_expense_list(self):
        expenses = []

        result = calculate_total(expenses)

        self.assertEqual(result, 0)


    def test_filter_by_category(self):
        expenses = [
            {
                "Date": "2026-08-27",
                "Category": "Food",
                "Amount": "25.00",
                "Note": "Lunch"
            },
            {
                "Date": "2026-08-27",
                "Category": "Travel",
                "Amount": "40.00",
                "Note": "Uber"
            },
            {
                "Date": "2026-08-27",
                "Category": "Food",
                "Amount": "10.00",
                "Note": "Coffee"
            }
        ]

        result = filter_by_category(expenses, "Food")

        self.assertEqual(len(result), 2)


    def test_category_with_no_matches(self):
        expenses = [
            {
                "Date": "2026-08-27",
                "Category": "Food",
                "Amount": "25.00",
                "Note": "Lunch"
            }
        ]

        result = filter_by_category(expenses, "Shopping")

        self.assertEqual(result, [])


    def test_invalid_amount_text(self):
        with self.assertRaises(ValueError):
            validate_amount("abc")


    def test_negative_amount(self):
        with self.assertRaises(ValueError):
            validate_amount("-10")


    def test_zero_amount(self):
        with self.assertRaises(ValueError):
            validate_amount("0")


    def test_valid_amount(self):
        result = validate_amount("25")

        self.assertEqual(result, 25.0)


if __name__ == "__main__":
    unittest.main()