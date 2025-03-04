import time
import allure

from locators.transaction_page_locators import TransactionPageLocators


@allure.feature("Проверка Deposit")
class TestDeposit:
    @allure.story('Успешный депозит')
    def test_successful_deposit(self, customer_account_page, login):
        with allure.step('Ввод суммы депозита и проверка отображения успешного сообщения после депозита'):
            customer_account_page.make_deposit("1000")
            expected_balance = "100"
            actual_balance = customer_account_page.get_balance()
            assert expected_balance == actual_balance, f'Ожидаемый баланс: 1000. Актуальный баланс: {actual_balance}'


@allure.feature("Проверка Transactions")
class TestTransactions:
    @allure.story('Проверка наличия транзакций в списке')
    def test_transaction_count(self, customer_account_page, transaction_page, login):
        with allure.step('Депозит'):
            customer_account_page.make_deposit("1000")
        with allure.step('Переход на страницу с транзакциями'):
            customer_account_page.click_transaction_button()
            time.sleep(5)
            assert transaction_page.element_is_visible(
                TransactionPageLocators.TRANSACTION_TABLE), 'Переход на страницу с транзакциями неуспешный'
        with allure.step('Проверка наличия транзакций в списке'):
            transaction_count = transaction_page.get_transaction_count()
            assert transaction_count > 0, 'Список транзакций пуст'

    @allure.story('Проверка очистки списка транзакций')
    def test_reset_transactions(self, customer_account_page, transaction_page, login):
        with allure.step('Депозит'):
            customer_account_page.make_deposit("1000")
        with allure.step('Переход на страницу с транзакциями'):
            customer_account_page.click_transaction_button()
        with allure.step('Очистка списка транзакций'):
            customer_account_page.reload_page()
            transaction_page.click_reset()
            transaction_count = transaction_page.get_transaction_count()
            assert transaction_count == 0, f"Список транзакций не очистился. Кол-во транзакций: {transaction_count}"


@allure.feature("Проверка Withdeawl")
class TestWithdeawl:
    @allure.story('Успешный вывод средств')
    def test_successful_withdrawal(self, customer_account_page, login):
        with allure.step('Ввод суммы депозита и проверка отображения успешного сообщения после депозита'):
            customer_account_page.make_deposit("1000")
        with allure.step('Ввод суммы вывода и проверка отображения успешного сообщения после вывода'):
            customer_account_page.make_withdrawal("10")
            expected_balance = "990"
            actual_balance = customer_account_page.get_balance()
            assert expected_balance == actual_balance, f'Ожидаемый баланс: 990. Актуальный баланс: {actual_balance}'


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
