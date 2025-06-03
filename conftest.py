from fixtures.driver import appium_driver, device_config
from fixtures.pages import home_page, product_view

def pytest_addoption(parser):
    parser.addoption("--device", 
                     action="store", 
                     default="RQ8R703W2AB", 
                     help="Device name from config")