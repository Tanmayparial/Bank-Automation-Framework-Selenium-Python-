import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.profile_page import ProfilePage
from selenium.webdriver.common.by import By

def test_update_profile(driver):
    lp = LoginPage(driver)
    lp.load()
    lp.login("john", "demo")

    hp = HomePage(driver)
    # open update contact link
    driver.find_element(By.LINK_TEXT, "Update Contact Info").click()

    pp = ProfilePage(driver)
    # fill sample data
    pp.update_contact("221B Baker Street", "London", "Greater London", "NW1 6XE", "+91-9999999999")
    assert "Profile Updated" in driver.page_source or "Personal Details Updated" in pp.success_message()
