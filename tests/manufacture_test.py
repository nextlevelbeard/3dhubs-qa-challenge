import pytest
import os
from pages.Checkout import CheckoutPage

dir = os.path.dirname(__file__)
ROOT_DIR = os.path.dirname(dir)
ASSETS_DIR = os.path.join(ROOT_DIR, 'assets')
STL_FILE = os.path.join(ASSETS_DIR, 'its_your_sample_but_im_uploading_it.stl')

@pytest.mark.parametrize("email,password", [("1@1.com", "1!aAaaaa")])
def test_can_proceed_to_checkout(
    browser, base_url,
    manufacture_page, cookie_banner, email_dialog, checkout_page, checkout_guard_page, email, password):

    manufacture_page.open()
    cookie_banner.allow()

    manufacture_page.useSample()
    manufacture_page.EmailDialog.submit(email)
    manufacture_page.CartContent.submit()
    checkout_guard_page.LoginForm.submit(None, password)

    assert CheckoutPage.PATH in browser.current_url
    assert checkout_page.submitAndPayBtn.is_displayed() is True

@pytest.mark.parametrize("email,password", [("1@1.com", "1!aAaaaa")])
def test_can_proceed_to_checkout_by_uploading_own_file(
    browser, base_url,
    manufacture_page, cookie_banner, email_dialog, checkout_page, checkout_guard_page,
    email, password):

    manufacture_page.open()
    cookie_banner.allow()

    manufacture_page.uploadFile(STL_FILE)
    manufacture_page.EmailDialog.submit(email)
    manufacture_page.CartContent.submit()
    checkout_guard_page.LoginForm.submit(None, password)

    assert CheckoutPage.PATH in browser.current_url
    assert checkout_page.submitAndPayBtn.is_displayed() is True
