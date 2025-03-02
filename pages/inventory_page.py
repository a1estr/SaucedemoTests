from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage


class InventoryPage(BasePage):
    CART_CONTAINER = (By.CLASS_NAME, "shopping_cart_link")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name ")
    CART_BADGE = (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")
    SIDEBAR_MENU = (By.CLASS_NAME, "bm-menu")
    ITEMS_LIST = ["Sauce Labs Backpack",
                  "Sauce Labs Bike Light",
                  "Sauce Labs Bolt T-Shirt",
                  "Sauce Labs Fleece Jacket",
                  "Sauce Labs Onesie",
                  "Test.allTheThings() T-Shirt (Red)"
                  ]
    DROPDOWN_SORT = (By.CLASS_NAME, "product_sort_container")
    PRICE = (By.CLASS_NAME, "inventory_item_price")
    PRICES_LIST = [29.99, 9.99, 15.99, 49.99, 7.99, 15.99]

    def add_to_cart(self, item_name):
        if "test" not in item_name:
            self.click_element((By.ID, f"add-to-cart-sauce-labs-{item_name}"))
        else:
            self.click_element(
                (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
            )

    def items_in_cart_count(self):
        return self.find_element(self.CART_BADGE).text

    def open_cart(self):
        self.click_element(self.CART_CONTAINER)

    def open_side_bar(self):
        self.click_element(self.BURGER_MENU)

    def logout(self):
        self.click_element(self.LOGOUT_BUTTON)

    def get_items_list(self):
        return self.ITEMS_LIST

    def get_all_items_list(self):
        items = self.get_elements(self.ITEM_NAME)
        items_list = []
        for item in items:
            items_list.append(item.text)
        return items_list

    def get_all_prices_list(self):
        prices = self.get_elements(self.PRICE)
        prices_list = []
        for price in prices:
            price_float = float(price.text.strip("$"))
            prices_list.append(price_float)
        return prices_list

    def select_sorting(self):
        dropdown_list = self.find_element(self.DROPDOWN_SORT)
        return Select(dropdown_list)

    def sort_a_to_z(self):
        select = self.select_sorting()
        return select.select_by_value("az")

    def sort_z_to_a(self):
        select = self.select_sorting()
        return select.select_by_value("za")

    def sort_low_to_high(self):
        select = self.select_sorting()
        return select.select_by_value("lohi")

    def sort_high_to_low(self):
        select = self.select_sorting()
        return select.select_by_value("hilo")
