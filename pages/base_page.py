import logging
from datetime import datetime
from playwright.sync_api import Page
from utils.logger import get_logger

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger()

    def log_action(self, action: str):
        """Log test actions"""
        self.logger.info(action)
    
    def navigate_to(self, url: str):
        """Navigate to a specific URL"""
        self.log_action(f"Navigating to: {url}")
        self.page.goto(url)
        self.log_action(f"Successfully navigated to: {url}")
    
    def click(self, selector: str):
        """Click on an element"""
        self.log_action(f"Clicking on: {selector}")
        self.page.click(selector)
        self.log_action(f"Successfully clicked: {selector}")
    
    def fill(self, selector: str, text: str):
        """Fill input field"""
        self.log_action(f"Filling '{selector}' with: {text}")
        self.page.fill(selector, text)
        self.log_action(f"Successfully filled: {selector}")
    
    def get_text(self, selector: str) -> str:
        """Get text from element"""
        self.log_action(f"Getting text from: {selector}")
        text = self.page.text_content(selector)
        self.log_action(f"Retrieved text: {text}")
        return text
    
    def is_visible(self, selector: str) -> bool:
        """Check if element is visible"""
        self.log_action(f"Checking visibility of: {selector}")
        return self.page.is_visible(selector)
    
    def wait_for_element(self, selector: str, timeout: int = 30000):
        """Wait for element to be visible"""
        self.log_action(f"Waiting for element: {selector}")
        self.page.wait_for_selector(selector, timeout=timeout)
        self.log_action(f"Element found: {selector}")

    # def accept_cookies(self, selector: str, timeout: int = 10000):
    #     """Accept cookies by clicking the consent button"""
    #     self.log_action(f"Waiting for cookie accept button: {selector}")
    #     self.page.wait_for_selector(selector, timeout=timeout)
    #     self.log_action(f"Clicking cookie accept button: {selector}")
    #     self.page.click(selector)
    #     self.log_action("Cookies accepted.")

# ...existing code...    