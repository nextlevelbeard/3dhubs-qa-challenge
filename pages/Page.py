from components.Header import Header


class Page(object):

	def __init__(self, browser, base_url):
		self.browser = browser
		self.base_url = base_url
		self.Header = Header(browser, base_url)