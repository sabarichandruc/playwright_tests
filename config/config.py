"""
Configuration module for Playwright test automation
Loads environment variables from .env file and provides centralized config management
"""

import os
import logging
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
env_file_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_file_path, override=False)


class Config:
    """Base configuration class"""

    # Environment
    ENV = os.getenv("ENV", "development").lower()

    # Application URLs
    BASE_URL = os.getenv("BASE_URL", "https://testautomationpractice.blogspot.com/")

    # Browser Configuration
    BROWSER = os.getenv("BROWSER", "chromium").lower()
    HEADLESS = os.getenv("HEADLESS", "True").lower() == "true"
    SLOW_MO = int(os.getenv("SLOW_MO", "0"))

    # Timeouts (in milliseconds)
    DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "6000"))
    DEFAULT_NAVIGATION_TIMEOUT = int(os.getenv("DEFAULT_NAVIGATION_TIMEOUT", "5000"))
    WAIT_FOR_SELECTOR_TIMEOUT = int(os.getenv("WAIT_FOR_SELECTOR_TIMEOUT", "5000"))
    PAGE_LOAD_TIMEOUT = int(os.getenv("PAGE_LOAD_TIMEOUT", "30000"))

    # Screenshots and Videos
    SCREENSHOT_ON_FAILURE = os.getenv("SCREENSHOT_ON_FAILURE", "True").lower() == "true"
    SCREENSHOTS_PATH = Path(__file__).resolve().parent.parent / os.getenv("SCREENSHOTS_PATH", "screenshots")
    VIDEOS_PATH = Path(__file__).resolve().parent.parent / os.getenv("VIDEOS_PATH", "videos")

    # Logs
    LOGS_PATH = Path(__file__).resolve().parent.parent / os.getenv("LOGS_PATH", "logs")

    # Test Configuration
    ASSERT_PLAY = os.getenv("ASSERT_PLAY", "True").lower() == "true"

    @classmethod
    def setup_directories(cls) -> None:
        """Create necessary directories if they don't exist"""
        cls.SCREENSHOTS_PATH.mkdir(parents=True, exist_ok=True)
        cls.VIDEOS_PATH.mkdir(parents=True, exist_ok=True)
        cls.LOGS_PATH.mkdir(parents=True, exist_ok=True)

    @classmethod
    def setup_logging(cls) -> logging.Logger:
        """
        Setup logging configuration
        Returns a configured logger instance
        """
        cls.setup_directories()

        logger = logging.getLogger("PlaywrightTests")
        logger.setLevel(logging.DEBUG)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # File handler
        log_file = cls.LOGS_PATH / "test_execution.log"
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)

        # Formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # Add handlers
        if not logger.handlers:
            logger.addHandler(console_handler)
            logger.addHandler(file_handler)

        return logger

    @classmethod
    def get_browser_launch_options(cls) -> dict:
        """
        Get browser launch options for Playwright
        Returns a dictionary of browser launch options
        """
        return {
            "headless": cls.HEADLESS,
            "slow_mo": cls.SLOW_MO,
        }

    @classmethod
    def get_browser_context_options(cls) -> dict:
        """
        Get browser context options for Playwright
        Returns a dictionary of context options
        """
        return {
            "screenshot": {"path": cls.SCREENSHOTS_PATH, "omit_background": True}
            if cls.SCREENSHOT_ON_FAILURE
            else None,
            "video_dir": str(cls.VIDEOS_PATH),
            "record_video_dir": str(cls.VIDEOS_PATH),
        }

    @classmethod
    def display_config(cls) -> None:
        """Display current configuration"""
        config_dict = {
            "Environment": cls.ENV,
            "Base URL": cls.BASE_URL,
            "Browser": cls.BROWSER,
            "Headless": cls.HEADLESS,
            "Slow Motion": f"{cls.SLOW_MO}ms",
            "Default Timeout": f"{cls.DEFAULT_TIMEOUT}ms",
            "Navigation Timeout": f"{cls.DEFAULT_NAVIGATION_TIMEOUT}ms",
            "Screenshots on Failure": cls.SCREENSHOT_ON_FAILURE,
            "Screenshots Path": str(cls.SCREENSHOTS_PATH),
            "Videos Path": str(cls.VIDEOS_PATH),
            "Logs Path": str(cls.LOGS_PATH),
        }

        logger = cls.setup_logging()
        logger.info("=" * 60)
        logger.info("TEST CONFIGURATION")
        logger.info("=" * 60)
        for key, value in config_dict.items():
            logger.info(f"{key}: {value}")
        logger.info("=" * 60)


# Initialize directories and logging on import
Config.setup_directories()
logger = Config.setup_logging()