from selenium.webdriver.common.by import By

class PimPage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_menu_option_xpath = (By.XPATH, '//a[@href="/web/index.php/pim/viewPimModule"]')
        self.add_button_xpath = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
        self.first_name_locator = (By.NAME, 'firstName')
        self.last_name_locator = (By.NAME, 'lastName')
        self.save_button_xpath = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')

    def navigate_to_pim(self):
        try:
            self.driver.find_element(*self.pim_menu_option_xpath).click()
        except Exception as e:
            print(f"Exception occurred while navigating to PIM: {e}")

    def add_employee(self, first_name, last_name):
        try:
            self.driver.find_element(*self.add_button_xpath).click()
            self.driver.find_element(*self.first_name_locator).send_keys(first_name)
            self.driver.find_element(*self.last_name_locator).send_keys(last_name)
            self.driver.find_element(*self.save_button_xpath).click()
        except Exception as e:
            print(f"Exception occurred while adding an employee: {e}")
