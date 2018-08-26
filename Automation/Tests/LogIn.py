import Pages
from EnvironmentSetUp import *
import unittest

class LogIn(EnvironmentSettingUp):
    def test_success_log_in(self):
        self.driver.get("https://qayanaautomation.ml/")

        home_page = Pages.HomePage(self.driver)
        home_page.get_my_account().click()

        account = Pages.AccountPage(self.driver)
        account.get_username_or_email_address().send_keys('admin')
        account.get_password().send_keys('pass')
        account.get_log_in().click()

        my_account_dashboard = Pages.MyAccountDashboardPage(self.driver)
        assert my_account_dashboard.get_dashboard()

    def test_invalid_credentials_log_in(self):
        self.driver.get("https://qayanaautomation.ml/")

        home_page = Pages.HomePage(self.driver)
        home_page.get_my_account().click()

        account = Pages.AccountPage(self.driver)
        account.get_username_or_email_address().send_keys('sdsad')
        account.get_password().send_keys('asdasd')
        account.get_log_in().click()

        account_page_error = Pages.AccountPageError(self.driver)
        assert account_page_error.get_invalid_username_error() == "ERROR: Invalid username. Lost your password?"


if __name__ == "__main__":
    unittest.main()