import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.parametrize(
    ("name", "password"), [
        ('standard_user', 'secret_sauce'),
        ('performance_glitch_user', 'secret_sauce'),
        ('problem_user', 'secret_sauce'),
        ('error_user', 'secret_sauce'),
        ('visual_user', 'secret_sauce')
    ]
)
def test_logout(driver, name, password):
    login_page = LoginPage(driver)

    # Залогинимся на сайт
    login_page.valid_login(name, password)
    inventory_page = InventoryPage(driver)

    # Откроем выпадающее меню
    inventory_page.open_side_bar()

    # Нажнем кнопку Logout
    inventory_page.logout()
    assert "https://www.saucedemo.com/" in driver.current_url, \
        "Пользователь не разлогинен"
