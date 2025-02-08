import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture
def login(driver):
    login_page = LoginPage(driver)
    login_page.valid_login(name="standard_user",
                           password="secret_sauce"
                           )
    return login_page


def test_sort_a_to_z(driver, login):
    # Применим сортировку A to Z
    inventory_page = InventoryPage(driver)
    inventory_page.sort_a_to_z()

    # Проверим примененную сортировку
    inventory_page.get_items_list()
    items_list = inventory_page.get_all_items_list()
    assert items_list == sorted(inventory_page.ITEMS_LIST), \
        "Товары отсортированы некорректно"


def test_sort_z_to_a(driver, login):
    # Применим сортировку A to Z
    inventory_page = InventoryPage(driver)
    inventory_page.sort_z_to_a()

    # Проверим примененную сортировку
    inventory_page.get_items_list()
    items_list = inventory_page.get_all_items_list()
    assert items_list == sorted(inventory_page.ITEMS_LIST, reverse=True), \
        "Товары отсортированы некорректно"


def test_sort_low_to_high(driver, login):
    # Применим сортировку по стоимости Low to High
    inventory_page = InventoryPage(driver)
    inventory_page.sort_low_to_high()

    # Проверим примененную сортировку
    prices_list = inventory_page.get_all_prices_list()
    assert prices_list == sorted(inventory_page.PRICES_LIST), \
        "Товары отсортированы некорректно"


def test_sort_high_to_low(driver, login):
    # Применим сортировку по стоимости High to Low
    inventory_page = InventoryPage(driver)
    inventory_page.sort_high_to_low()

    # Проверим примененную сортировку
    prices_list = inventory_page.get_all_prices_list()
    assert prices_list == sorted(inventory_page.PRICES_LIST, reverse=True), \
        "Товары отсортированы некорректно"
