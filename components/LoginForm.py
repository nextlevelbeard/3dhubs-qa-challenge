from selenium.webdriver.common.by import By

from components.Component import Component


class LoginForm(Component):
    def __init__(self, browser, selector='h3d-login-form form'):
        # Selectors
        super().__init__(browser, (By.CSS_SELECTOR, selector))
        self.S_EMAIL_INPUT = (By.CSS_SELECTOR, f'{selector} #email')
        self.S_PWD_INPUT = (By.CSS_SELECTOR, f'{selector} #password')
        self.S_SUBMIT_BTN = (By.CSS_SELECTOR, f'{selector} button[type="submit"]')

    # Elements
    @property
    def emailInput(self):
        return self.browser.find_element(*self.S_EMAIL_INPUT)

    @property
    def pwdInput(self):
        return self.browser.find_element(*self.S_PWD_INPUT)

    @property
    def submitBtn(self):
        return self.browser.find_element(*self.S_SUBMIT_BTN)

    # User actions
    def fill(self, email, password):
        if email is not None:
            self.emailInput.clear()
            self.emailInput.send_keys(email)
        if password is not None:
            self.pwdInput.clear()
            self.pwdInput.send_keys(password)

    def submit(self, email, password):
        self.fill(email, password)
        self.submitBtn.click()