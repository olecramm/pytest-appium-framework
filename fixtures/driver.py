from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.devices import DEVICES
from config.env import appium_url
import pytest

# This file contains fixtures for setting up the Appium driver and device configuration for tests.
@pytest.fixture(scope="session")
def device_config(pytestconfig):
    """Fixture to retrieve the device configuration based on the selected device.
    Raises ValueError if the selected device is not in the configured devices list.
    """
    # Retrieve the selected device from pytest configuration
    selected_device = pytestconfig.getoption("device")
    
    # Check if the selected device is in the configured devices list
    if selected_device not in DEVICES:
        raise ValueError(f"Device {selected_device} is not in the configured devices list.")
    
    # Return the configuration for the selected device
    return DEVICES[selected_device]

# This fixture initializes the Appium driver with the desired capabilities for the specified device.
@pytest.fixture(scope="session")
def appium_driver(device_config):
    desired_caps = device_config
    capabilitiesOptions = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote(appium_url, options=capabilitiesOptions)
    yield driver
    driver.terminate_app('com.amazon.mShop.android.shopping')
    
                              
                              