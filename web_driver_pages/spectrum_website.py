from web_driver_pages.base_page import BasePage
from web_driver_pages.base_page import By
import time

class spectrum_website(BasePage):
    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.spectrum_url = 'https://www.spectrum.net/'
        # locator Tuples
        self.LOADING_SPINNER = (By.CSS_SELECTOR, "ngk-loader-overlay[class*='kite-loader-overlay']")
        self.LOGIN_BUTTON = (By.ID, 'login-button')
        self.USERNAME_FIELD = (By.ID, 'cc-username')
        self.PASSWORD_FIELD = (By.ID, 'cc-user-password')
        self.SIGN_IN_BUTTON = (By.XPATH, '//button[contains(text(),"Sign In")]')
        self.PAYMENT_MESSAGE = (By.CLASS_NAME, 'paymentMessage')
        self.BALANCE_AMOUNT = (By.CSS_SELECTOR, 'span[class="kite-h1 balance"]')

        self.get_spectrum_page()

    def get_spectrum_page(self):
        self.logger.info(f"Hitting url: {self.spectrum_url}")
        self.webdriver.get(self.spectrum_url)

    def login(self, login_tuple):
        self.wait_for_elem_clickable(self.LOGIN_BUTTON).click()
        time.sleep(5)
        self.fill_in_field(self.USERNAME_FIELD, login_tuple[0], True)
        self.fill_in_field(self.PASSWORD_FIELD, login_tuple[1], True)
        self.wait_for_elem_clickable(self.SIGN_IN_BUTTON).click()
        self.wait_for_presence_of_elem((By.CLASS_NAME, 'paymentMessage'))

    def get_bill_data(self):
        due_date = self.wait_for_presence_of_elem(self.PAYMENT_MESSAGE).text
        due_date = due_date.replace('Payment Due by ', '')
        bill_amount = self.wait_for_presence_of_elem(self.BALANCE_AMOUNT).text
        return {"due_date" : due_date, "bill_amount" : bill_amount}
