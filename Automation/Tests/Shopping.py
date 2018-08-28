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

        product_page.add_product_to_cart()

        product_page_after_adding_to_cart = Pages.ProductPageAfterAddingToCart(self.driver)

        assert product_page_after_adding_to_cart.get_added_to_cart_message() == 'View cart\n' + '“' + product_name + '” has been added to your cart.'

        product_page_after_adding_to_cart.click_view_cart()


