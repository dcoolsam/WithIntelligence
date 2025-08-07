from pages.base_page import BasePage
from config.config import Config

class LoginPage(BasePage):
    # Locators
    EMAIL_INPUT = '[data-testid="login-email"]'
    PASSWORD_INPUT = '[data-testid="login-passwordInput"]'
    LOGIN_BUTTON = '[data-testid="login-submitBtn"]'
    ERROR_MESSAGE = '[data-testid="login-errorMessage"]'
    ACCEPT_COOKIES = {"name": "Accept All Cookies"}


    def navigate(self):
        """Navigate to login page"""
        login_url = f"{Config.BASE_URL}/login"
        self.navigate_to(login_url)
    
    def accept_cookies(self):
        """Accept cookies if popup appears"""
        self.page.wait_for_load_state("networkidle")
        cookie_button = self.page.get_by_role("button", **self.ACCEPT_COOKIES)

        try:
            if cookie_button.is_visible(timeout=300):
                self.log_action("Accepting cookies")
                cookie_button.click()
        except:
            self.log_action("No cookie popup found")
            print("No cookie popup found")
    
    def login(self, username: str, password: str):
        """Perform login"""
        self.accept_cookies()
        self.fill(self.EMAIL_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
    
    def get_error_message(self) -> str:
        """Get error message text"""
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_error_displayed(self) -> bool:
        """Check if error message is displayed"""
        return self.is_visible(self.ERROR_MESSAGE)
    
    def check_login_success(self) -> bool:
        """Check if login was successful by verifying URL"""
        self.page.wait_for_url("**/insights",timeout=30000)
        if "/insights" in self.page.url:
            self.log_action("Login successful, redirected to insights")
            return True
        else:
            self.log_action("Login failed, not redirected to insights")
            return False
        
    def check_login_failure(self) -> bool:
        """Check if login failed by verifying error message"""
        return self.is_error_displayed() and "We didn't recognize the username or password you entered" in self.get_error_message()    