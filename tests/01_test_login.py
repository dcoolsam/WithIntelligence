import pytest
from pages.login_page import LoginPage
from pages.insights_page import InsightsPage
from config.config import Config
from data.messages import LoginConstants


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
        login_page.login(LoginConstants.INVALID_USERNAME, LoginConstants.INVALID_PASSWORD)

        # Verify error message
        assert LoginConstants.LOGIN_ERROR_INVALID_CREDENTIALS in login_page.get_error_message()
