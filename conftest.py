import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver_path = "/home/m3chanix/Downloads/drivers"

def pytest_addoption(parser):
    parser.addoption("--browser", default="firefox")
    parser.addoption("--url", default="http://192.168.0.190:8081/")
    parser.addoption("--headless", action="store_true")

def get_driver(browser, headless):

    if browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.headless = headless
        service = Service(executable_path=f"{driver_path}/geckodriver")
        driver = webdriver.Firefox(service=service, options=options)

    elif browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.headless = headless
        service = Service(executable_path=f"{driver_path}/chromedriver")
        driver = webdriver.Chrome(service=service, options=options)

    elif browser == 'opera':
        options = webdriver.ChromeOptions()
        options.headless = headless
        service = Service(executable_path=f"{driver_path}/operadriver")
        driver = webdriver.Chrome(service=service, options=options)

    else:
        raise Exception('Driver not supported')

    return driver

@pytest.fixture(scope='module')
def driver(request):
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")
    
    driver = get_driver(browser, headless)
    driver.base_url = base_url

    request.addfinalizer(driver.quit)

    return driver



