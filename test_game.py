import unittest
from game import sort_test_choice, find_detail_attribute

class TestGame(unittest.TestCase):
    def test_sort_test_choice(self):
        self.assertEqual(sort_test_choice("123", "0123456789"), "123")
        self.assertEqual(sort_test_choice("546", "0123456789"), "456")
        self.assertEqual(sort_test_choice("7879", "0123456789"), "789")
    
    def test_find_detail_attribute(self):
        self.assertEqual(find_detail_attribute("detail", "type"), None)
        self.assertEqual(find_detail_attribute("topic", "attribute"), None)
        self.assertEqual(find_detail_attribute("topic", "type"), "choice")

if __name__ == "__main__":
    unittest.main()
