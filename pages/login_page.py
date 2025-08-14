from pages.base_page import BasePage
from config.config import Config
from playwright.sync_api import Page

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Locators
        self.email_input = page.get_by_test_id('login-email')
        self.password_input = page.get_by_test_id('login-passwordInput')
        self.login_button = page.get_by_test_id('login-submitBtn')
        self.error_message = page.get_by_test_id('login-errorMessage')
        self.accept_cookies_button = page.get_by_role("button", name="Accept All Cookies")

    def navigate(self):
        """Navigate to login page"""
        login_url = f"{Config.BASE_URL}/login"
        self.navigate_to(login_url)

    def accept_cookies(self):
        """Accept cookies if popup appears"""
        self.page.wait_for_load_state("networkidle")
        if self.is_visible(self.accept_cookies_button):
            self.log_action("Accepting cookies")
            self.click(self.accept_cookies_button)
        else:
            self.log_action("No cookie popup found")

    def login(self, username: str, password: str):
        """Perform login"""
        self.accept_cookies()
        self.fill(self.email_input, username)
        self.fill(self.password_input, password)
        self.click(self.login_button)

    def get_error_message(self) -> str:
        """Get error message text"""
        return self.get_text(self.error_message)

    def is_error_displayed(self) -> bool:
        """Check if error message is displayed"""
        return self.is_visible(self.error_message)

    def check_login_success(self) -> bool:
        """Check if login was successful by verifying URL"""
        self.page.wait_for_url("**/insights", timeout=30000)
        if "/insights" in self.page.url:
            self.log_action("Login successful, redirected to insights")
            return True
        else:
            self.log_action("Login failed, not redirected to insights")
            return False

    def check_login_failure(self) -> bool:
        """Check if login failed by verifying error message"""
        return self.is_error_displayed() and \
               "We didn't recognize the username or password you entered" in self.get_error_message()
