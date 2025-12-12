import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

def test_open_new_account(driver):
    lp = LoginPage(driver)
    lp.load()
    lp.login("john", "demo")

    hp = HomePage(driver)
    hp.open_new_account_link().click()

    # choose account type and open
    Select(driver.find_element(By.ID, "type")).select_by_visible_text("SAVINGS")
    Select(driver.find_element(By.ID, "fromAccountId")).select_by_index(0)
    driver.find_element(By.CSS_SELECTOR, "input[value='Open New Account']").click()

    # verify account opened
    assert "Account Opened!" in driver.page_source
