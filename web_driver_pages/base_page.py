from logs.logger import Logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

class BasePage:
    def __init__(self, webdriver):
        self.webdriver = webdriver
        self.logger = Logger()

    def verify_page_loaded(self):
        WebDriverWait(self.webdriver, 20).until(
            lambda driver: self.webdriver.execute_script('return document.readyState') == 'complete')

    def refresh_page(self):
        self.webdriver.refresh()

    def wait_for_presence_of_elem(self, locator_tuple):
        try:
            loc_str = locator_tuple[1]
            self.logger.info(f"Waiting for presence of element '{loc_str}'")
            return WebDriverWait(self.webdriver, 10).until(EC.presence_of_element_located(locator_tuple))
        except TimeoutException:
            self.logger.error(f"Did not find presence of element '{loc_str}'")

    def wait_for_elem_clickable(self, locator_tuple):
        try:
            loc_str = locator_tuple[1]
            self.logger.info(f"Waiting for element '{loc_str}' to be clicked")
            return WebDriverWait(self.webdriver, 10).until(EC.element_to_be_clickable(locator_tuple))
        except TimeoutException:
            self.logger.error(f"Could not click element '{loc_str}'")

    def fill_in_field(self, locator_tuple, value, is_login=False):
        try:
            loc_str = locator_tuple[1]
            if is_login:
                self.logger.info(f"Filling elem {loc_str} with login info")
            else:
                self.logger.info(f"Filling elem {loc_str} with {value}")

            WebDriverWait(self.webdriver, 10).until(EC.element_to_be_clickable(locator_tuple)).clear()
            WebDriverWait(self.webdriver, 10).until(EC.element_to_be_clickable(locator_tuple)).send_keys(value)
        except TimeoutException:
            self.logger.error(f"Could not fill in element '{loc_str}'")
