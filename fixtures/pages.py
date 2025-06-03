import pytest
from pages.home_page import HomePage
from pages.product_view import ProductView

@pytest.fixture
def home_page(appium_driver):
    return HomePage(driver=appium_driver)

@pytest.fixture
def product_view(appium_driver):
    return ProductView(driver=appium_driver)