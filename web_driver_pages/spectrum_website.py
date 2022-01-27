from web_driver_pages.base_page import BasePage

class spectrum_website(BasePage):
    def __init__(self, webdriver):
        super().__init__(self, webdriver)
        self.spectrum_url = 'https://www.spectrum.net/'
        # locator Tuples
        self.LOGIN_BUTTON = (By.ID, 'login-button')
        self.USERNAME_FIELD = (By.ID, 'cc-username')
        self.PASSWORD_FIELD = (By.ID, 'cc-user-password')
        self.SIGN_IN_BUTTON = (By.XPATH, '//button[text()="Sign In"]')
        self.PAYMENT_MESSAGE = (By.CLASS_NAME, 'paymentMessage')

        self.get_spectrum_page()

    def get_spectrum_page(self):
        self.logger.info(f"Hitting url: {self.spectrum_url}")
        self.webdriver.get(self.spectrum_url)

    def login(self, login_tuple):
        self.wait_for_elem_clickable(self.LOGIN_BUTTON).click()
        self.fill_in_field(self.USERNAME_FIELD, login_tuple[0])
        self.fill_in_field(self.PASSWORD_FIELD, login_tuple[1])
        self.wait_for_elem_clickable(self.SIGN_IN_BUTTON).click()
        self.wait_for_presence_of_elem((By.CLASS_NAME, 'paymentMessage'))

    def get_bill_data(self):
        print("TODO")
