import Pages
from EnvironmentSetUp import *
import unittest
from Functions import *
import time

class Shopping(EnvironmentSettingUp):
    def test_open_random_product_and_add_to_cart(self):
        self.driver.get("https://qayanaautomation.ml/shop/")

        shop_page = Pages.ShopPage(self.driver)
        shop_page.open_product()
        open_product_name = shop_page.get_opened_product_name()
        product_page = Pages.ProductPage(self.driver)
        product_name = product_page.get_product_name()
        assert open_product_name == product_name