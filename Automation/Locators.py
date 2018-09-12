from selenium.webdriver.common.by import By
class Locators:

#Home page
    my_account_link = (By.LINK_TEXT, 'My account')
    register_link = (By.LINK_TEXT, 'Register')
    blog_link = (By.LINK_TEXT, 'Blog')
    sample_page_link = (By.LINK_TEXT, 'Sample Page')
    search_products_field = (By.CLASS_NAME, 'search-field')
    cart_button = (By.CLASS_NAME, 'cart-contents')
#Shop page
    products_add_to_cart_buttons = [
        #(By.XPATH, '//*[@id="main"]/ul/li[1]/a[2]'),
        #(By.XPATH, '//*[@id="main"]/ul/li[2]/a[2]'),
        #(By.XPATH, '//*[@id="main"]/ul/li[3]/a[2]'),
        #(By.XPATH, '//*[@id="main"]/ul/li[4]/a[2]'),
        (By.XPATH, '//*[@id="main"]/ul/li[5]/a[2]'),
        #(By.XPATH, '//*[@id="main"]/ul/li[6]/a[2]'),
        (By.XPATH, '//*[@id="main"]/ul/li[7]/a[2]'),
        (By.XPATH, '//*[@id="main"]/ul/li[8]/a[2]'),
        (By.XPATH, '//*[@id="main"]/ul/li[9]/a[2]'),
        (By.XPATH, '//*[@id="main"]/ul/li[10]/a[2]'),
        (By.XPATH, '//*[@id="main"]/ul/li[11]/a[2]'),
        (By.XPATH, '//*[@id="main"]/ul/li[12]/a[2]')
    ]

    products_names = [
        #(By.XPATH, '//*[@id="main"]/ul/li[1]/a[1]/h2'),
        #(By.XPATH, '//*[@id="main"]/ul/li[2]/a[1]/h2'),
        #(By.XPATH, '//*[@id="main"]/ul/li[3]/a[1]/h2'),
        #(By.XPATH, '//*[@id="main"]/ul/li[4]/a[1]/h2'),
        (By.XPATH, '//*[@id="main"]/ul/li[5]/a[1]/h2'),
        #(By.XPATH, '//*[@id="main"]/ul/li[6]/a[1]/h2'),
        (By.XPATH, '//*[@id="main"]/ul/li[7]/a[1]/h2'),
        (By.XPATH, '//*[@id="main"]/ul/li[8]/a[1]/h2'),
        (By.XPATH, '//*[@id="main"]/ul/li[9]/a[1]/h2'),
        (By.XPATH, '//*[@id="main"]/ul/li[10]/a[1]/h2'),
        (By.XPATH, '//*[@id="main"]/ul/li[11]/a[1]/h2'),
        (By.XPATH, '//*[@id="main"]/ul/li[12]/a[1]/h2')
    ]

#Cart with products page
    cart_content = (By.CSS_SELECTOR, '.cart-contents')
    cart_content_list_first = (By.XPATH, '//*[@id="site-header-cart"]/li[2]/div[1]/div[1]/ul[1]/li[1]')
    view_cart_button = (By.XPATH, '//*[@id="site-header-cart"]/li[2]/div/div/p[2]/a[1]')
#Product page
    product_name_title = (By.CSS_SELECTOR, '.product_title.entry-title')
    product_quantity = (By.CSS_SELECTOR, '.input-text.qty.text')
    add_to_cart_button = (By.CSS_SELECTOR, '.single_add_to_cart_button.button.alt')
    product_price_label = (By.CSS_SELECTOR, '.price')

    product_alert = (By.CSS_SELECTOR, '.storefront-sticky-add-to-cart__content')
    product_name_on_alert = (By.XPATH, '//*[@id="page"]/section/div/div/div/span[1]/strong')
    add_to_cart_button_on_alert = (By.CSS_SELECTOR, '.storefront-sticky-add-to-cart__content-button.button.alt')
#Product page after adding product to cart
    added_to_cart_message = (By.CSS_SELECTOR, '.woocommerce-message')
    view_cart_link = (By.CSS_SELECTOR, '.button.wc-forward')
#Cart page
    cart_product = (By.CLASS_NAME, 'product-name')
    cart_product_price = (By.CLASS_NAME, 'product-price')
    cart_product_quantity = (By.CLASS_NAME, 'product-quantity')
    cart_product_total = (By.CLASS_NAME, 'product-subtotal')

    cart_subtotal = (By.CSS_SELECTOR, '.woocommerce-Price-amount.amount')
    check_out_button = (By.CSS_SELECTOR, '.checkout-button.button.alt.wc-forward')
    cart_product_name = (By.CSS_SELECTOR, '.product-name')
