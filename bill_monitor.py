import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

script_dir = os.path.dirname(__file__)
path_to_chromedriver = os.path.join(script_dir, "../chromedriver")

class bill_monitor:
    def __init__(self, options={}):
        self.chromedriver = webdriver.Chrome(path_to_chromedriver, options=options)
        self.bill_dict = {}

    # Utility methods
    def read_json(self, file):
        with open(os.path.join(script_dir, file)) as open_file:
            self.user_auth_file = json.load(open_file)

    def display_bill_data(self):
        for dict in self.bill_dict:
            print('----------------------------')
            print(f"Current Ammount due: {str(self.bill_dict[dict]['bill_amount']).ljust(22)}")
            print(f"Current due due: {str(self.bill_dict[dict]['due_date']).ljust(22)}")
            print('----------------------------')


    def close_driver(self):
        self.chromedriver.close()

    # Getting Bill data such as due date and amount due
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
            self.chromedriver.implicitly_wait(20)
            WebDriverWait(self.chromedriver, 10).until(EC.presence_of_element_located((By.ID, "lp2-login-btn")))
            self.chromedriver.find_element_by_id('lp2-login-btn').click()
            due_date = self.chromedriver.find_element_by_xpath("//div[contains(text(), 'Due ')]").text
            due_date = due_date.replace('Due ', '')
            bill_amount = self.chromedriver.find_element_by_xpath("//div[contains(text(), '$')]").text
            bill_amount = float(bill_amount.replace('$', ''))
            self.bill_dict.update({"tmobile" : {"due_date" : due_date, "bill_amount" : bill_amount}})
