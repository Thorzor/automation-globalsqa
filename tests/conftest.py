import datetime
import time

import pytest
import os
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.customer_account_page import CustomerAccountPage
from pages.transaction_page import TransactionPage
from pages.bank_manager import BankManager


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


@pytest.fixture(scope="function")
def login_page(page):
    LoginPage(page).open_page()
    return LoginPage(page)


@pytest.fixture(scope="function")
def customer_account_page(page):
    return CustomerAccountPage(page)


@pytest.fixture(scope="function")
def transaction_page(page):
    return TransactionPage(page)


@pytest.fixture(scope="function")
def bank_manager_page(page, login_page):
    login_page.click_bank_manager_login_button()
    return BankManager(page)


@pytest.fixture(scope="function")
def login(login_page):
    login_page.click_customer_login_button()
    login_page.pick_customer(customer_name='Harry Potter')
    login_page.click_login_button()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="function", autouse=True)
def screenshot_on_failure(request, page):
    yield

    if request.node.rep_call.failed:
        try:

            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")

            test_name = f"{request.node.name}-{time.time()}"
            screenshot_file = f"screenshots/{test_name}_failed.png"

            page.screenshot(path=screenshot_file)
            print(f"\nСкриншот сохранен: {screenshot_file}")
        except Exception as e:
            print(f"Ошибка при создании скриншота: {e}")
