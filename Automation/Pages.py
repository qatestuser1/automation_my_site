from Locators import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Functions import *
import time
#Home page
class HomePage:
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
class ShopPage:
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

    def scroll_down_on_product_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_product_name_on_alert(self):
        return self.driver.find_element(*Locators.product_name_on_alert).text

    def add_product_to_cart_via_alert(self):
        self.driver.find_element(*Locators.add_to_cart_button_on_alert).click()

class CartWithProducts:
    def __init__(self, driver):
        self.driver = driver
        self.cart = driver.find_element(*Locators.cart_content)

    def hover_cart(self):
        ActionChains(self.driver).move_to_element(self.cart).perform()

    def click_on_view_cart_button(self):
        self.driver.find_element(*Locators.view_cart_button).click()

#Product page
class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_name = driver.find_element(*Locators.product_name_title)
        self.add_to_cart = driver.find_element(*Locators.add_to_cart_button)
        self.quantity = driver.find_element(*Locators.product_quantity)
        self.product_price = driver.find_element(*Locators.product_price_label)

    def get_product_name(self):
        return self.product_name.text

    def get_product_price(self):
        return self.product_price.text

    def add_product_to_cart(self):
        self.add_to_cart.click()

    def set_product_quantity(self, quantity):
        self.quantity.clear()
        self.quantity.send_keys(quantity)
#Product page after adding product to cart
class ProductPageAfterAddingToCart:
    def __init__(self, driver):
        self.driver = driver
        self.added_to_cart_message = driver.find_element(*Locators.added_to_cart_message)
        self.view_cart = driver.find_element(*Locators.view_cart_link)

    def get_added_to_cart_message(self):
        return self.added_to_cart_message.text.strip('View cart\n')

    def click_view_cart(self):
        self.view_cart.click()

#Cart page
class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.product = driver.find_element(*Locators.cart_product) # returns "Product"
        self.price = driver.find_element(*Locators.cart_product_price) # returns "Price"
        self.quantity = driver.find_element(*Locators.cart_product_quantity) # returns "Quantity"
        self.total = driver.find_element(*Locators.cart_product_total) # returns "Total"

        self.subtotal = driver.find_element(*Locators.cart_subtotal)
        self.check_out = driver.find_element(*Locators.check_out_button)

    def get_subtotal(self):
        return self.subtotal.text

    def proceed_to_check_out(self):
        self.check_out.click()


#Checkout page
class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver
        self.billing_first_name = driver.find_element(*Locators.billing_first_name_field)
        self.billing_last_name = driver.find_element(*Locators.billing_last_name_field)
        self.billing_company = driver.find_element(*Locators.billing_company_field)
        self.billing_country = driver.find_element(*Locators.billing_country_drop_down)
        self.billing_address1 = driver.find_element(*Locators.billing_address1_field)
        self.billing_address2 = driver.find_element(*Locators.billing_address2_field)
        self.billing_city = driver.find_element(*Locators.billing_city_field)
        self.billing_county_optional = driver.find_element(*Locators.billing_county_optional_field)
        self.billing_post_code = driver.find_element(*Locators.billing_post_code_field)
        self.billing_phone = driver.find_element(*Locators.billing_phone_field)
        self.billing_email = driver.find_element(*Locators.billing_email_field)
        self.order_comments = driver.find_element(*Locators.order_comments_field)
        self.place_order = driver.find_element(*Locators.place_order_button)

    def fill_billing_details(self, billing_first_name, billing_last_name,
                             billing_company, billing_country, billing_address1,
                             billing_address2, billing_city, billing_county_optional,
                             billing_post_code, billing_phone, billing_email,
                             order_comments):
        self.billing_first_name.send_keys(billing_first_name)
        self.billing_last_name.send_keys(billing_last_name)
        self.billing_company.send_keys(billing_company)

        self.billing_country.click()

        billing_country_search = self.driver.find_element(*Locators.billing_country_search_field)
        billing_country_search.send_keys(billing_country)
        billing_country_search.send_keys(Keys.ENTER)

        self.billing_address1.send_keys(billing_address1)
        self.billing_address2.send_keys(billing_address2)
        self.billing_city.send_keys(billing_city)
        self.billing_county_optional.send_keys(billing_county_optional)
        self.billing_post_code.send_keys(billing_post_code)
        self.billing_phone.send_keys(billing_phone)
        self.billing_email.send_keys(billing_email)
        self.order_comments.send_keys(order_comments)

    def select_pay_pal_payment(self):
        #payment_method_pay_pal = self.driver.find_element(*Locators.payment_method_pay_pal_radio)
        payment_method_pay_pal = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(Locators.payment_method_pay_pal_radio))
        payment_method_pay_pal.click()
        time.sleep(3)

    def click_on_place_order(self):
        #time.sleep(3)
        #place_order = self.driver.find_element(*Locators.place_order_button)
        place_order = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(Locators.place_order_button))
        place_order.click()


