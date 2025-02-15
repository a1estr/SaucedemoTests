from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    ITEM_NAME_IN_CART = (By.CLASS_NAME, "inventory_item_name")
    CART_BADGE = (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')

    def get_item_name_in_cart(self):
        return self.find_element(self.ITEM_NAME_IN_CART).text

    def items_in_cart_count(self):
        return self.find_element(self.CART_BADGE).text