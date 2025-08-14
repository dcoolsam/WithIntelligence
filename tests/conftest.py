import pytest
import logging
import os
from datetime import datetime
import datetime
from playwright.sync_api import sync_playwright
from config.config import Config
from utils.logger import get_logger


# @pytest.fixture(scope="session", autouse=True)
# def setup_logging():
#     """Ensure logger is initialized at session start"""
#     logger = get_logger()
#     logger.info("Test session started")
#     return logger

@pytest.fixture(scope="function")
def browser_page(request):
    with sync_playwright() as p:
        browser = p[Config.BROWSER].launch(headless=Config.HEADLESS)
        context = browser.new_context()
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
        page.set_default_timeout(Config.DEFAULT_TIMEOUT)

        yield page  # only yield page, keep tests unchanged

        # Stop tracing after test
        os.makedirs("traces", exist_ok=True)
        test_name = request.node.name
        context.tracing.stop(path=f"traces/{test_name}.zip")

        context.close()
        browser.close()

@pytest.fixture(scope="function")
def take_screenshot(browser_page, request):
    """Take screenshot on test failure"""
    yield
    
    if request.node.rep_call.failed:
        # Create screenshots directory
        os.makedirs(Config.SCREENSHOT_PATH, exist_ok=True)
        
        # Generate screenshot filename
        test_name = request.node.name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(
            Config.SCREENSHOT_PATH, 
            f"{test_name}_{timestamp}.png"
        )
        
        # Take screenshot
        browser_page.screenshot(path=screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture test results for screenshot fixture"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

def pytest_configure(config):
    if not config.option.htmlpath: #if not defined in pytest.in
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        config.option.htmlpath = f"reporting/report_{timestamp}.html"