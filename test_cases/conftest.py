import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def Setup(browser):
    if browser == "Chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome browser....")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox browser....")
    else:
        driver = webdriver.Chrome()

    return driver

def pytest_addoption(parser):           # This will get value from CLI/hooks
    parser.addoption("--browser")       # Whatever browser name will pass in Command promt this method will get it

@pytest.fixture()
def browser(request):       # This will return given browser value to setup method
    return request.config.getoption("--browser")


############### pytest html reports  ######################

# it is hook for adding environment info to HTML report

def pytest_configure(config):    ## Below info will be populated in reports
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Amol'

# It is hook for delete/Modify Environment info to HTML report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

