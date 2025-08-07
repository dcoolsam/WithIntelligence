import pytest
from pages.login_page import LoginPage
from pages.insights_page import InsightsPage
from config.config import Config
from data.messages import LOGIN_ERROR_INVALID_CREDENTIALS


class TestLogin:
    
    def test_valid_login(self, browser_page, take_screenshot):
        """Test Case 1.1: Valid Credentials"""
        login_page = LoginPage(browser_page)
        
        # Navigate to login page
        login_page.navigate()
        
        # login_page.accept_cookies()

        # Login with valid credentials
        login_page.login(Config.USERNAME, Config.PASSWORD)
        
        # Verify redirect to insights page
        assert login_page.check_login_success()
        
    def test_invalid_login(self, browser_page, take_screenshot):
        """Test Case 1.2: Invalid Credentials"""
        login_page = LoginPage(browser_page)
        
        # Navigate to login page
        login_page.navigate()

        login_page.accept_cookies()
        
        # Login with invalid credentials
        login_page.login("invalid@email.com", "wrongpassword")
        
        # Verify error message
        assert LOGIN_ERROR_INVALID_CREDENTIALS in login_page.get_error_message()
