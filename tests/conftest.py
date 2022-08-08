import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--lang', action='store', default="ru",
                     help="Choose language to use")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    lang = request.config.getoption("lang")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': lang})
    browser = None
    if(browser_name == 'chrome'):
        browser = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    elif(browser_name == 'firefox'):
        browser = webdriver.Firefox(options=options, service=Service(GeckoDriverManager().install()))
    else:
        raise pytest.UsageError("Для данного браузера не настроена конфигурация")
    yield browser
    browser.quit()