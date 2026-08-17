import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_successful_login(page: Page, base_url: str):
    login_page = LoginPage(page, base_url)

    login_page.open()

    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )


@pytest.mark.parametrize(
    "username,password",
    [
        ("wrong_user", "wrong_password"),
        ("standard_user", "wrong_password"),
        ("wrong_user", "secret_sauce"),
    ],
    ids=[
        "invalid_username_and_password",
        "valid_username_invalid_password",
        "invalid_username_valid_password",
    ]
)
def test_invalid_login(
    page: Page,
    base_url: str,
    username: str,
    password: str
):
    login_page = LoginPage(page, base_url)

    login_page.open()

    login_page.login(username, password)

    error_message = page.locator("[data-test='error']")

    expect(error_message).to_have_text(
        "Epic sadface: Username and password do not match any user in this service"
    )