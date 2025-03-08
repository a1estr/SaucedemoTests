import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_customer_page import CheckoutCustomerPage
from pages.checkout_overview_page import CheckoutOverviewPage


@allure.feature("e2e test")
@allure.severity(severity_level="high")
@allure.story("Test Purchase")
def test_purchase(driver):
    with allure.step("Login and navigate to inventory page"):
        login_page = LoginPage(driver)
        login_page.valid_login(name="standard_user", password="secret_sauce")
        assert "inventory" in driver.current_url, "Ошибка: логин не удался"

    with allure.step("Add items to cart"):
        inventory_page = InventoryPage(driver)
        inventory_page.add_to_cart("backpack")
        inventory_page.add_to_cart("fleece-jacket")
        assert inventory_page.items_in_cart_count() == "2", "Число товаров в корзине != 2"

    with allure.step("Open cart and verify items"):
        inventory_page.open_cart()
        assert "cart" in driver.current_url, "Страница с корзиной не открылась"
        cart_page = CartPage(driver)
        added_items = cart_page.get_items_in_cart()
        for item in added_items:
            assert item.text in inventory_page.get_items_list(), "Товары не были добавлены в корзину"
        assert cart_page.items_in_cart_count() == "2", "Число товаров в корзине != 2"

    with allure.step("Proceed to checkout and enter customer info"):
        cart_page.checkout_order()
        assert "checkout-step-one" in driver.current_url, "Страница с заполнением информации о покупателе не открылась"
        checkout_customer_page = CheckoutCustomerPage(driver)
        checkout_customer_page.enter_valid_customer_info(first_name="Ivan", last_name="Ivanov", postal_code="220037")

    with allure.step("Confirm order details and complete purchase"):
        checkout_customer_page.submit_info()
        assert "checkout-step-two" in driver.current_url, "Страница с информацией о заказе не открылась"
        overview_page = CheckoutOverviewPage(driver)
        overview_items = overview_page.get_items_in_overview()
        for item in overview_items:
            assert item.text in inventory_page.get_items_list(), "Товары не были добавлены в корзину"
        assert cart_page.items_in_cart_count() == "2", "Число товаров в корзине != 2"

    with allure.step("Complete order"):
        overview_page.complete_order()
        assert "complete" in driver.current_url, "Заказ не оформлен"