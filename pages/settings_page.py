from pages.base_page import BasePage
from config.config import Config

class SettingsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Locators
        self.private_equity_section = page.get_by_text("Profile pages")

    def navigate(self):
        """Navigate to settings page"""
        # Wait for login to complete before moving to settings
        self.page.wait_for_url(f"{Config.BASE_URL}/insights", timeout=20000)

        # Load Settings page
        settings_url = f"{Config.BASE_URL}/account/settings"
        self.navigate_to(settings_url)

    def is_checkbox_checked(self, checkbox_label: str) -> bool:
        """Check if a specific checkbox is checked"""
        # Scope locator to the 'Profile pages' section
        checkbox = self.private_equity_section.locator("..").get_by_label(checkbox_label)
        if checkbox:
            return checkbox.is_checked()
        return False
