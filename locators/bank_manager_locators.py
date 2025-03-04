class BankManagerLocators:
    # Buttons
    ADD_CUSTOMER_BUTTON = "//button[@ng-class='btnClass1']"
    OPEN_ACCOUNT_BUTTON = "//button[@ng-class='btnClass2']"
    CUSTOMERS_BUTTON = "//button[@ng-class='btnClass3']"
    # Elements
    ADD_CUSTOMER_FORM = "//form[@ng-submit='addCustomer()']"
    OPEN_ACCOUNT_FORM = "//form[@ng-submit='process()']"
    CUSTOMER_TABLE = "//table[@class='table table-bordered table-striped']"
    SEARCH_CUSTOMER = "//input[@class='form-control ng-pristine ng-untouched ng-valid']"
    # Search table
    FIRST_NAME = "//td[@class='ng-binding'][1]"
    LAST_NAME = "//td[@class='ng-binding'][2]"
