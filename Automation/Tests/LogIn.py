import Pages
from EnvironmentSetUp import *
import unittest
import Functions
import time

class LogIn(EnvironmentSettingUp):
    def test_log_in_success(self):
        self.driver.get("https://qayanaautomation.ml/")

        home_page = Pages.HomePage(self.driver)
        home_page.get_my_account().click()

        account = Pages.AccountPage(self.driver)
        account.log_in_process('admin', 'pass')

        my_account_dashboard = Pages.MyAccountDashboardPage(self.driver)
        assert my_account_dashboard.get_dashboard()

    def test_log_in_invalid_credentials(self):
        self.driver.get("https://qayanaautomation.ml/")

        home_page = Pages.HomePage(self.driver)
        home_page.get_my_account().click()

        account = Pages.AccountPage(self.driver)
        account.log_in_process(Functions.get_random_name(12), Functions.get_random_name(12))

        account_page_error = Pages.AccountPageError(self.driver)
        assert account_page_error.get_invalid_username_error() == "ERROR: Invalid username. Lost your password?"

    def test_log_in_invalid_password(self):
        self.driver.get("https://qayanaautomation.ml/")

        home_page = Pages.HomePage(self.driver)
        home_page.get_my_account().click()

        account = Pages.AccountPage(self.driver)
        account.log_in_process('admin', Functions.get_random_name(12))

        account_page_error = Pages.AccountPageError(self.driver)
        assert account_page_error.get_invalid_username_error() == "ERROR: The password you entered for the username admin is incorrect. Lost your password?"

    def test_lost_password_success(self):
        self.driver.get("https://qayanaautomation.ml/my-account/lost-password/")

        lost_password_page = Pages.AccountLostPassword(self.driver)
        lost_password_page.reset_password_process('admin')

        lost_password_message_page = Pages.Lost_password_message(self.driver)
        assert lost_password_message_page.get_lost_password_message_text() == "Password reset email has been sent."

    def test_lost_password_invalid_username_or_email(self):
        self.driver.get("https://qayanaautomation.ml/my-account/lost-password/")

        lost_password_page = Pages.AccountLostPassword(self.driver)
        lost_password_page.reset_password_process(Functions.get_random_name(6))

        lost_password_error_page = Pages.Lost_password_error(self.driver)
        assert lost_password_error_page.get_lost_password_error_text() == "Invalid username or email."

if __name__ == "__main__":
    unittest.main()