from selenium.webdriver.common.by import By

from pages.Page import Page


class CheckoutPage(Page):
    PATH = 'checkout'
    S_SUBMIT_AND_PAY = (By.CSS_SELECTOR, f'[id="button__submit-and-pay"]')

    def __init__(self, browser, base_url):
        super().__init__(browser, base_url)

    # Elements
    @property
    def submitAndPayBtn(self):
        return self.browser.find_element(*self.S_SUBMIT_AND_PAY)

    # User Actions
    def open(self):
        self.browser.get(f'{self.base_url}/{self.PATH}')