from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy as By

class ProductView(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    LOCATOR_TXT_PRODUCT_NAME = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("SEIKO SRPB77 Automatic Watch for Men - Presage Cocktail Time - Patterned Silver Dial with Gloss Finish, Date Calendar, 50m Water-Resistant")')
        
    def is_opened(self):
        """Check if the product view is opened by verifying the presence of the product name.
        
        Args:
            model (str): The name of the product to check.
        
        Returns:
            bool: True if the product view is opened, False otherwise.
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