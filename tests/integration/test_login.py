import pytest
from pages.login_page import LoginPage


@pytest.mark.parametrize(
    ("name", "password"), [
        ('standard_user', 'secret_sauce'),
        ('locked_out_user', 'secret_sauce'),
        ('problem_user', 'secret_sauce'),
        ('performance_glitch_user', 'secret_sauce'),
    ]
)
def test_valid_login(driver, name, password):
    login_page = LoginPage(driver)
    login_page.get_login_page()
    login_page.enter_username(name)
    login_page.enter_password(password)
    login_page.click_login()
    if name == 'locked_out_user':
        assert "https://www.saucedemo.com/" == driver.current_url, \
            "Ошибка: логин удался"
    else:
        assert "inventory" in driver.current_url, "Ошибка: логин не удался"
