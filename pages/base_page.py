import logging
from utils.wait_utils import *
from utils.scroll_utils import *

class BasePage:
    
    # constructor to initialize the BasePage with a driver instance
    def __init__(self, driver):
        """
        Initialize the BasePage with a driver instance.
        
        Args:
            driver: The WebDriver instance used to interact with the app's UI elements.
        """
        self.driver = driver
    
    # click the search box to open it
    def click_search_box(self, *locator):
        """Click the search box to open it.
        Args:
            locator (tuple): Locator for the search box element.
        """
        try:
            element = wait_until_clickable(self.driver, locator)
            element.click()
        except Exception as e:
            logging.error(f"Error clicking search box: {e}")
            raise
    
    # def perform_search(self, query):
    def enter_search_query(self, *locator, query):
        """Enter a search query into the search box.
        Args:
            locator (tuple): Locator for the search box element.
            query (str): The search query to enter.
        """
        try:
            element = wait_until_visible(self.driver, locator)
            element.send_keys(query)
        except Exception as e:
            logging.error(f"Error entering search query '{query}': {e}")
            raise
    
    # def swipe_up(self, driver, how_many_times=1):
    def swipe_to_text(self, text, driver):
        """Scroll to an element containing the specified text and click it.
        
        Args:
            text (str): The text to search for in the scrollable view.
            driver: The Appium WebDriver instance.
        """
        try:
            ScrollUtil.scroll_to_text(text, driver)
        except Exception as e:
            logging.error(f"Error scrolling to text '{text}': {e}")
            raise
    
    # check if an element is displayed on the page
    def check_element_displayed(self, *locator): 
        """Check if an element is displayed on the page.
        
        Args:
            locator (tuple): Locator for the element to check.
        
        Returns:
            bool: True if the element is displayed, False otherwise.
        """
        try:
            return wait_until_visible(self.driver, locator).is_displayed()
        except Exception as e:
            logging.warning(f"Element not found or not displayed: {e}")
            return False