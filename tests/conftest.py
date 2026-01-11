import os
import pytest
import allure
from pathlib import Path
from dotenv import load_dotenv

# load .env from repo root; don't override real environment variables
load_dotenv(dotenv_path=Path(__file__).resolve().parents[1] / ".env", override=False)

@pytest.fixture(scope="session")
def base_url():
    # read at fixture time so CI/CLI env overrides work
    return os.getenv("BASE_URL", "https://example.com")



@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # attach screenshot on failure
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            img = page.screenshot()
            allure.attach(img, name="screenshot", attachment_type=allure.attachment_type.PNG)