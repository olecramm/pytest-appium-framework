# Pytest Appium Framework

A robust, maintainable test automation framework for Android apps using [Pytest](https://pytest.org/) and [Appium](https://appium.io/). This project follows the Page Object Model (POM) pattern for clear separation of test logic and UI interactions.

## Features

- **Pytest-based**: Simple, powerful test discovery and execution.
- **Appium-powered**: Automates real Android devices or emulators.
- **Page Object Model**: Clean, reusable code for UI interactions.
- **Fixtures**: Easy driver and device setup with Pytest fixtures.
- **End-to-End Tests**: Example tests for search and product view flows.

## Project Structure

```
pytest-appium-framework/
├── config/           # Device and environment configuration
├── fixtures/         # Pytest fixtures for driver and device setup
├── pages/            # Page Object Model classes
├── tests/            # Test cases
├── utils/            # Utility functions (waits, scrolling, etc.)
```

## Example Test

```python
def test_search_box(home_page, product_view):
    query = "Seiko"
    model = "Presage Cocktail Time"
    home_page.perform_search(query)
    home_page.open_product_view(model)
    assert product_view.is_opened()
```

## Getting Started

1. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2. **Configure devices and environment:**
    - Edit files in `config/` as needed.

3. **Run tests:**
    ```bash
    pytest
    ```

## Requirements

- Python 3.7+
- Appium server running
- Android device or emulator

*Automate. Test. Deliver quality Android apps with confidence!*