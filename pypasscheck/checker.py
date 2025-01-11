from enum import Enum
import re

class Checker:
    class Feedback(Enum):
        STRONG_ENOUGH = 1
        TOO_SHORT = 2
        NO_DIGITS = 3
        NO_ALPHAPHABETIC = 4
        NO_SPECIAL_CHAR = 5

    @staticmethod
    def is_long_enough(password: str, expected_len = 8):
        return len(password) >= expected_len
    

    @staticmethod
    def has_digits(password: str):
        return any(c.isdigit() for c in password)
    

    @staticmethod
    def has_alphabetic(password: str):
        return any(c.isalpha() for c in password)


    @staticmethod
    def contains_special_characters(s):
        pattern = r'[ !"#$%&\'()*+,\-./:;<=>?@\[\]^_`{|}~]'
        # Regex to match any non-alphanumeric character
        return bool(re.search(pattern, s))


    @staticmethod
    def is_strong(password: str):
        if Checker.is_long_enough(password) and \
            Checker.has_digits(password) and \
            Checker.has_alphabetic(password) and \
            Checker.contains_special_characters(password):
            return True
        else:
            return False


    @staticmethod
    def password_feedback(password: str):
        if not Checker.is_long_enough(password):
            return Checker.Feedback.TOO_SHORT
        elif not Checker.has_alphabetic(password):
            return Checker.Feedback.NO_ALPHAPHABETIC
        elif not Checker.has_digits(password):
            return Checker.Feedback.NO_DIGITS
        elif not Checker.contains_special_characters(password):
            return Checker.Feedback.NO_SPECIAL_CHAR
        else:
            return Checker.Feedback.STRONG_ENOUGH


    @staticmethod
    def password_assessment(password: str):
        result = []
        if not Checker.is_long_enough(password):
            result.append(Checker.Feedback.TOO_SHORT)

        if not Checker.has_alphabetic(password):
            result.append(Checker.Feedback.NO_ALPHAPHABETIC)

        if not Checker.has_digits(password):
            result.append(Checker.Feedback.NO_DIGITS)

        if not Checker.contains_special_characters(password):
            result.append(Checker.Feedback.NO_SPECIAL_CHAR)

        if Checker.is_strong(password):
            result.append(Checker.Feedback.STRONG_ENOUGH)
        
        return result
