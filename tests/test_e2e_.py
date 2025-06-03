import time

# Test the search box functionality by performing a search for 'Seiko' and verifying the product view opens correctly.
def test_search_box(home_page, product_view):
    """Test the search box functionality by performing a search for 'Seiko'."""
    
    query = "Seiko"
    model = "Presage Cocktail Time"
    
    home_page.perform_search(query)
    home_page.open_product_view(model)
    resp = product_view.is_opened()
    assert resp == True, f"Product view for '{model}' is not opened."
    time.sleep(5)
    
# Test the product name retrieval functionality
def test_product_name(product_view):
    """Test the product name retrieval functionality."""
    
    expected_product_name = "Presage Cocktail Time"
    
    actual_product_name = product_view.get_product_name()
    
    assert expected_product_name in actual_product_name, f"Expected product name '{expected_product_name}' not found in actual product name '{actual_product_name}'."
    time.sleep(5)
