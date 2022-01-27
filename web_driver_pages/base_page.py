from logs.logger import Logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, webdriver):
        self.webdriver = webdriver
        self.logger = Logger

    def refresh_page(self):
        self.webdriver.refresh()

    def wait_for_presence_of_elem(self, locator_tuple):
        loc_str = locator_tuple[1]
        self.logger.info(f"Waiting for presence of element '{loc_str}'")
        return WebDriverWait(self.chromedriver, 10).until(EC.presence_of_element_located(locator_tuple))

    def wait_for_elem_clickable(self, locator_tuple):
        loc_str = locator_tuple[1]
        self.logger.info(f"Waiting for element '{loc_str}' to be clicked")
        return WebDriverWait(self.chromedriver, 10).until(EC.element_to_be_clickable(locator_tuple))

    def fill_in_field(self, locator_tuple, value):
        loc_str = locator_tuple[1]
        self.logger.info(f"Filling elem {loc_str} with {value}")
        WebDriverWait(self.chromedriver, 10).until(EC.element_to_be_clickable(locator_tuple)).clear()
        WebDriverWait(self.chromedriver, 10).until(EC.element_to_be_clickable(locator_tuple)).send_keys(value)
