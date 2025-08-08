from pages.base_page import BasePage

class SettingsPage(BasePage):
    # Locators
    PRIVATE_EQUITY_CHECKBOX = "text=Profile pages"

    def navigate(self):
        """Navigate to settings page"""
        from config.config import Config
        
        # Let Login complete before moving to settings 
        self.page.wait_for_url(f"{Config.BASE_URL}/insights", timeout=20000)  # waits up to 20 seconds
        
        #Load Settings
        settings_url = f"{Config.BASE_URL}/account/settings"
        self.navigate_to(settings_url)
    
    def is_checkbox_checked(self, checkbox_label: str) -> bool:
        """Check if a specific checkbox is checked"""
        # Scope locator to the 'Profile pages' section
        profile_section = self.page.locator(self.PRIVATE_EQUITY_CHECKBOX).locator("..") 
        checkbox = profile_section.get_by_label(checkbox_label)
        if checkbox:
            # print(f"Checkbox with label '{checkbox_label}'  found")
            return checkbox.is_checked()

