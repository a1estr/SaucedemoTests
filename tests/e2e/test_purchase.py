from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_customer_page import CheckoutCustomerPage
from pages.checkout_overview_page import CheckoutOverviewPage


def test_purchase(driver):
    # Залогинимся и перейдем на страницу с товарами
    login_page = LoginPage(driver)
    login_page.valid_login(name="standard_user",
                           password="secret_sauce"
                           )
    assert "inventory" in driver.current_url, "Ошибка: логин не удался"

    # Добавим несколько товаров в корзину
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart("backpack")
    inventory_page.add_to_cart("fleece-jacket")

    # Проверим, что корзина не пустая
    assert inventory_page.items_in_cart_count() == "2", "Число товаров в корзине != 2"

    # Перейдем в корзину
    inventory_page.open_cart()
    assert "cart" in driver.current_url, "Страница с корзиной не открылась"

    # Проверим, что товары присутствуют в корзине
    cart_page = CartPage(driver)
    added_items = cart_page.get_items_in_cart()
    for item in added_items:
        assert item.text in inventory_page.get_items_list(), \
            "Товары не были добавлены в корзину"
    assert cart_page.items_in_cart_count() == "2", "Число товаров в корзине != 2"

    # Перейдем на страницу заполнения информации покупателя
    cart_page.checkout_order()
    assert "checkout-step-one" in driver.current_url, \
        "Страница с заполнением информации о покупателе не открылась"

    # Заполним данные о покупателе
    checkout_customer_page = CheckoutCustomerPage(driver)
    checkout_customer_page.enter_valid_customer_info(first_name="Ivan",
                                                     last_name="Ivanov",
                                                     postal_code="220037"
                                                     )

    # Перейдем на финальную страницу оформления заказа
    checkout_customer_page.submit_info()
    assert "checkout-step-two" in driver.current_url, \
        "Страница с информацией о заказе не открылась"

    # Проверим, что выбранные товары присутствуют в заполненном заказе
    overview_page = CheckoutOverviewPage(driver)
    overview_items = overview_page.get_items_in_overview()
    for item in overview_items:
        assert item.text in inventory_page.get_items_list(), \
            "Товары не были добавлены в корзину"
    assert cart_page.items_in_cart_count() == "2", "Число товаров в корзине != 2"

    # Завершаем оформление заказа
    overview_page.complete_order()
    assert "complete" in driver.current_url, "Заказ не оформлен"
