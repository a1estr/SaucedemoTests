from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    CART_CONTAINER = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')

    def add_to_cart(self, item_name):
        if "test" not in item_name:
            self.click_element((By.ID, f"add-to-cart-sauce-labs-{item_name}"))
        else:
            self.click_element((By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)"))

    def items_in_cart_count(self):
        return self.find_element(self.CART_BADGE).text

    def open_cart(self):
        self.click_element(self.CART_CONTAINER)
