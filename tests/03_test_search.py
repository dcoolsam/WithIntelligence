from email.mime import text
import pytest
from pages.login_page import LoginPage
from pages.insights_page import InsightsPage
from config.config import Config
from data.messages import SearchConstants
from playwright.sync_api import expect
import re
import random

class TestSearch:
    
    def test_valid_search(self, browser_page, take_screenshot):
        """Test Case 3.1: Valid Search Query"""
        # Login first
        login_page = LoginPage(browser_page)
        login_page.navigate()
        login_page.login(Config.USERNAME, Config.PASSWORD)
        
        # Perform search
        insights_page = InsightsPage(browser_page)
        insights_page.search(SearchConstants.VALID_SEARCH_TERM)
        
        #Check no results message
        expect(browser_page.locator("body")).to_contain_text(SearchConstants.VALID_SEARCH_TERM)

    def test_no_search_results(self, browser_page, take_screenshot):
        """Test Case 3.2: No Search Results"""
        # Login first
        login_page = LoginPage(browser_page)
        login_page.navigate()
        login_page.login(Config.USERNAME, Config.PASSWORD)
        
        insights_page = InsightsPage(browser_page)
        
        # Perform search with no results
        insights_page.search(SearchConstants.INVALID_SEARCH_TERM)        

        # Check no results message
        expect(browser_page.locator("body")).to_contain_text(SearchConstants.INVALID_SEARCH_RESULTS_TITLE)

