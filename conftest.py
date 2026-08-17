import os

import pytest


@pytest.fixture(scope="session")
def base_url():
    return "https://www.saucedemo.com"


@pytest.fixture
def logged_in_page(page, base_url):
    from pages.login_page import LoginPage

    login_page = LoginPage(page, base_url)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    return page


@pytest.fixture(autouse=True)
def screenshot_on_failure(page, request):
    yield

    if request.node.rep_call.failed:
        os.makedirs("screenshots", exist_ok=True)

        screenshot_path = (
            f"screenshots/{request.node.name}.png"
        )

        page.screenshot(
            path=screenshot_path,
            full_page=True
        )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, f"rep_{rep.when}", rep)