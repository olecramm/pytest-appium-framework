import time
import allure
# import pytest

@allure.feature("E2E Tests")
@allure.story("Search Box Functionality")
@allure.title("Test Search Box Opens Product View")
@allure.description("This test verifies that the search box opens the product view for a specific product when searched.")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("e2e", "search", "product_view")
def test_search_box_opens_product_view(home_page, product_view, logger):
    """Test the search box functionality by performing a search for 'Seiko'."""
    #Arrange
    SEIKO_QUERY = "seiko"
    PRESAGE_MODEL = "Presage"
    
    #Act
    logger.info(f"Step 1: Performing search for '{SEIKO_QUERY}' and opening product view for '{PRESAGE_MODEL}'.")
    home_page.perform_search(SEIKO_QUERY)
    
    logger.info(f"Step 2: Opening product view for '{PRESAGE_MODEL}'.")
    home_page.open_product_view()
    
    logger.info(f"Step 3: Checking if product view for '{PRESAGE_MODEL}' is opened.")
    resp = product_view.is_opened()
    
    #Assert
    logger.info(f"Step 4: Product view for '{PRESAGE_MODEL}' is opened: {resp}.")
    assert resp is True, f"Product view for '{PRESAGE_MODEL}' is not opened."
    
    #only for debugging purposes
    time.sleep(5)
    
@allure.feature("E2E Tests")
@allure.story("Product Name Retrieval")
@allure.title("Test Product Name Retrieval")
@allure.description("This test verifies that the product name can be retrieved correctly from the product view.")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("e2e", "product_view", "name_retrieval")
#@pytest.mark.skip
def test_product_name(product_view, logger):
    """Test the product name retrieval functionality."""
    # Arrange
    expected_product_name = "Presage"
    
    # Act
    logger.info(f"Step 5: Retrieving product name for '{expected_product_name}'.")
    actual_product_name = product_view.get_product_name()
    
    # Assert
    logger.info(f"Step 6: Actual product name retrieved: '{actual_product_name}'.")
    assert expected_product_name in actual_product_name, \
    f"Expected product name '{expected_product_name}' not found in actual product name '{actual_product_name}'."
    
    logger.info("Step 7: Product name retrieval test passed.")
    
    # only for debugging purposes
    time.sleep(5)
    
@allure.feature("E2E Tests")
@allure.story("Allure Skip Category")
@allure.title("Test Allure Skip Category")
@allure.description("This test is intentionally skipped to demonstrate the allure skip category functionality.")
@allure.severity(allure.severity_level.MINOR)
@allure.tag("e2e", "skip", "allure_skip_category")
@allure.label("category", "Critical defects")
# @pytest.mark.skip(reason="Skipping this test to demonstrate allure skip category.")
def test_e2e_testing_alure_skip_category():
    """Test to verify that the allure skip category is working."""
    # This test is intentionally left empty to demonstrate the allure skip category.
    pass
