import Pages
from EnvironmentSetUp import *
import unittest
from Functions import *
import time

class Cart(EnvironmentSettingUp):
    def test_hover_cart(self):
        self.driver.get("https://qayanaautomation.ml/shop/")
        shop_page = Pages.ShopPage(self.driver)
        shop_page.add_to_cart()
        cart_with_products_page = Pages.CartWithProducts(self.driver)
        cart_with_products_page.hover_cart()
        time.sleep(10)
        cart_with_products_page.click_on_view_cart_button()
        time.sleep(10)