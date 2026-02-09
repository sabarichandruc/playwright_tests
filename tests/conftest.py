import os
import pytest
import allure
from pathlib import Path
import sys

# Add parent directory to path to import config
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.config import Config

# Initialize config and display settings
Config.display_config()


@pytest.fixture(scope="session")
def base_url():
    """Get base URL from config"""
    return Config.BASE_URL


@pytest.fixture(scope="session")
def default_timeout():
    """Get default timeout from config"""
    return Config.DEFAULT_TIMEOUT


@pytest.fixture(scope="session")
def config():
    """Get config object for use in tests"""
    return Config


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Attach screenshot on failure"""
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page and Config.SCREENSHOT_ON_FAILURE:
            img = page.screenshot()
            allure.attach(img, name="screenshot", attachment_type=allure.attachment_type.PNG)