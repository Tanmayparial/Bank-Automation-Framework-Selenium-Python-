from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def welcome_message(self):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1"))).text

    def open_new_account_link(self):
        return self.driver.find_element(By.LINK_TEXT, "Open New Account")

    def accounts_overview_link(self):
        return self.driver.find_element(By.LINK_TEXT, "Accounts Overview")

    def transfer_funds_link(self):
        return self.driver.find_element(By.LINK_TEXT, "Transfer Funds")

    def logout_link(self):
        return self.driver.find_element(By.LINK_TEXT, "Log Out")
