import pytest


@pytest.fixture
def make_password() -> str:
    return 'my_own_password'
