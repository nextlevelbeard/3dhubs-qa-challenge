from selenium.webdriver.common.by import By

from components.Component import Component


class HubSpotDialog(Component):
    S_DISMISS_BTN = (By.CSS_SELECTOR, '[aria-label="Dismiss"]')

    def __init__(self, browser, selector='[id="hubspot-messages-iframe-container"] iframe'):
        super().__init__(browser, (By.CSS_SELECTOR, selector))

    @property
    def dismissBtn(self):
        return self.browser.find_element(self.S_DISMISS_BTN)

    # User Actions
    def dismiss(self):
        container = self.container
        if container.is_displayed():
            self.browser.switch_to.frame(container)
            self.dismissBtn.click()
            self.browser.switch_to.default_content()

