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
    # only lowercase + spec chars + digits
    out.append(''.join(r.choices(string.ascii_lowercase + string.digits + special_characters, k=25)))
    # only uppercase + spec chars + digits
    out.append(''.join(r.choices(string.ascii_uppercase + string.digits + special_characters, k=25)))
    return out


class TestPasswordComplexity(unittest.TestCase):


    def test_weak_password(self):
        for password in generate_weak_password():
            self.assertFalse(Checker.is_strong(password))


    def test_strong_password(self):
        self.assertTrue(Checker.is_strong("XWZkaOOl@11{23!kk"))
        for password in generate_strong_passwords(special_characters):
            self.assertTrue(Checker.is_strong(password))

    
    def test_password_assessment(self):
        digits_short = "123"
        lower_short = "abc"
        digits_lower_short = "123abc"
        digits_lower_upper_short = "123abcD"
        digits_lower_upper_spec_short = "123abD@"
        digits_lower_upper_spec_long = "123abD@!!"
        self.assertEqual(set(Checker.password_assessment(digits_short)), {Checker.Feedback.TOO_SHORT, 
                                                                          Checker.Feedback.NO_UPPERCASE, 
                                                                          Checker.Feedback.NO_LOWERCASE, 
                                                                          Checker.Feedback.NO_SPECIAL_CHAR})
        
        self.assertEqual(set(Checker.password_assessment(lower_short)), {Checker.Feedback.TOO_SHORT, 
                                                                         Checker.Feedback.NO_DIGITS,
                                                                         Checker.Feedback.NO_UPPERCASE, 
                                                                         Checker.Feedback.NO_SPECIAL_CHAR})

        self.assertEqual(set(Checker.password_assessment(digits_lower_short)), {Checker.Feedback.TOO_SHORT, 
                                                                                Checker.Feedback.NO_UPPERCASE, 
                                                                                Checker.Feedback.NO_SPECIAL_CHAR})
        
        self.assertEqual(set(Checker.password_assessment(digits_lower_upper_short)), {Checker.Feedback.TOO_SHORT,  
                                                                                      Checker.Feedback.NO_SPECIAL_CHAR})
        
        self.assertEqual(set(Checker.password_assessment(digits_lower_upper_spec_short)), {Checker.Feedback.TOO_SHORT})

        self.assertEqual(set(Checker.password_assessment(digits_lower_upper_spec_long)), {Checker.Feedback.STRONG_ENOUGH})


# Run the tests
if __name__ == '__main__':
    unittest.main()