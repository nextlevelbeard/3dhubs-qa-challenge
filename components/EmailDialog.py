from selenium.webdriver.common.by import By
from components.Component import Component


class EmailDialog(Component):
    def __init__(self, browser, selector='[id="mat-dialog-0"]'):
        super().__init__(browser, (By.CSS_SELECTOR, selector))
        self.EMAIL_INPUT = (By.CSS_SELECTOR, f'{selector} #email')
        self.UPDATES_CHECKBOX = (By.CSS_SELECTOR, f'{selector} label[class*="checkbox"]')
        self.UPDATES_INPUT = (By.CSS_SELECTOR, f'{selector} input[type="checkbox"]')
        self.SUBMIT_BTN = (By.CSS_SELECTOR, f'{selector} button[type="submit"]')

    # Elements
    @property
    def emailInput(self):
        return self.browser.find_element(*self.EMAIL_INPUT)

    @property
    def updatesInput(self):
        return self.browser.find_element(*self.UPDATES_INPUT)

    @property
    def updatesCheckbox(self):
        return self.browser.find_element(*self.UPDATES_CHECKBOX)

    @property
    def submitBtn(self):
        return self.browser.find_element(*self.SUBMIT_BTN)

    @property
    def updatesChecked(self):
        if self.updatesInput.get_attribute("checked") == 'true':
            return True
        return False

    # User Actions
    def fill(self, email, wantsUpdates=False):
        if email is not None:
            self.emailInput.clear()
            self.emailInput.send_keys(email)
        if self.updatesChecked != wantsUpdates:
            self.updatesCheckbox.click()

    def submit(self, email, updates=False):
        self.fill(email, updates)
        self.submitBtn.click()