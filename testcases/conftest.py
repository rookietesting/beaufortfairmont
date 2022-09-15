import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
#
#pytest --browser chrome --url http://inv.beaufortfairmont.com


@pytest.fixture(autouse=True)
def setup(request, browser, url):
    if browser == "chrome":
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")

@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")




