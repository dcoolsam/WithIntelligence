# utils/logger.py
import logging

import sys
from pathlib import Path
from datetime import datetime

class TestLogger:
    def __init__(self, name="TestFramework", log_level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)
        self.logger.handlers.clear()  # clear existing

        # Ensure logs directory
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)

        # Setup formatter
        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)8s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # Single log file for both info and errors
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        file_handler = logging.FileHandler(log_dir / f"test_{timestamp}.log", mode='w', encoding='utf-8')
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG)
        self.logger.addHandler(file_handler)
        self.main_log_file = str(log_dir / f"test_{timestamp}.log")

        # Console handler
        console_formatter = logging.Formatter(fmt="%(asctime)s | %(levelname)8s | %(message)s", datefmt="%H:%M:%S")
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(console_formatter)
        console_handler.setLevel(logging.INFO)
        self.logger.addHandler(console_handler)

    # Simple API: directly use info/debug/etc
    def info(self, msg):      self.logger.info(msg)
    def debug(self, msg):     self.logger.debug(msg)
    def warning(self, msg):   self.logger.warning(msg)
    def error(self, msg):     self.logger.error(msg)
    def critical(self, msg):  self.logger.critical(msg)

    # Test framework helpers
    def test_start(self, name, description=""):
        sep = "=" * 60
        self.info(f"\n{sep}\nSTART TEST: {name}")
        if description:
            self.info(f"DESCRIPTION: {description}")
        self.info(sep)
    def test_end(self, name, status="COMPLETED"):
        self.info(f"END TEST: {name} | STATUS: {status}\n{'='*60}\n")
    def test_step(self, step, desc):
        self.info(f"STEP {step}: {desc}")

    def exception(self, exc, context=""):
        self.error(f"EXCEPTION: {type(exc).__name__}: {exc}" + (f" | {context}" if context else ""))

    def get_log_file(self):
        return self.main_log_file

# Singleton logger
_logger = None
def get_logger():
    global _logger
    if _logger is None:
        _logger = TestLogger()
    return _logger

# Quick shortcuts
def log_info(msg):       get_logger().info(msg)
def log_warning(msg):    get_logger().warning(msg)
def log_error(msg):      get_logger().error(msg)
def log_step(step, desc):get_logger().test_step(step, desc)

# Optional context manager for tests
class TestLogContext:
    def __init__(self, name, desc=""): self.name, self.desc = name, desc
    def __enter__(self): get_logger().test_start(self.name, self.desc)
    def __exit__(self, exc, val, tb):
        get_logger().test_end(self.name, "FAILED" if exc else "PASSED")
        if exc: get_logger().exception(val)

# Example usage
if __name__ == "__main__":
    logger = get_logger()
    with TestLogContext("Demo Test"):
        log_step(1, "Do stuff")
        log_info("Sample info")
        log_warning("Something fishy")
        log_error("Oops, error happened")
    print(f"Log file: {logger.get_log_file()}")
