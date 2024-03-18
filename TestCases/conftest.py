import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from Config.config import TestData


# This function adds command line options --browser and --headless
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser choice")
    parser.addoption("--headless", action="store_true", default="headed", help="Run in headless mode")


''' Function Scope '''


@pytest.fixture(scope='class')
def init_driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    driver = None
    if browser == 'chrome':
        if headless:
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument('--window-size=1920,1080')
        service_chrome = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service_chrome)
    if browser == "firefox":
        if headless:
            firefox_options = FirefoxOptions()
            firefox_options.add_argument("--headless")
            firefox_options.add_argument('--window-size=1920,1080')
        service_firefox = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service_firefox)
    if browser == "edge":
        if headless:
            edge_options = EdgeOptions()
            edge_options.use_chromium = True  # This is needed to support --headless
            edge_options.add_argument("--headless")
            edge_options.add_argument('--window-size=1920,1080')
        service_edge = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service_edge)
    driver.set_page_load_timeout(30)
    request.cls.driver = driver
    driver.maximize_window()
    driver.get(TestData.BASE_URL)

    yield request.cls.driver
    request.cls.driver.quit()
