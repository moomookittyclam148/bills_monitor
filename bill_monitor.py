import os
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

script_dir = os.path.dirname(__file__)
path_to_chromedriver = os.path.join(script_dir, "../chromedriver")

class bill_monitor:
    def __init__(self, file=None):
        self.chromedriver = webdriver.Chrome(path_to_chromedriver)
        self.file = file
        self.bill_dict = {}

    def read_json(self, file):
        with open(os.path.join(script_dir, file)) as open_file:
            self.user_auth_file = json.load(open_file)


    def get_tmobile_bill(self):
        if self.user_auth_file == None:
            print('Load user auth json first')
        else:
            self.chromedriver.get('https://www.t-mobile.com/')
            self.chromedriver.find_element_by_id('user-links-dropdown').click()
            self.chromedriver.find_element_by_id('user-link-dropdown-item-0-0-0').click()
            WebDriverWait(self.chromedriver, 10).until(EC.presence_of_element_located((By.ID, "usernameTextBox")))
            self.chromedriver.find_element_by_id('usernameTextBox').send_keys(self.user_auth_file['user_info']['tmobile_info']['username'])
            self.chromedriver.find_element_by_id('lp1-next-btn').click()
            WebDriverWait(self.chromedriver, 10).until(EC.presence_of_element_located((By.ID, "passwordTextBox")))
            self.chromedriver.find_element_by_id('passwordTextBox').send_keys(self.user_auth_file['user_info']['tmobile_info']['password'])
            self.chromedriver.find_element_by_id('lp2-login-btn').click()

    def close_driver(self):
        self.chromedriver.close()
