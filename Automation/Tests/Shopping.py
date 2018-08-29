import Pages
from EnvironmentSetUp import *
import unittest
from Functions import *
import time

class Shopping(EnvironmentSettingUp):

    def test_open_random_product_and_add_to_cart_and_order_with_cash(self):
        self.driver.get("https://qayanaautomation.ml/shop/")

        shop_page = Pages.ShopPage(self.driver)
        shop_page.open_product()
        open_product_name = shop_page.get_opened_product_name()

        product_page = Pages.ProductPage(self.driver)
        product_price = product_page.get_product_price()
        product_name = product_page.get_product_name()

        assert open_product_name == product_name
        product_quantity = 3

        product_page.set_product_quantity(product_quantity)
        product_page.add_product_to_cart()

        product_page_after_adding_to_cart = Pages.ProductPageAfterAddingToCart(self.driver)

        assert product_page_after_adding_to_cart.get_added_to_cart_message() == str(product_quantity) + ' × “' + product_name + '” have been added to your cart.'

        product_page_after_adding_to_cart.click_view_cart()

        cart_page = Pages.CartPage(self.driver)
        assert cart_page.get_subtotal() == '$' + '{:.2f}'.format(float(product_price[1:]) * product_quantity)
        time.sleep(3)
        cart_page.proceed_to_check_out()
        check_out_page = Pages.CheckOutPage(self.driver)
        check_out_page.fill_billing_details('Suki', 'Hannah', 'Qcompany', 'Russia', 'Sarmiento 151, Piso 3,'
                                            ' Oficina 311 BIS', '112', 'Moscow', 'Russia/Moscow', '03142',
                                            '+380664322345', 'qa_test_mail@neo.com', 'Some notes...')
        time.sleep(3)
        check_out_page.click_on_place_order()

        order_details_page = Pages.OrderDetailsPage(self.driver)
        assert order_details_page.get_order_number() is not None
        assert order_details_page.get_order_total() == '$' + '{:.2f}'.format(float(product_price[1:]) * product_quantity)
        assert order_details_page.get_order_payment_method() == '\nCash on delivery'

    def test_open_random_product_and_add_to_cart_and_order_with_pay_pal(self):
        self.driver.get("https://qayanaautomation.ml/shop/")

        shop_page = Pages.ShopPage(self.driver)
        shop_page.open_product()
        open_product_name = shop_page.get_opened_product_name()

        product_page = Pages.ProductPage(self.driver)
        product_price = product_page.get_product_price()
        product_name = product_page.get_product_name()

        assert open_product_name == product_name

        product_quantity = 3
        product_page.set_product_quantity(product_quantity)
        product_page.add_product_to_cart()

        product_page_after_adding_to_cart = Pages.ProductPageAfterAddingToCart(self.driver)

        assert product_page_after_adding_to_cart.get_added_to_cart_message() == str(
            product_quantity) + ' × “' + product_name + '” have been added to your cart.'

        product_page_after_adding_to_cart.click_view_cart()

        cart_page = Pages.CartPage(self.driver)
        assert cart_page.get_subtotal() == '$' + '{:.2f}'.format(float(product_price[1:]) * product_quantity)

        cart_page.proceed_to_check_out()
        check_out_page = Pages.CheckOutPage(self.driver)
        time.sleep(3)
        check_out_page.fill_billing_details('Suki', 'Hannah', 'Qcompany', 'Russia', 'Sarmiento 151, Piso 3,'
                                                                                    ' Oficina 311 BIS', '112', 'Moscow',
                                            'Russia/Moscow', '03142',
                                            '+380664322345', 'qa_test_mail@neo.com', 'Some notes...')

        check_out_page.select_pay_pal_payment()
        check_out_page.click_on_place_order()

        pay_pal_page = Pages.PayPalPage(self.driver)
        pay_pal_page.pay_pal_sign_in_process('pp.personal01-buyer@example.com', '2710yana')
        time.sleep(15)
        pay_pal_page.click_pay_now()
        time.sleep(15)

        order_details_page = Pages.OrderDetailsPage(self.driver)
        assert order_details_page.get_order_number() is not None
        assert order_details_page.get_order_total() == '$' + '{:.2f}'.format(
            float(product_price[1:]) * product_quantity)
        assert order_details_page.get_order_payment_method() == 'PayPal'
