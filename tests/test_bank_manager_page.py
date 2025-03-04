import time

import allure
from locators.bank_manager_locators import BankManagerLocators


@allure.feature('Проверка страницы Bank Manager')
class TestBankManger:
    @allure.story('Проверка перехода по вкладкам на станица Bank Manager')
    def test_navigating_through_tabs(self, bank_manager_page):
        with allure.step('Переход на вкладку для добавления пользователей'):
            bank_manager_page.click_add_customer()
            time.sleep(1)
            assert bank_manager_page.element_is_visible(
                BankManagerLocators.ADD_CUSTOMER_FORM), 'Форма для добавления пользователей не отобразилась'
        with allure.step('Переход на вкладку для открытия аккаунта'):
            bank_manager_page.click_open_account()
            time.sleep(1)
            assert bank_manager_page.element_is_visible(
                BankManagerLocators.OPEN_ACCOUNT_FORM), 'Форма для открытия аккаунта не отобразилась'
        with allure.step('Переход на вкладку cо списком пользователей'):
            bank_manager_page.click_customers()
            time.sleep(1)
            assert bank_manager_page.element_is_visible(
                BankManagerLocators.CUSTOMER_TABLE), 'Таблица с пользователями не отобразилась'

    @allure.story('Проверка поиска пользователей')
    def test_customer_search(self, bank_manager_page):
        with allure.step('Переход на страницу для поиска пользователей'):
            bank_manager_page.click_customers()
        with allure.step('Вводи имени пользователя'):
            bank_manager_page.search_customer(customer_name="Potter")
        with allure.step('Проверка выдачи поиска'):
            expected_result = "Potter"
            assert expected_result == bank_manager_page.get_first_name() or bank_manager_page.get_last_name(), \
                'Пользователь с таким именем не найден'
