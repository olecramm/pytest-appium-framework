import pytest
from utils.logger import setup_logger

@pytest.fixture(scope="session", autouse=True)
def logger():
    logger = setup_logger()
    logger.info("=== Pytest Session Started ===")
    yield logger
    logger.info("=== Pytest Session Finished ===")
