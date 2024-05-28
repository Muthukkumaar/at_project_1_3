import pytest

@pytest.fixture(scope="session")
def setup():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
