from Locators import *
from selenium.webdriver.common.keys import Keys
from Functions import *
#Home page
class HomePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.my_account = driver.find_element(*Locators.my_account_link)
        self.register = driver.find_element(*Locators.register_link)
        self.blog = driver.find_element(*Locators.blog_link)
        self.sample_page = driver.find_element(*Locators.sample_page_link)
        self.search = driver.find_element(*Locators.search_products_field)

    def get_my_account(self):
        return self.my_account

    def get_register(self):
        return self.register

    def get_blog(self):
        return self.blog

    def get_sample_page(self):
        return self.sample_page

    def perform_search(self, search_input):
        self.search.send_keys(search_input)
        self.search.send_keys(Keys.ENTER)


#Shop page
class ShopPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.products_add = []
        self.products_names = []
        self.added_product = ''
        self.opened_product = ''
        self.opened_product_name = ''

        for product_add in Locators.products_add_to_cart_buttons:
            self.products_add.append(driver.find_element(*product_add))

        for product_name in Locators.products_names:
            self.products_names.append(driver.find_element(*product_name))

    def get_random_product_add(self):
        return get_random_in_list(self.products_add)

    def add_to_cart(self):
        self.added_product = self.get_random_product_add()
        self.added_product.click()

    def get_random_product_name(self):
        return get_random_in_list(self.products_names)

    def open_product(self):
        self.opened_product = self.get_random_product_name()
        self.opened_product_name = self.opened_product.text
        self.opened_product.click()

    def get_opened_product_name(self):
        return self.opened_product_name

#Product page
class ProductPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.product_name = driver.find_element(*Locators.product_name_title)

    def get_product_name(self):
        return self.product_name.text

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
        self.forgot_password = driver.find_element(*Locators.lost_your_password_link)

    def set_username_or_email_address(self, username):
        self.username_or_email_address.send_keys(username)

    def set_password(self, password):
        self.password.send_keys(password)

    def click_log_in(self):
        self.log_in.click()

    def get_invalid_username_error(self):
        return self.invalid_username_error

    def log_in_process(self, username, password):
        self.set_password(password)
        self.set_username_or_email_address(username)
        self.click_log_in()

    def lost_your_password(self):
        return self.forgot_password

class AccountPageError(object):
    def __init__(self, driver):
        self.driver = driver
        self.invalid_username_error = driver.find_element(*Locators.invalid_username_error_text)

    def get_invalid_username_error(self):
        return self.invalid_username_error.text

class AccountLostPassword(object):
    def __init__(self, driver):
        self.driver = driver
        self.lost_username_or_email = driver.find_element(*Locators.lost_username_or_email_field)
        self.reset_password = driver.find_element(*Locators.reset_password_button)

    def set_lost_username_or_email(self, username_or_email):
        self.lost_username_or_email.send_keys(username_or_email)

    def click_reset_password(self):
        self.reset_password.click()

    def reset_password_process(self, username_or_email):
        self.set_lost_username_or_email(username_or_email)
        self.click_reset_password()

class Lost_password_message(object):
    def __init__(self, driver):
        self.driver = driver
        self.lost_password_message = driver.find_element(*Locators.lost_password_message)
    def get_lost_password_message_text(self):
        return self.lost_password_message.text


class Lost_password_error(object):
    def __init__(self, driver):
        self.driver = driver
        self.lost_password_error = driver.find_element(*Locators.lost_password_error)
    def get_lost_password_error_text(self):
        return self.lost_password_error.text

#My Account Dashboard page
class MyAccountDashboardPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.dashboard = driver.find_element(*Locators.dashboard_text)

    def get_dashboard(self):
        return self.dashboard
#Register page
class RegisterPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.username = driver.find_element(*Locators.username_field)
        self.first_name = driver.find_element(*Locators.first_name_field)
        self.last_name = driver.find_element(*Locators.last_name_field)
        self.email_address = driver.find_element(*Locators.email_address_field)
        self.password = driver.find_element(*Locators.password_reg_field)
        self.confirm_password = driver.find_element(*Locators.confirm_password_field)
        self.register = driver.find_element(*Locators.register_button)

    def set_username(self, username):
        self.username.send_keys(username)

    def set_first_name(self, first_name):
        self.first_name.send_keys(first_name)

    def set_last_name(self, last_name):
        self.last_name.send_keys(last_name)

    def set_email_address(self, email_address):
        self.email_address.send_keys(email_address)

    def set_password(self, password):
        self.password.send_keys(password)

    def set_confirm_password(self, confirm_password):
        self.confirm_password.send_keys(confirm_password)

    def click_register_button(self):
        self.register.click()

    def registration_process(self, username, first_name, last_name, email_address, password, confirm_password):
        self.set_username(username)
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_email_address(email_address)
        self.set_password(password)
        self.set_confirm_password(confirm_password)
        self.click_register_button()

class AfterRegistration(object):
    def __init__(self, driver):
        self.driver = driver
        self.after_registration = driver.find_element(*Locators.after_registration_title)

    def after_registration_title_text(self):
        return self.after_registration.text


class RegistrationValidationErrorsPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.username_required = driver.find_element(*Locators.username_validation_error)
        self.email_required = driver.find_element(*Locators.email_validation_error)
        self.password_required = driver.find_element(*Locators.password_validation_error)

    def get_username_validation_error_text(self):
        return self.username_required.text

    def get_email_validation_error_text(self):
        return self.email_required.text

    def get_password_validation_error_text(self):
        return self.password_required.text

#Blog page

#Sample page

#Lost password page

#Search page
class SearchPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.search_results_info = driver.find_element(*Locators.search_results_info_box)
        self.search_results_title = driver.find_element(*Locators.search_results_title)

    def get_search_results_info_text(self):
        return self.search_results_info.text

    def get_search_results_title_text(self):
        return self.search_results_title.text