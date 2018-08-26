from selenium.webdriver.common.by import By
class Locators(object):

#Home page
    my_account_link = (By.LINK_TEXT, 'My account')
    register_link = (By.LINK_TEXT, 'Register')
    blog_link = (By.LINK_TEXT, 'Blog')
    sample_page_link = (By.LINK_TEXT, 'Sample Page')

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
#My Account page errors
    invalid_username_error_text = (By.XPATH, '//*[@id="content"]/div/div[1]/ul/li')
#My Account Dashboard page
    dashboard_text = (By.XPATH, '//*[@id="post-37"]/div/div/div/p[1]')
#Register page

#Blog page

#Sample page

#Lost password page

#Search page

