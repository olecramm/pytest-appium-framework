# Pytest Appium Framework

A robust, maintainable test automation framework for Android apps using [Pytest](https://pytest.org/) and [Appium](https://appium.io/). This project follows the Page Object Model (POM) pattern for clear separation of test logic and UI interactions.

## Features

- **Pytest-based**: Simple, powerful test discovery and execution.
- **Appium-powered**: Automates real Android devices or emulators.
- **Page Object Model**: Clean, reusable code for UI interactions.
- **Fixtures**: Easy driver, device, and logger setup with Pytest fixtures.
- **End-to-End Tests**: Example tests for search and product view flows.
- **Logging**: Session-based logging to both console and file.

## Project Structure

```
pytest-appium-framework/
├── config/           # Device and environment configuration
├── fixtures/         # Pytest fixtures for driver, pages, and logger
├── pages/            # Page Object Model classes
├── tests/            # Test cases
├── utils/            # Utility functions (waits, scrolling, logging, etc.)
├── logs/             # Log files
├── requirements.txt  # Python dependencies
├── pytest.ini        # Pytest configuration
```

## Example Test

```python
def test_search_box_opens_product_view(home_page, product_view, logger):
    query = "seiko"
    home_page.perform_search(query)
    home_page.open_product_view()
    assert product_view.is_opened()
```

## Getting Started

1. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2. **Configure devices and environment:**
    - Edit files in `config/` as needed.
    - Set your Appium server URL in `.env.qa` or `.env.example`.

3. **Run tests:**
    ```bash
    pytest
    ```

    To specify a device:
    ```bash
    pytest --device=<DEVICE_NAME>
    ```

## Requirements

- Python 3.7+
- Appium server running
- Android device or emulator

## Environment Variables

Copy `.env.example` to `.env.qa` and set your Appium server URL:

```
APPIUM_SERVER_URL=http://0.0.0.0:4723
```

*Automate. Test. Deliver quality Android apps with confidence!*