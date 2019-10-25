import os
from pytest_bdd import scenario, given, when, then
from pages.Checkout import CheckoutPage

from definitions import ASSETS_PATH
STL_FILE = os.path.join(ASSETS_PATH, 'its_your_sample_but_im_uploading_it.stl')


#Scenarios
@scenario('manufacture.feature', 'Can proceed to checkout after uploading a 3D model file')
def test_proceed_to_checkout_uploading_file(browser, base_url):
	pass

@scenario('manufacture.feature', 'Can proceed to checkout by using the sample')
def test_proceed_to_checkout_using_sample(browser, base_url):
	pass

# Steps
@given("I go to 3D Hubs")
def go_to_3d_hubs(home_page):
	home_page.open()

@given("I choose to get a quote")
def choose_to_get_a_quote(home_page):
	hamburgerBtn = home_page.Header.hamburgerBtn
	if hamburgerBtn.is_displayed():
		hamburgerBtn.click()
	home_page.Header.quoteBtn.click()

@given("I upload a file")
def upload_a_file(browser, base_url, manufacture_page):
	manufacture_page.uploadFile(STL_FILE)

@given("I choose to upload a sample part")
def choose_to_upload_a_sample_part(browser, base_url, manufacture_page):
	manufacture_page.useSample()

@given("I enter my email")
def enter_my_email(browser, base_url, email_dialog):
	email_dialog.submit('1@1.com')

@when("I press Continue")
def press_Continue(browser, base_url, manufacture_page):
	manufacture_page.CartContent.submit()

@when("I login")
def login(browser, base_url, checkout_guard_page):
	checkout_guard_page.LoginForm.submit(None, "1!aAaaaa")

@then("I should see the checkout")
def should_see_the_checkout(browser, base_url, checkout_page):
	assert CheckoutPage.PATH in browser.current_url
	assert checkout_page.submitAndPayBtn.is_displayed() is True