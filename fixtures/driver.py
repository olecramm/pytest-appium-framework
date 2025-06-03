from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.devices import DEVICES
from config.env import appium_url
import pytest

# This file contains fixtures for setting up the Appium driver and device configuration for tests.
@pytest.fixture(scope="session")
def device_config(pytestconfig):
    selected = pytestconfig.getoption("device")
    return DEVICES[selected]

# This fixture initializes the Appium driver with the desired capabilities for the specified device.
@pytest.fixture(scope="session")
def appium_driver(device_config):
    desired_caps = device_config
    capabilitiesOptions = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote(appium_url, options=capabilitiesOptions)
    yield driver
    driver.terminate_app('com.amazon.mShop.android.shopping')
    
                              
                              