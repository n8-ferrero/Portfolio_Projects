"""
Strong password generation utility
"""
import string
from random import choice, randint


def generate_random_password(_min: int = 12, _max: int = 16) -> str:
    """
    Generate random password
    _min : int : minimum length
    _max : int : maximum length
    return : str
    """
    _c = string.ascii_letters
    _d = string.digits
    _p = "!@#$^*"  # string.punctuation
    characters = _c + _p + _d
    _l = randint(_min, _max)

    return "".join(choice(characters) for x in range(_l))


print(f"Here is your new password: {generate_random_password()}")
