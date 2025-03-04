import allure
from locators.bank_manager_locators import BankManagerLocators


@allure.feature("Проверка логина")
class TestLoginPage:
    @allure.story('Проверка успепшного логина под ролью customer')
    def test_customer_successful_login(self, login_page, customer_account_page):
        with allure.step('Выбор пользователя из списка для логина'):
            login_page.click_customer_login_button()
            assert login_page.pick_customer(customer_name='Hermoine Granger')
        with allure.step('Логин и проверка что вход выполнен под выбранным пользователем'):
            login_page.click_login_button()
            expected_customer_name = 'Hermoine Granger'
            actual_customer_name = customer_account_page.get_customer_name()
            assert expected_customer_name == actual_customer_name, f'Имя пользователя на странице не совпадает с ' \
                                                                   f'тем что выбрали в списке. ' \
                                                                   f'Имя пользователя на странице: {actual_customer_name}'

    @allure.story('Проверка уаспешного логина под ролью bank manager')
    def test_bank_manager_successful_login(self, login_page):
        with allure.step('Клик по кнопке для входа под ролью bank manager'):
            login_page.click_bank_manager_login_button()
        with allure.step('Проверка наличия кнопки для добавления customer'):
            assert login_page.element_is_clickable(locator=
                                                   BankManagerLocators.ADD_CUSTOMER_BUTTON), 'Кнопки добавления покупателя нету на странице'

    @allure.story('Проверка успешного выхода из аккаунта под ролью customer')
    def test_customer_successful_logout(self, login_page, customer_account_page):
        with allure.step('Вход в аккаунт под ролью customer'):
            login_page.login(customer_name='Ron Weasly')
            expected_customer_name = 'Ron Weasly'
            actual_customer_name = customer_account_page.get_customer_name()
            assert expected_customer_name == actual_customer_name, f'Имя пользователя на странице не совпадает с ' \
                                                                   f'тем что выбрали в списке. ' \
                                                                   f'Имя пользователя на странице: {actual_customer_name}'
        with allure.step('Выход из аккаунта'):
            customer_account_page.logout()
            current_location = login_page.get_current_url()
            expected_location = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer'
            assert current_location == expected_location, f'Выход из аккаунта неуспешный. ' \
                                                          f'Текущее расположение: {current_location}'

    @allure.story('Проверка перехода на страницу для входа с помощью кнопки Home')
    def test_move_to_home(self, login_page, customer_account_page, login):
        with allure.step('Клик по кнопке Home и проверка перенапралвения на страницу для входа'):
            login_page.click_home_button()
            expected_url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
            actual_url = login_page.get_current_url()
            assert expected_url == actual_url, f"Редирект произошел на страницу {actual_url}"
