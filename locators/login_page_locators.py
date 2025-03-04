class LoginPageLocators:
    CUSTOMER_LOGIN_BUTTON = "//button[text()='Customer Login']"
    BANK_MANAGER_LOGIN_BUTTON = "//button[text()='Bank Manager Login']"
    CUSTOMER_SELECTOR = "//select[contains(@class, 'form-control')]"
    LOGIN_BUTTON = "//button[@class='btn btn-default']"
    HOME_BUTTON = "//button[@class='btn home']"

    @staticmethod
    def get_xpath_by_customer_name(customer_name: str) -> str:
        return f"//option[text()='{customer_name}']"
