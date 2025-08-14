import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Environment URLs
    ENVIRONMENTS = {
        'dev': 'https://platform.withintelligence.com',
        'qa': 'https://platform.withintelligence.com',
        'staging': 'https://platform.withintelligence.com',
        'prod': 'https://platform.withintelligence.com'
    }
    
    # Current environment (can be changed)
    CURRENT_ENV = 'qa'
    BASE_URL = ENVIRONMENTS[CURRENT_ENV]
    
    # Browser settings
    BROWSER = 'chromium'  # chromium, firefox, webkit
    HEADLESS = True
    SLOW_MO = 0
    
    # Test credentials
    USERNAME = os.getenv('TEST_USERNAME')
    PASSWORD = os.getenv('TEST_PASSWORD')
    
    # Timeouts
    DEFAULT_TIMEOUT = 30000
    
    # Paths
    SCREENSHOT_PATH = './screenshots'
    LOG_PATH = './logs'
    REPORT_PATH = './reporting'