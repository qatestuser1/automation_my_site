from unittest import TestCase
from selenium import webdriver


class EnvironmentSettingUp(TestCase):
    def setUp(self):
        #self.driver = webdriver.Chrome('D:/chromedriver_win32/chromedriver.exe')
        self.driver = webdriver.Chrome('C:/Users/YANAK/Downloads/chromedriver_win32/chromedriver.exe')
        print("Chrome Environment Set Up")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    def tearDown(self):
        print("Test Environment Destroyed")
        self.driver.close()
        self.driver.quit()
