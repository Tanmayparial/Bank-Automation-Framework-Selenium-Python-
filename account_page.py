from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AccountPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def accounts_table_rows(self):
        return self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#accountTable tbody tr")))

    def open_account(self, account_id):
        rows = self.accounts_table_rows()
        for r in rows:
            link = r.find_element(By.TAG_NAME, "a")
            if link.text.strip() == str(account_id):
                link.click()
                return True
        return False

    def transactions_table(self):
        return self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#transactionTable tbody tr")))
