from selenium.webdriver.common.by import By
class Locators(object):

#Home page
    my_account_link = (By.LINK_TEXT, 'My account')
    register_link = (By.LINK_TEXT, 'Register')
    blog_link = (By.LINK_TEXT, 'Blog')
    sample_page_link = (By.LINK_TEXT, 'Sample Page')
    search_products_field = (By.CLASS_NAME, 'search-field')
    cart_button = (By.CLASS_NAME, 'cart-contents')
#Shop page

#Cart page

#Checkout page

#PayPal page

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

