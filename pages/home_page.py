import time
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy as By

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    LOCATOR_VIEW_SEARCH_BOX = (By.ID, 'com.amazon.mShop.android.shopping:id/chrome_search_hint_view')
    LOCATOR_TXT_SEARCH_BOX = (By.ID, 'com.amazon.mShop.android.shopping:id/rs_search_src_text')

    def perform_search(self, query):
        """Open the search box, enter a search query, and simulate pressing the Enter key.
        Args:
            query (str): The search query to enter.
        Note:
            The method uses `press_keycode(66)` to simulate pressing the Enter key, which corresponds to the Android keycode for Enter.
        """
        self.click_search_box(*self.LOCATOR_VIEW_SEARCH_BOX)
        self.enter_search_query(*self.LOCATOR_TXT_SEARCH_BOX, query=query)
        self.driver.press_keycode(66)
        

    def open_product_view(self, model):
        """Navigate to a product by scrolling to it and clicking on it.
        Args:
            model (str): The name of the product to navigate to.
        """
        time.sleep(2)
        self.swipe_to_text(model, self.driver)
