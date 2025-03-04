import time

import allure
from locators.transaction_page_locators import TransactionPageLocators
from locators.customer_account_page_locators import CustomerAccountPageLocators


@allure.feature("Проверка Deposit")
class TestDeposit:
    @allure.story('Успешный депозит')
    def test_successful_deposit(self, customer_account_page, login):
        with allure.step('Ввод суммы депозита и проверка отображения успешного сообщения после депозита'):
            customer_account_page.click_deposit_button()
            customer_account_page.enter_deposit_amount("1000")
            customer_account_page.click_submit_deposit()
            expected_successful_message = 'Deposit Successful'
            actual_successful_message = customer_account_page.get_message_text()
            assert expected_successful_message == actual_successful_message, f'Успешное сообщение не отображается. ' \
                                                                             f'Сообщение которое отображется: ' \
                                                                             f'{actual_successful_message}'


@allure.feature("Проверка Transactions")
class TestTransactions:
    @allure.story('Проверка наличия транзакций в списке')
    def test_transaction_count(self, customer_account_page, transaction_page, login):
        with allure.step('Депозит'):
            customer_account_page.click_deposit_button()
            customer_account_page.enter_deposit_amount("1000")
            customer_account_page.click_submit_deposit()
        with allure.step('Переход на страницу с транзакциями'):
            customer_account_page.click_transaction_button()
            time.sleep(5)
            assert transaction_page.element_is_visible(
                TransactionPageLocators.TRANSACTION_TABLE), 'Переход на страницу с транзакциями неуспешный'
        with allure.step('Проверка наличия транзакций в списке'):
            transaction_count = transaction_page.get_transaction_count()
            assert transaction_count > 0, 'Список транзакций пуст'


@allure.feature("Проверка Withdeawl")
class TestWithdeawl:
    @allure.story('Успешный вывод средств')
    def test_successful_withdrawal(self, customer_account_page, login):
        with allure.step('Ввод суммы депозита и проверка отображения успешного сообщения после депозита'):
            customer_account_page.click_deposit_button()
            customer_account_page.enter_deposit_amount("1000")
            customer_account_page.click_submit_deposit()
            expected_successful_message = 'Deposit Successful'
            actual_successful_message = customer_account_page.get_message_text()
            assert expected_successful_message == actual_successful_message, f'Успешное сообщение не отображается. ' \
                                                                             f'Сообщение которое отображется: ' \
                                                                             f'{actual_successful_message}'
        with allure.step('Ввод суммы вывода и проверка отображения успешного сообщения после вывода'):
            customer_account_page.click_withdrawal_button()
            time.sleep(1)
            customer_account_page.enter_deposit_amount("10")
            customer_account_page.click_submit_deposit()
            expected_successful_message = 'Transaction successful'
            actual_successful_withdrawal_message = customer_account_page.get_message_text()
            assert expected_successful_message == actual_successful_withdrawal_message, f'Успешное сообщение не отображается. ' \
                                                                                        f'Сообщение которое отображется: ' \
                                                                                        f'{actual_successful_withdrawal_message}'


@allure.feature("Проверка смены account number")
class TestAccountNumber:
    @allure.story("Успешная смена account_number")
    def test_select_account_number(self, customer_account_page, login):
        with allure.step("Смена account number и проверка отображения выбранного account number в селекторе"):
            expected_account_number = "1005"
            assert customer_account_page.select_account_number(expected_account_number)
            actual_account_number = customer_account_page.get_account_number()
            assert expected_account_number == actual_account_number, f"Выбранный неверный account number. " \
                                                                     f"Текущий account number: {actual_account_number}"
