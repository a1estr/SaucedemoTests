from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container")
    ERROR_BUTTON_INPUT_USERNAME = (By.XPATH, '//*[@id="login_button_container"]/div/form/div[1]/svg')

    def enter_username(self, username):
        self.enter_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)

    def find_error_button(self):
        return self.find_element(self.ERROR_BUTTON_INPUT_USERNAME).text

    def get_error_message(self):
        return self.find_element(self.ERROR_MESSAGE).text

    def get_login_page(self):
        return self.open_url("https://www.saucedemo.com/")

    def valid_login(self):
        self.get_login_page()
        self.enter_username("standard_user")
        self.enter_password("secret_sauce")
        self.click_login()