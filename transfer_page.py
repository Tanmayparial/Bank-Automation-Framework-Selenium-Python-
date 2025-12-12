from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class TransferPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def from_account_select(self):
        el = self.wait.until(EC.presence_of_element_located((By.ID, "fromAccountId")))
        return Select(el)

    def to_account_select(self):
        el = self.wait.until(EC.presence_of_element_located((By.ID, "toAccountId")))
        return Select(el)

    def amount_input(self):
        return self.driver.find_element(By.ID, "amount")

    def transfer_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[value='Transfer']")

    def transfer_funds(self, from_value, to_value, amount):
        self.from_account_select().select_by_value(str(from_value))
        self.to_account_select().select_by_value(str(to_value))
        self.amount_input().clear()
        self.amount_input().send_keys(str(amount))
        self.transfer_button().click()

    def success_message(self):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#rightPanel .title"))).text
