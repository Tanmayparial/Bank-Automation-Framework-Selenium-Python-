from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://parabank.parasoft.com/parabank/index.htm"

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def load(self):
        self.driver.get(self.URL)

    def username_input(self):
        return self.wait.until(EC.presence_of_element_located((By.NAME, "username")))

    def password_input(self):
        return self.wait.until(EC.presence_of_element_located((By.NAME, "password")))

    def login_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[value='Log In']")

    def login(self, username, password):
        self.username_input().clear()
        self.username_input().send_keys(username)
        self.password_input().clear()
        self.password_input().send_keys(password)
        self.login_button().click()

    def get_error(self):
        try:
            return self.driver.find_element(By.CSS_SELECTOR, "#rightPanel .error").text
        except:
            return ""
