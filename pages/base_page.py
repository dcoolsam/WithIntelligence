import logging
from playwright.sync_api import Page, Locator
import re
from utils.logger import get_logger

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger()

    def log_action(self, action: str):
        self.logger.info(action)

    def selector_string(self, locator: Locator) -> str:
        """Extract just the selector string from a Playwright Locator object."""
        match = re.search(r"selector='([^']+)'", str(locator))
        return match.group(1) if match else "<unknown selector>"

    def navigate_to(self, url: str):
        self.log_action(f"Navigating to: {url}")
        self.page.goto(url)
        self.log_action(f"Successfully navigated to: {url}")

    def click(self, locator: Locator):
        locator_text = self.selector_string(locator)
        self.log_action(f"Clicking on: {locator_text}")
        locator.click()
        self.log_action(f"Successfully clicked: {locator_text}")

    def fill(self, locator: Locator, text: str):
        locator_text = self.selector_string(locator)
        self.log_action(f"Filling {locator_text} with: {text}")
        locator.fill(text)
        self.log_action(f"Successfully filled: {locator_text}")

    def get_text(self, locator: Locator) -> str:
        locator_text = self.selector_string(locator)
        self.log_action(f"Getting text from: {locator_text}")
        text = locator.text_content()
        self.log_action(f"Retrieved text: {text}")
        return text

    def is_visible(self, locator: Locator) -> bool:
        locator_text = self.selector_string(locator)
        self.log_action(f"Checking visibility of: {locator_text}")
        return locator.is_visible()

    def wait_for_element(self, locator: Locator, timeout: int = 30000):
        locator_text = self.selector_string(locator)
        self.log_action(f"Waiting for element: {locator_text}")
        locator.wait_for(timeout=timeout)
        self.log_action(f"Element found: {locator_text}")
