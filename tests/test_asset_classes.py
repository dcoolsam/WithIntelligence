import pytest
from pages.login_page import LoginPage
from pages.settings_page import SettingsPage
from config.config import Config

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
        
        # Expected asset classes
        expected_classes = [
            'Private Equity', 'Private Credit', 'Real Estate',
            'Infrastructure', 'Public Markets', 'Family Offices'
        ]
        
        # Verify each asset class is checked
        for asset_class in expected_classes:
            assert settings_page.is_asset_class_checked(asset_class), \
                f"Asset class '{asset_class}' should be checked"
        
        # Verify all expected classes are checked
        checked_classes = settings_page.get_checked_asset_classes()
        assert set(checked_classes) == set(expected_classes)