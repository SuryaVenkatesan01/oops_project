import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestKohlsLoginPage:
    @pytest.fixture
    def driver(self, request):
        driver = webdriver.Edge()
        driver.get("https://www.kohls.com/")
        driver.maximize_window()
        driver.implicitly_wait(30)
        request.addfinalizer(driver.quit)
        return driver

    def test_login(self, driver):
        driver.find_element(By.XPATH, "//a[@title='Account']").click()
        driver.find_element(By.XPATH, "//input[@id='Profilelogin']").click()
        driver.find_element(By.XPATH, "//input[@name='loginEmail']").send_keys("suryavenkatesan6@gmail.com")
        driver.find_element(By.XPATH, "//input[@name='loginPassword']").send_keys('Surya2001')
        driver.find_element(By.XPATH, "//input[@name='loginEmail']").click()
        expected_header = 'Shop by Category'
        element = driver.find_element(By.XPATH, "//span[text()='Shop by Category']")
        assert expected_header in element.text
