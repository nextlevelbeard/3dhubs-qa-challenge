class Component(object):

	def __init__(self, browser, selector):
		self.browser = browser
		self.selector = selector

	@property
	def container(self):
		return self.browser.find_element(*self.selector)