import time

# Test the search box functionality by performing a search for 'Seiko' and verifying the product view opens correctly.
def test_search_box_opens_product_view(home_page, product_view, logger):
    """Test the search box functionality by performing a search for 'Seiko'."""
    #Arrange
    SEIKO_QUERY = "Seiko"
    PRESAGE_MODEL = "Presage Cocktail Time"
    
    #Act
    logger.info(f"Step 1: Performing search for '{SEIKO_QUERY}' and opening product view for '{PRESAGE_MODEL}'.")
    home_page.perform_search(SEIKO_QUERY)
    
    logger.info(f"Step 2: Opening product view for '{PRESAGE_MODEL}'.")
    home_page.open_product_view(PRESAGE_MODEL)
    
    logger.info(f"Step 3: Checking if product view for '{PRESAGE_MODEL}' is opened.")
    resp = product_view.is_opened()
    
    #Assert
    logger.info(f"Step 4: Product view for '{PRESAGE_MODEL}' is opened: {resp}.")
    assert resp == True, f"Product view for '{PRESAGE_MODEL}' is not opened."
    
    #only for debugging purposes
    time.sleep(5)
    
# Test the product name retrieval functionality
def test_product_name(product_view, logger):
    """Test the product name retrieval functionality."""
    # Arrange
    expected_product_name = "Presage Cocktail Time"
    
    # Act
    logger.info(f"Step 1: Retrieving product name for '{expected_product_name}'.")
    actual_product_name = product_view.get_product_name()
    
    # Assert
    logger.info(f"Step 2: Actual product name retrieved: '{actual_product_name}'.")
    assert expected_product_name in actual_product_name, \
    f"Expected product name '{expected_product_name}' not found in actual product name '{actual_product_name}'."
    
    logger.info("Step 3: Product name retrieval test passed.")
    
    # only for debugging purposes
    time.sleep(5)
