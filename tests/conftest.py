import getpass
import warnings
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from utilities.utils import Util_Test
from datetime import datetime
from testData import constants
import pytest
import os
import pytz


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")


@pytest.fixture(scope='class')
def test_setup(request):
    driver = None
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        download_path = os.path.abspath(constants.download_path)
        options = webdriver.ChromeOptions()
        options.add_argument("disable-features=DownloadUI")
        options.add_experimental_option("prefs", {
            "download.default_directory": download_path,
            "plugins.plugins_disabled": ["Chrome PDF Viewer"],
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    elif browser == "firefox":
        download_path = os.path.abspath(constants.download_path)
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.manager.showWhenStarting", False)
        options.set_preference("signon.management.page.os-authKeystore", False)
        options.set_preference("browser.download.dir", download_path)
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    elif browser == "edge":
        download_path = os.path.abspath(constants.download_path)
        edge_options = webdriver.EdgeOptions()
        # edge_options.add_argument("--headless")
        # edge_options.add_argument("--disable-gpu")
        edge_options.add_argument("--remote-debugging-port=9222")
        edge_options.add_experimental_option('prefs', {
            'download.default_directory': download_path,
            'download.prompt_for_download': False,
            'download.directory_upgrade': True,
            'safebrowsing.enabled': True
        })
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)
    driver.implicitly_wait(2)
    driver.maximize_window()
    driver.delete_all_cookies()
    request.cls.driver = driver
    yield
    driver.close()


# HTML Reports
def pytest_html_report_title(report):
    report.title = "Docusign Automation Test Report"

# Helper function to capture screenshots
def capture_screenshot(driver, test_name):
    screenshots_dir = "test_results/screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = os.path.join(screenshots_dir, f"{test_name}_{timestamp}.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved to: {screenshot_path}")


# Hook to capture screenshots on test failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Capture screenshot on test failure
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            test_name = item.name
            capture_screenshot(driver, test_name)
