from pages.base_page import BasePage
from locators.customer_account_page_locators import CustomerAccountPageLocators


class CustomerAccountPage(BasePage):
    def get_customer_name(self) -> str:
        return self.get_element_text(CustomerAccountPageLocators.CUSTOMER_NAME)

    def get_message_text(self) -> str:
        return self.get_element_text(CustomerAccountPageLocators.MESSAGE)

    def get_account_number(self) -> str:
        return self.get_element_text(CustomerAccountPageLocators.ACCOUNT_NUMBER).replace(" ", "")

    def click_transaction_button(self) -> None:
        self.click(CustomerAccountPageLocators.TRANSACTIONS_BUTTON)

    def click_deposit_button(self) -> None:
        self.click(CustomerAccountPageLocators.DEPOSIT_BUTTON)

    def click_withdrawal_button(self) -> None:
        self.click(CustomerAccountPageLocators.WITHDRAWAL_BUTTON)

    def click_submit_deposit(self) -> None:
        self.click(CustomerAccountPageLocators.SUBMIT_DEPOSIT)

    def enter_deposit_amount(self, amount) -> None:
        self.fill_value(locator=CustomerAccountPageLocators.AMOUNT_INPUT, value=amount)

    def logout(self) -> None:
        self.click(CustomerAccountPageLocators.LOGOUT_BUTTON)

    def select_account_number(self, account_number: str) -> bool:
        self.click(CustomerAccountPageLocators.ACCOUNT_SELECTOR)
        if self.select_from_list(locator=CustomerAccountPageLocators.ACCOUNT_SELECTOR, label=account_number):
            return True
        else:
            return False
