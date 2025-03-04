from pages.base_page import BasePage
from locators.bank_manager_locators import BankManagerLocators


class BankManager(BasePage):
    def click_add_customer(self) -> None:
        self.click(BankManagerLocators.ADD_CUSTOMER_BUTTON)

    def click_open_account(self) -> None:
        self.click(BankManagerLocators.OPEN_ACCOUNT_BUTTON)

    def click_customers(self) -> None:
        self.click(BankManagerLocators.CUSTOMERS_BUTTON)

    def search_customer(self, customer_name: str) -> None:
        self.fill_value(BankManagerLocators.SEARCH_CUSTOMER, value=customer_name)

    def get_first_name(self) -> str:
        return self.get_element_text(BankManagerLocators.FIRST_NAME)

    def get_last_name(self) -> str:
        return self.get_element_text(BankManagerLocators.LAST_NAME)
