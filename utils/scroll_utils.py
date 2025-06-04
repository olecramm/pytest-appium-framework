from appium.webdriver.common.appiumby import AppiumBy as By
from utils.logger import setup_logger

class ScrollUtil:

    # Scrolls to an element containing the specified text and clicks it.
    # Uses UiScrollable to find the element in a scrollable view.
    # This method is specifically for Android devices using UiAutomator2.
    
    logger = setup_logger(__name__)
    
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
    def swipe_up(self, driver, how_many_times=1):
        """
        Swipes up on the screen a specified number of times.
        :param driver: The Appium WebDriver instance.
        :param how_many_times: The number of times to swipe up.
        """
        for i in range(how_many_times):
            driver.swipe(609, 1624, 609, 680, 1000)

    @staticmethod
    def swipe_to_element(self, driver, *locator):
        """
        Scrolls to an element specified by the locator and clicks it.
        :param driver: The Appium WebDriver instance.
        :param locator: The locator tuple for the element to scroll to.
        """
        # Get screen size
        window_size = driver.get_window_size()
        width = window_size['width']
        height = window_size['height']
        
        start_x = width // 2    # Calculate swipe start and end points
        start_y = int(height * 0.7)   # Start below the carousel
        end_y = int(height * 0.3)     # Scroll upward
        
        # Find the element using the locator
        element = driver.find_elements(*locator)
        
        while len(element) == 0:
            
            # Perform the swipe
            ScrollUtil.logger.info(f"Swiping from ({start_x}, {start_y}) to ({start_x}, {end_y}) to find element: {locator}")
            driver.swipe(start_x, start_y, start_x, end_y, 1000)
            
            element = driver.find_elements(*locator)
            
            # Check if the element is now displayed
            if element is not None and len(element) > 0:
                ScrollUtil.logger.info(f"Element found: {element[0].text}")
                element[0].click()
                ScrollUtil.logger.info(f"Clicked on element with text: {element[0].text}")
                break

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
            
