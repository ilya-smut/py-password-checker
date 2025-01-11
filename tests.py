import unittest
from pypasscheck.checker import Checker
from random import Random
import string

special_characters = u'[ !"#$%&\'()*+,-./:;<=>?@[]^_`{|}~]'


def generate_strong_passwords(special):
    baseline = "abcDE189"
    out = []
    for symbol in special:
        out.append(baseline+symbol)
    return out


def generate_weak_password():
    r = Random()
    out = []
    # too short + lowercase only
    out.append(''.join(r.choices(string.ascii_lowercase, k=7)))
    # lowercase only
    out.append(''.join(r.choices(string.ascii_lowercase, k=25)))
    # no spec characters and no digits
    out.append(''.join(r.choices(string.ascii_lowercase + string.ascii_uppercase, k=25)))
    # no spec characters
    out.append(''.join(r.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=25)))
    # no digits
    out.append(''.join(r.choices(string.ascii_lowercase + string.ascii_uppercase + special_characters, k=25)))
    return out


class TestPasswordComplexity(unittest.TestCase):


    def test_weak_password(self):
        for password in generate_weak_password():
            self.assertFalse(Checker.is_strong(password))


    def test_strong_password(self):
        self.assertTrue(Checker.is_strong("XWZkaOOl@11{23!kk"))
        for password in generate_strong_passwords(special_characters):
            self.assertTrue(Checker.is_strong(password))
            

    def test_password_feedback(self):
        too_short = "Aa1@"
        no_alphabetic = "12345678@!"
        no_digits = "abcdefghij@"
        no_spec_char = "ABCdefGHI12345678"
        good_enough = "IUsa89@!iiiooo.com"
        self.assertEqual(Checker.password_feedback(too_short), Checker.Feedback.TOO_SHORT)
        self.assertEqual(Checker.password_feedback(no_alphabetic), Checker.Feedback.NO_ALPHAPHABETIC)
        self.assertEqual(Checker.password_feedback(no_digits), Checker.Feedback.NO_DIGITS)
        self.assertEqual(Checker.password_feedback(no_spec_char), Checker.Feedback.NO_SPECIAL_CHAR)
        self.assertEqual(Checker.password_feedback(good_enough), Checker.Feedback.STRONG_ENOUGH)

    
    def test_password_assessment(self):
        psw = "123"
        result = Checker.password_assessment(psw)
        self.assertEqual(set(result), {Checker.Feedback.TOO_SHORT, Checker.Feedback.NO_ALPHAPHABETIC, Checker.Feedback.NO_SPECIAL_CHAR})
        




# Run the tests
if __name__ == '__main__':
    unittest.main()