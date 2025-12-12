from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def update_contact_link(self):
        return self.driver.find_element(By.LINK_TEXT, "Update Contact Info")

    def address_field(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, "customer.address.street")))

    def city_field(self):
        return self.driver.find_element(By.ID, "customer.address.city")

    def state_field(self):
        return self.driver.find_element(By.ID, "customer.address.state")

    def zip_field(self):
        return self.driver.find_element(By.ID, "customer.address.zipCode")

    def phone_field(self):
        return self.driver.find_element(By.ID, "customer.phoneNumber")

    def update_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[value='Update Profile']")

    def update_contact(self, address, city, state, zipc, phone):
        self.address_field().clear()
        self.address_field().send_keys(address)
        self.city_field().clear()
        self.city_field().send_keys(city)
        self.state_field().clear()
        self.state_field().send_keys(state)
        self.zip_field().clear()
        self.zip_field().send_keys(zipc)
        self.phone_field().clear()
        self.phone_field().send_keys(phone)
        self.update_button().click()

    def success_message(self):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#rightPanel .title"))).text
