import pytest

from utils.password import generate_hash, check_hash
from utils.password.exceptions import CheckPasswordHashException


def test_generate_hash_and_check_hash(make_password):
    new_hash = generate_hash(make_password)
    check_hash(make_password, new_hash)


def test_check_invalid_hash(make_password):
    invalid_hash = b'1234567_invalid_hash'

    with pytest.raises(CheckPasswordHashException):
        check_hash(make_password, invalid_hash)


def test_generate_hash_exception():
    password_int = 123
    password_none = None

    with pytest.raises(AttributeError):
        generate_hash(password_int)
        generate_hash(password_none)
