import pytest
from pages.login_page import LoginPage


@pytest.fixture
def opened_login_page(driver):
    login_page = LoginPage(driver)
    login_page.get_login_page()
    return login_page


def test_empty_fields(opened_login_page):
    opened_login_page.click_login()
    assert opened_login_page.get_error_message() == "Epic sadface: Username is required"


def test_filled_username(opened_login_page):
    opened_login_page.enter_username("standard_user")
    opened_login_page.click_login()
    assert opened_login_page.get_error_message() == "Epic sadface: Password is required"


def test_filled_password(opened_login_page):
    opened_login_page.enter_password("secret_sauce")
    opened_login_page.click_login()
    assert (opened_login_page.get_error_message() ==
            "Epic sadface: Username is required")


def test_invalid_credentials(opened_login_page):
    opened_login_page.enter_username("test")
    opened_login_page.enter_password("test")
    opened_login_page.click_login()
    assert (opened_login_page.get_error_message() ==
            "Epic sadface: Username and password do not match any user in this service")