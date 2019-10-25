from selenium.webdriver.common.by import By

from components.Component import Component


class Header(Component):

	def __init__(self, browser, base_url, selector='header'):
		super().__init__(browser, (By.CSS_SELECTOR, selector))
		self.S_GET_QUOTE = (By.CSS_SELECTOR, f'{selector} [href="/manufacture/"]')
		self.S_HAMBURGER_MENU = (By.CSS_SELECTOR, f'{selector} [id="navbar__hamburger"]')

	@property
	def quoteBtn(self):
		return self.browser.find_element(*self.S_GET_QUOTE)

	@property
	def hamburgerBtn(self):
		return self.browser.find_element(*self.S_HAMBURGER_MENU)

