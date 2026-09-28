import pytest
from bank import BankAccount

@pytest.fixture
def account():
    return BankAccount(balance=100)

def test_deposit50(account):
    account.deposit(50)
    assert account.balance == 150

def test_deposit100(account):
    account.deposit(100)
    assert account.balance == 150