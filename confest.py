import pytest
from bank import BankAccount

@pytest.fixture
def funded_account():
    return BankAccount(balance=1000)

def test_balance(funded_account):
    assert funded_account.balance == 1000