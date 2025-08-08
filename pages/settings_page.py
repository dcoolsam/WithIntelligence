from pages.base_page import BasePage

class SettingsPage(BasePage):
    # Locators
    ASSET_CLASSES_SECTION = '.profile-pages, .asset-classes'
    PRIVATE_EQUITY_CHECKBOX = 'input[value="Private Equity"], input[name*="private-equity"]'
    PRIVATE_CREDIT_CHECKBOX = 'input[value="Private Credit"], input[name*="private-credit"]'
    REAL_ESTATE_CHECKBOX = 'input[value="Real Estate"], input[name*="real-estate"]'
    INFRASTRUCTURE_CHECKBOX = 'input[value="Infrastructure"], input[name*="infrastructure"]'
    PUBLIC_MARKETS_CHECKBOX = 'input[value="Public Markets"], input[name*="public-markets"]'
    FAMILY_OFFICES_CHECKBOX = 'input[value="Family Offices"], input[name*="family-offices"]'
    
    def navigate(self):
        """Navigate to settings page"""
        from config.config import Config
        
        # Let Login complete before moving to settings 
        self.page.wait_for_url(f"{Config.BASE_URL}/insights", timeout=20000)  # waits up to 20 seconds
        
        #Load Settings
        settings_url = f"{Config.BASE_URL}/account/settings"
        self.navigate_to(settings_url)
    
    # def is_asset_class_checked(self, asset_class: str) -> bool:
    #     """Check if specific asset class is checked"""
    #     checkbox_map = {
    #         'Private Equity': self.PRIVATE_EQUITY_CHECKBOX,
    #         'Private Credit': self.PRIVATE_CREDIT_CHECKBOX,
    #         'Real Estate': self.REAL_ESTATE_CHECKBOX,
    #         'Infrastructure': self.INFRASTRUCTURE_CHECKBOX,
    #         'Public Markets': self.PUBLIC_MARKETS_CHECKBOX,
    #         'Family Offices': self.FAMILY_OFFICES_CHECKBOX
    #     }
        
    #     checkbox_selector = checkbox_map.get(asset_class)
    #     if checkbox_selector:
    #         return self.page.is_checked(checkbox_selector)
    #     return False
    
    # def get_checked_asset_classes(self) -> list:
    #     """Get list of all checked asset classes"""
    #     asset_classes = [
    #         'Private Equity', 'Private Credit', 'Real Estate',
    #         'Infrastructure', 'Public Markets', 'Family Offices'
    #     ]
        
    #     checked_classes = []
    #     for asset_class in asset_classes:
    #         if self.is_asset_class_checked(asset_class):
    #             checked_classes.append(asset_class)
        
    #     return checked_classes

    def is_checkbox_checked(self, checkbox_label: str) -> bool:
        """Check if a specific checkbox is checked"""
        # Locate the container/div that has text 'Profile pages'

        checkbox = self.page.get_by_label(checkbox_label).first
        if checkbox:
            # print(f"Checkbox with label '{checkbox_label}'  found")
            return checkbox.is_checked()

