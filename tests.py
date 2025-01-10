import unittest
from pypasscheck.checker import Checker

special_characters = u'[ !"#$%&\'()*+,-./:;<=>?@[]^_`{|}~]'

print(special_characters)

def generator(special):
    baseline = "abcDE189"
    out = []
    for symbol in special:
        out.append(baseline+symbol)
    return out



class TestPasswordComplexity(unittest.TestCase):
    def test_weak_password(self):
        self.assertFalse(Checker.is_strong("12345678a"))
    def test_strong_password(self):
        self.assertTrue(Checker.is_strong("XWZkaOOl@11{23!kk"))
        for password in generator(special_characters):
            print(password, end=" ")
            try:
                self.assertTrue(Checker.is_strong(password))
                print("STRONG - PASSED")
            except AssertionError:
                print("WEAK - FAILED")
                raise AssertionError




# Run the tests
if __name__ == '__main__':
    unittest.main()