from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutCustomerPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    SUBMIT = (By.ID, "continue")

    def enter_first_name(self, first_name):
        self.enter_text(self.FIRST_NAME, first_name)

    def enter_last_name(self, last_name):
        self.enter_text(self.LAST_NAME, last_name)

    def enter_postal_code(self, postal_code):
        self.enter_text(self.POSTAL_CODE, postal_code)

    def submit_info(self):
        self.click_element(self.SUBMIT)

    def enter_valid_customer_info(self, first_name, last_name, postal_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
