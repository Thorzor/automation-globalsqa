from pages.base_page import BasePage
from locators.transaction_page_locators import TransactionPageLocators


class TransactionPage(BasePage):
    def get_transaction_count(self) -> int:
        return len(self.get_elements(TransactionPageLocators.TRANSACTION_RAW))

    def click_reset(self) -> None:
        self.click(TransactionPageLocators.RESET_BUTTON)
