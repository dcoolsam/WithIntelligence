import pytest
from pages.login_page import LoginPage
from pages.settings_page import SettingsPage
from config.config import Config
from data.messages import SettingsConstants

class TestAssetClasses:
    
    def test_verify_asset_classes(self, browser_page, take_screenshot):
        """Scenario 4: Verify Asset Classes"""
        # Login
        login_page = LoginPage(browser_page)
        login_page.navigate()
        login_page.login(Config.USERNAME, Config.PASSWORD)
        
        # Navigate to settings
        settings_page = SettingsPage(browser_page)
        settings_page.navigate()
        
        # Verify each expected asset class is checked
        for asset_class in SettingsConstants.EXPECTED_CLASSES:
            assert settings_page.is_checkbox_checked(asset_class), f"{asset_class} checkbox is not checked"
