from Locators import *

#Home page
class HomePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.my_account = driver.find_element(*Locators.my_account_link)

    def get_my_account(self):
        return self.my_account
#Shop page

#Cart page

#Checkout page

#PayPal page

#About page

#Contact page

#My Account page
class AccountPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.username_or_email_address = driver.find_element(*Locators.username_or_email_address_field)
        self.password = driver.find_element(*Locators.password_field)
        self.log_in = driver.find_element(*Locators.log_in_button)

    def get_username_or_email_address(self):
        return self.username_or_email_address
    def get_password(self):
        return self.password
    def get_log_in(self):
        return self.log_in
    def get_invalid_username_error(self):
        return self.invalid_username_error

class AccountPageError(object):
    def __init__(self, driver):
        self.driver = driver
        self.invalid_username_error = driver.find_element(*Locators.invalid_username_error_text)

    def get_invalid_username_error(self):
        return self.invalid_username_error.text
#My Account Dashboard page
class MyAccountDashboardPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.dashboard = driver.find_element(*Locators.dashboard_text)
    def get_dashboard(self):
        return self.dashboard
#Register page

#Blog page

#Sample page

#Lost password page

#Search page