from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    ITEM_NAME_IN_OVERVIEW = (By.CLASS_NAME, "inventory_item_name")
    FINISH_BUTTON = (By.ID, "finish")

    def get_items_in_overview(self):
        return self.get_elements(self.ITEM_NAME_IN_OVERVIEW)

    def complete_order(self):
        self.click_element(self.FINISH_BUTTON)
