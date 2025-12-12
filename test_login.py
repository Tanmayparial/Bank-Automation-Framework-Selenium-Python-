import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

def test_valid_login(driver):
    lp = LoginPage(driver)
    lp.load()
    lp.login("john", "demo")
    # verify landing page mentions "Accounts Overview" or similar
    assert "Accounts Overview" in driver.page_source

def test_invalid_login(driver):
    lp = LoginPage(driver)
    lp.load()
    lp.login("invaliduser", "badpass")
    assert "The username and password could not be verified." in lp.get_error()
