import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.account_page import AccountPage

def test_transactions_table(driver):
    lp = LoginPage(driver)
    lp.load()
    lp.login("john", "demo")

    hp = HomePage(driver)
    hp.accounts_overview_link().click()

    ap = AccountPage(driver)
    rows = ap.accounts_table_rows()
    assert len(rows) > 0
