from pages.Page import Page


class HomePage(Page):
	def __init__(self, browser, base_url):
		super().__init__(browser, base_url)

	def open(self):
		self.browser.get(f'{self.base_url}')
