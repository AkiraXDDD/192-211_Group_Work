import pytest
from conftest import funded_account

def test_deposit_increases_balance(funded_account):
    result = funded_account.deposit(500)
    assert result == 1500
    assert funded_account.balance == 1500  # deposit test


def test_withdraw_decreases_balance(funded_account):
    result = funded_account.withdraw(300)
    assert result == 700
    assert funded_account.balance == 700  # withdraw test


def test_withdraw_insufficient_funds_raises(funded_account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        funded_account.withdraw(1001)
    assert funded_account.balance == 1000  # balance unchanged after failure