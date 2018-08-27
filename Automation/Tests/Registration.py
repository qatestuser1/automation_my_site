import Pages
from EnvironmentSetUp import *
import unittest
from Functions import *
import time

class Registration(EnvironmentSettingUp):
    def test_registration_success(self):
        self.driver.get("https://qayanaautomation.ml/register/")
        register_page = Pages.RegisterPage(self.driver)
        username = get_random_name(10)
        first_name = get_random_name(10)
        last_name = get_random_name(10)
        email = generate_random_email(12)
        password = '123asdQQ'
        confirm_password = password
        register_page.registration_process(username, first_name, last_name, email, password, confirm_password)

        after_registration_page = Pages.AfterRegistration(self.driver)
        assert after_registration_page.after_registration_title_text() == first_name + ' ' + last_name

    def test_registration_empty_required_fields(self):
        self.driver.get("https://qayanaautomation.ml/register/")
        register_page = Pages.RegisterPage(self.driver)
        register_page.click_register_button()

        registration_validation_errors_page = Pages.RegistrationValidationErrorsPage(self.driver)
        assert registration_validation_errors_page.get_username_validation_error_text() == "Username is required"
        assert registration_validation_errors_page.get_email_validation_error_text() == "You must provide your email"
        assert registration_validation_errors_page.get_password_validation_error_text() == "Password is required"