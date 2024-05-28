from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = (By.NAME, 'username')
        self.password_locator = (By.NAME, 'password')
        self.submit_button_locator = (By.XPATH, '//button[@type="submit"]')

    def login(self, username, password):
        try:
            self.driver.find_element(*self.username_locator).send_keys(username)
            self.driver.find_element(*self.password_locator).send_keys(password)
            self.driver.find_element(*self.submit_button_locator).click()
        except Exception as e:
            print(f"Exception occurred during login: {e}")
