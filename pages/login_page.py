import time

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def open_page(self, url="https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login") -> None:
        self.open_url(url=url)

    def click_customer_login_button(self) -> None:
        self.click(LoginPageLocators.CUSTOMER_LOGIN_BUTTON)

    def click_bank_manager_login_button(self) -> None:
        self.click(LoginPageLocators.BANK_MANAGER_LOGIN_BUTTON)

    def click_login_button(self) -> None:
        self.click(LoginPageLocators.LOGIN_BUTTON)

    def pick_customer(self, customer_name: str) -> bool:
        self.click(LoginPageLocators.CUSTOMER_SELECTOR)
        if self.select_from_list(locator=LoginPageLocators.CUSTOMER_SELECTOR, label=customer_name):
            return True
        else:
            return False

    def login(self, customer_name: str) -> None:
        self.click_customer_login_button()
        self.pick_customer(customer_name=customer_name)
        self.click_login_button()
