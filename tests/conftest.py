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
    parser.addoption("--browser", action="store", default="edge")


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
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.manager.showWhenStarting", False)
        options.set_preference("signon.management.page.os-authKeystore", False)
        options.set_preference("browser.download.dir", download_path)
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    elif browser == "edge":
        download_path = os.path.abspath(constants.download_path)
        edge_options = webdriver.EdgeOptions()
        edge_options.add_experimental_option('prefs', {
            'download.default_directory': download_path,
            'download.prompt_for_download': False,
            'download.directory_upgrade': True,
            ' safebrowsing.enabled': True
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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    html = None
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    #extra = getattr(report, "extra", [])
    if report.when == "call" or report.when == "test_setup":
        # adding url to report
        # extra.append(pytest_html.extras.url(os.path.abspath(constants.screenshots_path)))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            driver = item.funcargs.get('driver', None)
            if driver is not None:
                utils = Util_Test(driver)
                file_name = "/failed.png"
                utils.getscreenshot(file_name)
                filename = os.path.abspath(Util_Test.folder_path) + file_name
                if file_name:
                    html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % filename
                #extra.append(pytest_html.extras.html(html))

       # report.extra = extra

#
# # It is Hook for adding environment info to HTML reports
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'Docusign'
#     config._metadata['Run User'] = os.environ.get('TriggeringUser', 'Unknown')
#     config._metadata['UTC Time'] = datetime.now(pytz.UTC)
#
#
# # It is Hook for delete/modify environment info to HTML report
# def pytest_metadata(metadata):
#     metadata.pop("Packages", None)
#     metadata.pop("Plugins", None)
#     metadata.pop("Python", None)
