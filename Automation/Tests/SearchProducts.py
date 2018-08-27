import Pages
from EnvironmentSetUp import *
import unittest
from Functions import *
import time

class SearchProducts(EnvironmentSettingUp):
    def test_search_products_invalid(self):
        self.driver.get("https://qayanaautomation.ml/")
        home_page = Pages.HomePage(self.driver)
        search_input = get_random_name(10)
        home_page.perform_search(search_input)

        search_results_page = Pages.SearchPage(self.driver)
        assert search_results_page.get_search_results_info_text() == "No products were found matching your selection."
        assert search_results_page.get_search_results_title_text() == "Search results: “" + search_input + "”"

