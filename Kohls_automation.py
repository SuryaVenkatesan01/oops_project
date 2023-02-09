import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def login():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get("https://www.kohls.com/")
    driver.find_element(By.XPATH, "//a[@title='Account']").click()
    driver.find_element(By.XPATH, "//input[@id='Profilelogin']").click()
    driver.find_element(By.XPATH, "//input[@name='loginEmail']").send_keys("suryavenkatesan6@gmail.com")
    driver.find_element(By.XPATH, "//input[@name='loginPassword']").send_keys('Surya2001')
    driver.find_element(By.XPATH, "//input[@name='loginEmail']").click()
    time.sleep(5)
    return('Shop by Category')
    element = driver.find_element(By.XPATH, "//span[text()='Shop by Category']")