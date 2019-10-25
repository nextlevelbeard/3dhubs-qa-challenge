import pytest
import os
import json

from datetime import datetime
from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.support.ui import WebDriverWait

from components.CookieBanner import CookieBanner
from components.EmailDialog import EmailDialog
from pages.Checkout import CheckoutPage
from pages.CheckoutGuard import CheckoutGuardPage
from pages.Home import HomePage
from pages.Manufacture import ManufacturePage

from definitions import CONFIG_PATH, ASSETS_PATH
DEFAULT_WAIT_TIME = 30
SUPPORTED_BROWSERS = ['chrome', 'firefox']

@pytest.fixture(scope='session')
def config():
    with open(os.path.join(CONFIG_PATH, 'config.json')) as config_file:
        data = json.load(config_file)
    return data

@pytest.fixture(scope='session')
def config_browser(config):
    if 'browser' not in config:
        raise Exception('The config file does not contain "browser"')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config['browser']

@pytest.fixture(scope='session')
def config_wait_time(config):
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture(scope='session')
def base_url(base_url):
    if base_url == '' or base_url is None:
        return "https://www.3dhubs.com"

@pytest.fixture
def browser(config_browser, config_wait_time):
    if config_browser == 'chrome':
        driver = Chrome()
    elif config_browser == 'firefox':
        driver = Firefox()
    else:
        raise Exception(f'"{config_browser}" is not a supported browser')
    driver.implicitly_wait(config_wait_time)
    driver.wait = WebDriverWait(driver, config_wait_time, 1)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            timestamp = datetime.now().strftime("%d %B %Y @ %HH%Mm%Ss")
            filename = f'{ASSETS_PATH}/scr on {timestamp}.png'
            browser = item.funcargs['browser']
            browser.save_screenshot(filename)
            extra.append(pytest_html.extras.image(filename))
            report.extra = extra


@pytest.fixture
def manufacture_page(browser, base_url):
    return ManufacturePage(browser, base_url)

@pytest.fixture
def home_page(browser, base_url):
    return HomePage(browser, base_url)

@pytest.fixture
def email_dialog(browser, base_url):
    return EmailDialog(browser)

@pytest.fixture
def checkout_page(browser, base_url):
    return CheckoutPage(browser, base_url)

@pytest.fixture
def checkout_guard_page(browser, base_url):
    return CheckoutGuardPage(browser, base_url)

@pytest.fixture
def cookie_banner(browser, base_url):
    return CookieBanner(browser)