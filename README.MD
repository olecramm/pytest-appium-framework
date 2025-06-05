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

## Allure Report Integration

This project supports [Allure](https://docs.qameta.io/allure/) for advanced test reporting and visualization.

### How to Generate and View Allure Reports

1. **Run your tests to generate Allure results:**
    ```bash
    pytest
    ```

2. **Generate the Allure HTML report:**
    ```bash
    allure generate allure-results -o allure-report --clean
    ```

3. **Open the Allure report in your browser:**
    ```bash
    allure open allure-report
    ```

> **Note:**  
> Make sure you have the [Allure commandline tool](https://docs.qameta.io/allure/#_installing_a_commandline) installed.  
> You can install it via Homebrew (`brew install allure`), Scoop (`scoop install allure`), or download from the [official site](https://github.com/allure-framework/allure2/releases).

The report will be available at [http://localhost:port](http://localhost:port) after running the `allure open` command.

*Automate. Test. Deliver quality Android apps with confidence!*