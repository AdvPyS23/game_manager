import unittest
import game
from game import sort_test_choice, find_detail_attribute

class TestGame(unittest.TestCase):
    def test_sort_test_choice(self):
        # Test edge cases, i.e. that first and last values are considere
        self.assertEqual(sort_test_choice("0123", "0123"), "0123")
        # Test sorting
        self.assertEqual(sort_test_choice("546", "0123456789"), "456")
        # Test empty input
        self.assertEqual(sort_test_choice("", "0123456789"), "")
        # Test multiple occurences
        self.assertEqual(sort_test_choice("7879", "0123456789"), "789")
        # Test for wrong input (not all digits in allowed values)
        self.assertEqual(sort_test_choice("125", "0123"), "NOT VALID")

    def test_find_detail_attribute(self):
        # Test wrong attribute value
        self.assertRaises(KeyError, find_detail_attribute, "topic", "wrong_attr")
        # Test wrong detail value
        self.assertRaises(KeyError, find_detail_attribute, "wrong_detail", "type")
        # Test for both correct values (att = "type")
        self.assertEqual(find_detail_attribute("topic", "type"), "choice")
        # Test for both correct values (att = "string")
        self.assertEqual(find_detail_attribute("min_age", "string"), "minimum age (years)")
        # Test for aboth correct values (att = "allowed_values")
        self.assertEqual(find_detail_attribute("topic", "allowed_values"), game.TOPICS)
        # Test for aboth correct values (att = "allowed_values", different type of detail)
        self.assertEqual(find_detail_attribute("complexity", "allowed_values"), ["1 - 10"])
        # Test for aboth correct values (att = "allowed_values", third type of detail)
        self.assertEqual(find_detail_attribute("min_age", "allowed_values"), [">=1"])

if __name__ == "__main__":
    unittest.main()
