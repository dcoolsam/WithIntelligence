# Login Constants
class LoginConstants:
    LOGIN_ERROR_INVALID_CREDENTIALS = "We didn't recognize the username or password you entered"
    LOGIN_SUCCESS_URL = "**/insights"
    INVALID_USERNAME = "invalid@email.com"
    INVALID_PASSWORD = "wrongpassword"

# Search Constants
class SearchConstants:
    VALID_SEARCH_TERM = "Investors"
    INVALID_SEARCH_TERM = "IMPOSSSSSSIBLEEEEDD"
    VALID_SEARCH_RESULTS_TITLE = f"Displaying results for '{VALID_SEARCH_TERM}'"
    INVALID_SEARCH_RESULTS_TITLE = "did not match any documents"


#Settings Constants
class SettingsConstants:
    EXPECTED_CLASSES = [
        'Private Equity', 'Private Credit', 'Real Estate',
        'Infrastructure', 'Public Markets', 'Family Offices'
    ]