#Checkout page
    billing_first_name_field = (By.ID, 'billing_first_name')
    billing_last_name_field = (By.ID, 'billing_last_name')
    billing_company_field = (By.ID, 'billing_company')
    billing_country_drop_down = (By.ID, 'select2-billing_country-container')
    billing_country_search_field = (By.CLASS_NAME, 'select2-search__field')
    billing_address1_field = (By.ID, 'billing_address_1')
    billing_address2_field = (By.ID, 'billing_address_2')
    billing_city_field = (By.ID, 'billing_city')
    billing_county_optional_field = (By.ID, 'billing_state')
    billing_post_code_field = (By.ID, 'billing_postcode')
    billing_phone_field = (By.ID, 'billing_phone')
    billing_email_field = (By.ID, 'billing_email')
    order_comments_field = (By.ID, 'order_comments')

    payment_method_pay_pal_radio = (By.CSS_SELECTOR, '.wc_payment_method.payment_method_paypal')


    place_order_button = (By.ID, 'place_order')
#PayPal page
    pay_pal_email_field = (By.XPATH, '//*[@id="email"]')
    pay_pal_password_field = (By.XPATH, '//*[@id="password"]')
    pay_pal_sign_in_button = (By.XPATH, '//*[@id="btnLogin"]')

    pay_pal_pay_now_button = (By.XPATH, '//*[@id="confirmButtonTop"]')
#Order received & Order details page
    order_thank_you_message = (By.CSS_SELECTOR, '.woocommerce-notice.woocommerce-notice--success.woocommerce-thankyou-order-received')
    order_number = (By.CSS_SELECTOR, '.woocommerce-order-overview__order.order')
    order_date = (By.CSS_SELECTOR, '.woocommerce-order-overview__date.date')
    order_total = (By.CSS_SELECTOR, '.woocommerce-order-overview__total.total')
    order_payment_method = (By.CSS_SELECTOR, '.woocommerce-order-overview__payment-method.method')
#About page

#Contact page

#My Account page
    username_or_email_address_field = (By.XPATH, '//*[@id="username"]')
    password_field = (By.XPATH, '//*[@id="password"]')
    log_in_button = (By.NAME, 'login')
    lost_your_password_link = (By.LINK_TEXT, 'Lost your password?')
#My Account page errors
    invalid_username_error_text = (By.XPATH, '//*[@id="content"]/div/div[1]/ul/li')

#My Account Lost password page
    lost_username_or_email_field = (By.NAME, 'user_login')
    reset_password_button = (By.XPATH, '//*[@id="post-37"]/div/div/form/p[3]/button')

#Lost password message page
    lost_password_message = (By.XPATH, '//*[@id="post-37"]/div/div/div')

#Lost password error page
    lost_password_error = (By.XPATH, '//*[@id="content"]/div/div[1]/ul/li')
#My Account Dashboard page
    dashboard_text = (By.XPATH, '//*[@id="post-37"]/div/div/div/p[1]')
#Register page
    username_field = (By.ID, 'user_login-7')
    first_name_field = (By.ID, 'first_name-7')
    last_name_field = (By.ID, 'last_name-7')
    email_address_field = (By.ID, 'user_email-7')
    password_reg_field = (By.ID, 'user_password-7')
    confirm_password_field = (By.ID, 'confirm_user_password-7')
    register_button = (By.ID, 'um-submit-btn')

#After Registration page
    after_registration_title = (By.XPATH, '//*[@id="post-11"]/header/h1')
#Registration Validation Errors Page
    username_validation_error = (By.XPATH, '//*[@id="post-15"]/div/div/div/form/div[1]/div/div[1]/div[3]')
    email_validation_error = (By.XPATH, '//*[@id="post-15"]/div/div/div/form/div[1]/div/div[4]/div[3]')
    password_validation_error = (By.XPATH, '//*[@id="post-15"]/div/div/div/form/div[1]/div/div[5]/div[3]')
#Blog page

#Sample page

#Lost password page

#Search page
    search_results_title = (By.XPATH, '//*[@id="main"]/header/h1')
    search_results_info_box = (By.XPATH, '//*[@id="main"]/p')

