import pytest
from pages.insights_page import InsightsPage
from pages.explore_page import ExplorePage
from pages.login_page import LoginPage
from config.config import Config

class TestNavigation:
    
    def test_explore_navigation(self, browser_page, take_screenshot):
        """Scenario 2: Navigation and Links"""
        # Login first
        login_page = LoginPage(browser_page)
        login_page.navigate()
        login_page.login(Config.USERNAME, Config.PASSWORD)
        
        # Navigate to insights and click explore
        insights_page = InsightsPage(browser_page)
        insights_page.click_explore_link()
        
        # Verify explore page loaded
        explore_page = ExplorePage(browser_page)
        assert explore_page.is_loaded()
        assert f"{Config.BASE_URL}/explore" == browser_page.url