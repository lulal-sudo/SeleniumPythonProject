from selenium.webdriver.common.by import By
from POMDemo.Locators.locators import Locators

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = "txtPassword"
        self.login_button_id = "btnLogin"

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_textbox_id).clear()
        self.driver.find_element(By.ID, self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, Locators.password_textbox_id).clear()
        self.driver.find_element(By.ID, Locators.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.login_button_id).click()
