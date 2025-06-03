import time

# Test the search box functionality by performing a search for 'Seiko' and verifying the product view opens correctly.
def test_search_box_opens_product_view(home_page, product_view):
    """Test the search box functionality by performing a search for 'Seiko'."""
    #Arrange
    SEIKO_QUERY = "Seiko"
    PRESAGE_MODEL = "Presage Cocktail Time"
    
    #Act
    home_page.perform_search(SEIKO_QUERY)
    home_page.open_product_view(PRESAGE_MODEL)
    resp = product_view.is_opened()
    
    #Assert
    assert resp == True, f"Product view for '{PRESAGE_MODEL}' is not opened."
    
    #only for debugging purposes
    time.sleep(5)
    
# Test the product name retrieval functionality
def test_product_name(product_view):
    """Test the product name retrieval functionality."""
    # Arrange
    expected_product_name = "Presage Cocktail Time"
    
    # Act
    actual_product_name = product_view.get_product_name()
    
    # Assert
    assert expected_product_name in actual_product_name, \
    f"Expected product name '{expected_product_name}' not found in actual product name '{actual_product_name}'."
    
    # only for debugging purposes
    time.sleep(5)
