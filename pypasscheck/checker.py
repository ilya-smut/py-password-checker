import re

def contains_special_characters(s):
    # Regex to match any non-alphanumeric character
    return bool(re.search(r"[^a-zA-Z0-9]", s))

class Checker:
    def is_strong(password: str):
        if len(password) >= 8 and \
            any(c.isdigit() for c in password) and \
            any(c.isalpha() for c in password) and \
            contains_special_characters(password):
                return True
        else:
            return False

