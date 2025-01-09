import unittest
from pypasscheck.checker import Checker

class TestPasswordComplexity(unittest.TestCase):
    def test_weak_password(self):
        self.assertFalse(Checker.is_strong("12345678a"))
    def test_strong_password(self):
        self.assertTrue(Checker.is_strong("XWZkaOOl@11{23!kk"))


# Run the tests
if __name__ == '__main__':
    unittest.main()