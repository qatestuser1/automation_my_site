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

#Blog page

#Sample page

#Lost password page

#Search page

