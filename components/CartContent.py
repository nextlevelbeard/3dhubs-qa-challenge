from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

from components.Component import Component
from components.HubSpotDialog import HubSpotDialog


class CartContent(Component):
	def __init__(self, browser, selector='[class*="h3d-quote-request-cart__content"]'):
		super().__init__(browser, (By.CSS_SELECTOR, selector))
		# Selectors
		self.S_SUBMIT_BTN = (By.CSS_SELECTOR, f'{selector} button[type="submit"]')
		self.S_FLOATING_TOTAL = (By.CSS_SELECTOR, f'{selector} h3d-quote-request-subtotal .floating-total')
		self.S_CALCULATED_SUBTOTAL = (By.CSS_SELECTOR, f'{selector} [data-subtotal__calculated-subtotal]')

	# Elements
	@property
	def floatingTotal(self):
		return self.browser.find_element(*self.S_FLOATING_TOTAL)

	@property
	def submitBtn(self):
		return self.browser.find_element(*self.S_SUBMIT_BTN)

	@property
	def calculatedSubtotal(self):
		return self.browser.find_element(*self.S_CALCULATED_SUBTOTAL)

	# User Actions
	def submit(self):
		self.browser.wait.until(lambda x: self.calculatedSubtotal.is_displayed())
		self.browser.execute_script("return arguments[0].scrollIntoView({block: 'center'})", self.submitBtn)

		try:
			self.submitBtn.click()
		except ElementClickInterceptedException as e:
			HubSpotDialog(self.browser).dismiss()
			self.submitBtn.click()
