import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",'..'))
from POMDemo.Pages.loginPage import LoginPage
from POMDemo.Pages.homePage import HomePage
import HtmlTestRunner

class LoginTests(unittest.TestCase):

   # driver = webdriver.Chrome(ChromeDriverManager().install())

    @classmethod
    def setUpClass(cls):
        options = Options()
        # options.add_argument("start-maximized")
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        # driver = webdriver.Chrome('/Users/lulal/PycharmProjects/Selenium/driver/chromedriver.exe')
        cls.driver.implicitly_wait(10)

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        # self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        # self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        # self.driver.find_element(By.ID, "btnLogin").click()
        # self.driver.find_element(By.ID, "welcome").click()
        # self.driver.find_element(By.LINK_TEXT, "Logout").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/lulal/PycharmProjects/Selenium/reports'))