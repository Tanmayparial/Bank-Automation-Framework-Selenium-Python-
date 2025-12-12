import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.transfer_page import TransferPage

def test_transfer_funds(driver):
    lp = LoginPage(driver)
    lp.load()
    lp.login("john", "demo")

    hp = HomePage(driver)
    hp.transfer_funds_link().click()

    tp = TransferPage(driver)
    # Note: demo site account values vary — using indices/values that exist on the demo account might be needed.
    # You can also read account ids from Accounts Overview and pass into transfer_funds.
    # Try with the first available account values: use visible texts/values as seen on the site.
    # Example uses placeholder values; adjust if transfer fails due to account mismatches.
    try:
        # attempt transfer with sample values
        tp.transfer_funds(from_value=12345, to_value=54321, amount=100)
    except Exception:
        # fallback: select first option in dropdowns and transfer
        from_select = tp.from_account_select()
        to_select = tp.to_account_select()
        from_val = from_select.options[0].get_attribute("value")
        to_val = to_select.options[0].get_attribute("value")
        tp.transfer_funds(from_val, to_val, 10)

    assert "Transfer Complete!" in tp.success_message()
