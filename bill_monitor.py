from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path_to_chromedriver = "/Users/Moomookittyclam/Documents/Programming projects/Bills_moniter/chromedriver"

class bill_monitor:
    def __init__(self, file=None):
        self.chromedriver = webdriver.Chrome(path_to_chromedriver)
        self.file = file

    def read_file(self, file):
        print('TODO')

    def get_tmobile_bill(self):
        self.chromedriver.get('https://www.t-mobile.com/')
        self.chromedriver.find_element_by_id('user-links-dropdown').click()
        self.chromedriver.find_element_by_id('user-link-dropdown-item-0-0-0').click()
        WebDriverWait(self.chromedriver, 10).until(EC.presence_of_element_located((By.ID, "usernameTextBox")))
        self.chromedriver.find_element_by_id('usernameTextBox').send_keys('USERNAME')
        self.chromedriver.find_element_by_id('lp1-next-btn').click()
        WebDriverWait(self.chromedriver, 10).until(EC.presence_of_element_located((By.ID, "passwordTextBox")))
        self.chromedriver.find_element_by_id('passwordTextBox').send_keys('PASSWORD')
        self.chromedriver.find_element_by_id('lp2-login-btn').click()

    def close_driver(self):
        self.chromedriver.close()