#PayPal page
class PayPalPage:
    def __init__(self, driver):
        self.driver = driver
        self.pay_pal_email = driver.find_element(*Locators.pay_pal_email_field)
        self.pay_pal_password = driver.find_element(*Locators.pay_pal_password_field)
        self.pay_pal_sign_in = driver.find_element(*Locators.pay_pal_sign_in_button)

    def pay_pal_sign_in_process(self, email, password):
        self.pay_pal_email.clear()
        self.pay_pal_email.send_keys(email)
        #time.sleep(3)
        self.pay_pal_password.clear()
        self.pay_pal_password.send_keys(password)
        self.pay_pal_sign_in.click()

    def click_pay_now(self):
        #pay_pal_pay_now= self.driver.find_element(*Locators.pay_pal_pay_now_button)
        pay_pal_pay_now = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(Locators.pay_pal_pay_now_button))
        pay_pal_pay_now.click()

#Order received & Order details page
class OrderDetailsPage:
    def __init__(self, driver):
        self.driver = driver
        self.order_number = driver.find_element(*Locators.order_number)
        self.order_date = driver.find_element(*Locators.order_date)
        self.order_total = driver.find_element(*Locators.order_total)
        self.order_payment_method = driver.find_element(*Locators.order_payment_method)

    def get_order_number(self):
        return self.order_number.text.strip('ORDER NUMBER:\n')

    def get_order_date(self):
        return self.order_date.text.strip('DATE:\n')

    def get_order_total(self):
        return self.order_total.text.strip('TOTAL:\n')

    def get_order_payment_method(self):
        #return self.order_payment_method.text.strip('PAYMENT METHOD:\n')
        return self.order_payment_method.text[15:]
#About page

#Contact page

#My Account page
class AccountPage:
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

class AccountPageError:
    def __init__(self, driver):
        self.driver = driver
        self.invalid_username_error = driver.find_element(*Locators.invalid_username_error_text)

    def get_invalid_username_error(self):
        return self.invalid_username_error.text

class AccountLostPassword:
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

class Lost_password_message:
    def __init__(self, driver):
        self.driver = driver
        self.lost_password_message = driver.find_element(*Locators.lost_password_message)
    def get_lost_password_message_text(self):
        return self.lost_password_message.text


class Lost_password_error:
    def __init__(self, driver):
        self.driver = driver
        self.lost_password_error = driver.find_element(*Locators.lost_password_error)
    def get_lost_password_error_text(self):
        return self.lost_password_error.text

#My Account Dashboard page
class MyAccountDashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard = driver.find_element(*Locators.dashboard_text)

    def get_dashboard(self):
        return self.dashboard
#Register page
class RegisterPage:
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

class AfterRegistration:
    def __init__(self, driver):
        self.driver = driver
        self.after_registration = driver.find_element(*Locators.after_registration_title)

    def after_registration_title_text(self):
        return self.after_registration.text


class RegistrationValidationErrorsPage:
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
class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_results_info = driver.find_element(*Locators.search_results_info_box)
        self.search_results_title = driver.find_element(*Locators.search_results_title)

    def get_search_results_info_text(self):
        return self.search_results_info.text

    def get_search_results_title_text(self):
        return self.search_results_title.text