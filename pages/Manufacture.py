from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

from components.CartContent import CartContent
from components.HubSpotDialog import HubSpotDialog
from components.EmailDialog import EmailDialog
from pages.Page import Page


class ManufacturePage(Page):
    PATH = 'manufacture'
    # Selectors
    S_UPLOADER_PRIVACY = (By.CSS_SELECTOR, "h3d-uploader-privacy")
    S_UPLOAD_SAMPLE_BTN = (By.CSS_SELECTOR, f'{S_UPLOADER_PRIVACY[1]} button')
    S_FILE_INPUT = (By.CSS_SELECTOR, '[id="file"]')

    def __init__(self, browser, base_url):
        super().__init__(browser, base_url)
        # Components
        self.CartContent = CartContent(self.browser)
        self.EmailDialog = EmailDialog(self.browser)

    # Element
    @property
    def sampleBtn(self):
        return self.browser.find_element(*self.S_UPLOAD_SAMPLE_BTN)

    @property
    def fileInput(self):
        return self.browser.find_element(*self.S_FILE_INPUT)

    # User Actions
    def open(self):
        self.browser.get(f'{self.base_url}/{self.PATH}')

    def useSample(self):
        sampleBtn = self.sampleBtn
        try:
            sampleBtn.click()
        except ElementClickInterceptedException as e:
            HubSpotDialog(self.browser).dismiss()
            sampleBtn.click()

    def uploadFile(self, absFilePath):
        self.fileInput.send_keys(absFilePath)


