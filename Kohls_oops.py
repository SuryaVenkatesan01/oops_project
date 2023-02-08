import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class KohlsLoginPage:
    def __init__(self):
        self.driver = webdriver.Edge()
        self.driver.get("https://www.kohls.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def login(self):
        self.driver.find_element(By.XPATH, "//a[@title='Account']").click()
        self.driver.find_element(By.XPATH, "//input[@id='Profilelogin']").click()
        self.driver.find_element(By.XPATH, "//input[@name='loginEmail']").send_keys("suryavenkatesan6@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@name='loginPassword']").send_keys('Surya2001')
        self.driver.find_element(By.XPATH, "//input[@name='loginEmail']").click()


class ShopByCategoryPage(KohlsLoginPage):

    def select_boots_category(self):
        self.driver.find_element(By.XPATH, "//span[text()='Shop by Category']").click()
        self.driver.find_element(By.XPATH, "(//a[@class='navigation-item-link'])[10]").click()
        time.sleep(5)

    def exception1(self):
        try:
            self.driver.find_element(By.XPATH, "//span[text()='Shop by Categor']").click()
        except:
            print("Invalid Xpath")


# Menu
obj = ShopByCategoryPage()

while True:
    print("Enter 1 login")
    print("Enter 2 for select items only after logging in")
    print("Enter 3 for exception")
    print("Enter 4 for exit code")
    userchoice = int(input())
    if userchoice == 1:
        obj.login()
    elif userchoice == 2:
        obj.select_boots_category()
    elif userchoice == 3:
        obj.exception1()
    elif userchoice == 4:
        quit()
