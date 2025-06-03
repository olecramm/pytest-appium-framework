from appium.webdriver.common.appiumby import AppiumBy as By

class ScrollUtil:

    # Scrolls to an element containing the specified text and clicks it.
    # Uses UiScrollable to find the element in a scrollable view.
    # This method is specifically for Android devices using UiAutomator2.
    @staticmethod
    def scroll_to_text(text, driver):
        """
        Scrolls to an element containing the specified text and clicks it.
        Uses UiScrollable to find the element in a scrollable view.
        This method is specifically for Android devices using UiAutomator2.
        :param text: The text to search for in the scrollable view.
        :param driver: The Appium WebDriver instance.
        """
        driver.find_element(By.ANDROID_UIAUTOMATOR, \
            f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("{text}").instance(0))').click()

    @staticmethod
    def swipe_up(driver, how_many_times=1):
        """
        Swipes up on the screen a specified number of times.
        :param driver: The Appium WebDriver instance.
        :param how_many_times: The number of times to swipe up.
        """
        for i in range(how_many_times):
            driver.swipe(609, 1624, 609, 680, 1000)

    @staticmethod
    def swipe_down(driver, how_many_times=1):
        """
        Swipes down on the screen a specified number of times.
        :param driver: The Appium WebDriver instance.
        :param how_many_times: The number of times to swipe down.
        """
        for i in range(how_many_times):
            driver.swipe(540, 440, 620, 1640, 1000)

    @staticmethod
    def swipe_left(driver, how_many_times=1):
        """
        Swipes left on the screen a specified number of times.
        :param driver: The Appium WebDriver instance.
        :param how_many_times: The number of times to swipe left.
        """
        for i in range(how_many_times):
            driver.swipe(115,1700,960,1700,1000)

    @staticmethod
    def swipe_right(driver, how_many_times=1):
        """
        Swipes right on the screen a specified number of times.
        :param driver: The Appium WebDriver instance.
        :param how_many_times: The number of times to swipe right.
        """
        for i in range(how_many_times):
            driver.swipe(960, 1700, 115, 1700, 1000)