from components.LoginForm import LoginForm
from pages.Page import Page


class CheckoutGuardPage(Page):
    PATH = 'checkout-guard'

    def __init__(self, browser, base_url):
        super().__init__(browser, base_url)
        # Components
        self.LoginForm = LoginForm(self.browser)

    # User Actions
    def open(self):
        self.browser.get(f'{self.base_url}/{self.PATH}')