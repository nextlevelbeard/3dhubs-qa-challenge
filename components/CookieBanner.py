from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By

from components.Component import Component


class CookieBanner(Component):
    def __init__(self, browser, selector='.cookie-consent-banner'):
        super().__init__(browser, (By.CSS_SELECTOR, selector))
        self.ALLOW_BTN = (By.CSS_SELECTOR, f'{selector} button')

    # Elements
    @property
    def allowBtn(self):
        return self.browser.find_element(*self.ALLOW_BTN)

    # User Actions
    def allow(self):
        if self.container.is_displayed():
            self.browser.wait.until(lambda x: self.allowBtn.is_displayed())
            try:
                self.allowBtn.click()
            except ElementNotInteractableException: # geckodriver issue, bug?
                self.allowBtn.click()
            self.browser.wait.until_not(lambda x: self.container.is_displayed())
