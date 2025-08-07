import pytest
from pages.login_page import LoginPage
from pages.insights_page import InsightsPage
from config.config import Config

class TestSearch:
    
    def test_valid_search(self, browser_page, take_screenshot):
        """Test Case 3.1: Valid Search Query"""
        # Login first
        login_page = LoginPage(browser_page)
        login_page.navigate()
        login_page.login(Config.USERNAME, Config.PASSWORD)
        
        # Perform search
        insights_page = InsightsPage(browser_page)
        insights_page.search("Investors")
        
        # Verify search results
        results_title = insights_page.get_search_results_title()
        assert "Displaying results for 'Investors'" in results_title
        assert insights_page.has_search_results()
    
    def test_no_search_results(self, browser_page, take_screenshot):
        """Test Case 3.2: No Search Results"""
        # Login first
        login_page = LoginPage(browser_page)
        login_page.navigate()
        login_page.login(Config.USERNAME, Config.PASSWORD)
        
        # Perform search with no results
        insights_page = InsightsPage(browser_page)
        insights_page.search("abcdefghihgfedcba")
        
        # Verify no results message
        no_results_message = insights_page.get_no_results_message()
        assert "Your search for 'abcdefghihgfedcba' did not match any documents" in no_results_message