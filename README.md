## What is a strong password? ##
A strong password should be at least eight characters long and include a mix of upper- and lowercase letters, numbers, and special symbols. It is also essential to choose a password that is not easily guessed, such as a name, birth date, or address. A strong password should not be reused on other accounts. - https://iso-docs.com/blogs/iso-27001-isms/password-policy (ISO27001)

### Check if your passwords are strong
```python
from pypasscheck.checker import Checker

password = "SimplePassword"
Checker.is_strong(password)

# Returns False
```

### Get detailed feedback on supplied password
```python
from pypasscheck.checker import Checker

password = "SimplePassword"
Checker.password_assessment(password)

# Returns [<Feedback.NO_DIGITS: 3>, <Feedback.NO_SPECIAL_CHAR: 4>]
```