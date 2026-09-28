import pytest

# Yield fixture: runs setup before and teardown after
@pytest.fixture
def setup_teardown():
    print("[setup]")
    yield
    print("[teardown]")

# First test: multiplication
def test_multiplication(setup_teardown):
    print("Running multiplication test")
    assert 6 * 7 == 42

# Second test: string uppercase
def test_string_upper(setup_teardown):
    print("Running string test")
    assert "omg".upper() == "OMG"
