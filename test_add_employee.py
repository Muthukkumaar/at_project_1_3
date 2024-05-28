import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.pim_page import PimPage

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_add_employee(setup):
    driver = setup
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    login_page = LoginPage(driver)
    pim_page = PimPage(driver)
    
    login_page.login("Admin", "admin123")
    pim_page.navigate_to_pim()
    pim_page.add_employee("MahendraSingh", "Dhoni")

    # Add assertions as necessary, for example:
    # assert "Employee Information" in driver.page_source
