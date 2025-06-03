# This file contains the configuration for devices used in Appium tests.
# It includes device names, platform versions, and other necessary parameters.

DEVICES = {
    "RQ8R703W2AB": {
      "platformName": "Android",
      "appium:platformVersion": "13",
      "appium:deviceName": "Samsung Galaxy S20 FE",
      "appium:udid": "RQ8R703W2AB",
      "appium:automationName": "UiAutomator2",
      "appium:appPackage": "com.amazon.mShop.android.shopping",
      "appium:appActivity": "com.amazon.mShop.home.HomeActivity",
      "appium:noReset": True
    },
    "Pixel6a": {
      "platformName": "Android",
      "appium:platformVersion": "16",
      "appium:deviceName": "sdk_gphone64_x86_64",
      "appium:udid": "emulator-5554",
      "appium:automationName": "UiAutomator2",
      "appium:appPackage": "com.amazon.mShop.android.shopping",
      "appium:appActivity": "com.amazon.mShop.home.HomeActivity",
      "appium:noReset": True
    }
}