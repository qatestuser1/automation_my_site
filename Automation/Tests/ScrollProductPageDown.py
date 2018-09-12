import Pages
from EnvironmentSetUp import *
import time

class ScrollProductPageDown(EnvironmentSettingUp):
    def test_scroll_product_and_add_to_cart(self):
        self.driver.get("https://qayanaautomation.ml/shop/")
        shop_page = Pages.ShopPage(self.driver)
        shop_page.open_product()
        product_name = shop_page.get_opened_product_name()
        shop_page.scroll_down_on_product_page()
        product_name_on_alert = shop_page.get_product_name_on_alert()

        assert product_name == product_name_on_alert
        time.sleep(10)
        shop_page.add_product_to_cart_via_alert()

        product_page_after_adding_to_cart = Pages.ProductPageAfterAddingToCart(self.driver)
        assert product_page_after_adding_to_cart.get_added_to_cart_message() == "“" + product_name + '” has been added to your cart.'
