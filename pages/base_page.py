import logging
from utils.wait_utils import *
from utils.scroll_utils import *
from utils.logger import setup_logger

class BasePage:
    
    # constructor to initialize the BasePage with a driver instance
    def __init__(self, driver):
        """
        Initialize the BasePage with a driver instance.
        
        Args:
            driver: The WebDriver instance used to interact with the app's UI elements.
        """
        self.driver = driver
    
    logger = setup_logger(__name__)
    
    # click the search box to open it
    def click_search_box(self, *locator):
        """Click the search box to open it.
        Args:
            locator (tuple): Locator for the search box element.
        """
        
        try:
            element = wait_until_clickable(self.driver, locator)
            element.click()
            self.logger.info(f"Clicked on search box with locator: {locator}")
        except Exception as e:
            raise RuntimeError(f"Error clicking search box: {e}")
    
    # def perform_search(self, query):
    def enter_search_query(self, *locator, query):
        """Enter a search query into the search box.
        Args:
            locator (tuple): Locator for the search box element.
            query (str): The search query to enter.
        """
        try:
            print(f"Entering search query: {query}")
            element = wait_until_visible(self.driver, locator)
            self.logger.info(f"Entering search query: {query}")
            element.send_keys(query)
        except Exception as e:
            raise RuntimeError(f"Error entering search query '{query}': {e}")
    # scroll to an element specified by the locator and click it
    def swipe_to_product_item(self, driver, *locator):
        try:
            ScrollUtil.swipe_to_element(self, driver, *locator)
        except Exception as e:
            raise RuntimeError(f"Error swiping to product item: {e}")
    
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