from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy as By

class ProductView(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    LOCATOR_TXT_PRODUCT_NAME = (By.XPATH, "//android.view.View[contains(@text, 'SEIKO SRPB77')]")
        
    def is_opened(self):
        """Check if the product view is opened by verifying if the product name is displayed.
        Returns:
            bool: True if the product name is displayed, otherwise False.
        """
        return self.check_element_displayed(*self.LOCATOR_TXT_PRODUCT_NAME)
    
    def get_product_name(self):
        """Get the name of the product displayed in the product view.
        
        Returns:
            str: The name of the product if it is displayed, otherwise an empty string.
        """
        try:
            element = self.driver.find_element(*self.LOCATOR_TXT_PRODUCT_NAME)
            return element.text
        except Exception as e:
            print(f"Error retrieving product name: {e}")
            return ""