import os
import time
from datetime import datetime

def create_directory(path: str):
    """Create directory if it doesn't exist"""
    os.makedirs(path, exist_ok=True)

def get_timestamp() -> str:
    """Get current timestamp string"""
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def wait(seconds: int):
    """Simple wait function"""
    time.sleep(seconds)