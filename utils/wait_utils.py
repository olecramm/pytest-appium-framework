from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@staticmethod
def wait_until_visible(driver, locator, timeout=10):
    """Wait until an element is visible on the page.
    
    Args:
        driver: The WebDriver instance used to interact with the app's UI elements.
        locator (tuple): Locator for the element to wait for.
        timeout (int): Maximum time to wait for the element to become visible.
        
    Returns:
        WebElement: The visible element if found within the timeout period.
    """
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))

@staticmethod
def wait_until_clickable(driver, locator, timeout=10):
    """Wait until an element is clickable on the page.
    
    Args:
        driver: The WebDriver instance used to interact with the app's UI elements.
        locator (tuple): Locator for the element to wait for.
        timeout (int): Maximum time to wait for the element to become clickable.
        
    Returns:
        WebElement: The clickable element if found within the timeout period.
    """
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))