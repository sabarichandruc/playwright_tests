from playwright.sync_api import Page, expect
from pathlib import Path 
import sys
import allure

sys.path.append(str(Path(__file__).parent.parent))

from pages.Home import HomePage
from config.config import Config, logger


def test_practice_page(page: Page, base_url: str, config) -> None:
    """
    Complete form submission test with all required fields and selections
    """
    # Set timeouts from config
    page.set_default_timeout(config.DEFAULT_TIMEOUT)
    page.set_default_navigation_timeout(config.DEFAULT_NAVIGATION_TIMEOUT)

    home_page = HomePage(page, config)
    
    with allure.step("Navigate to Practice Page and fill the form"):
        logger.info(f"Navigating to {base_url}")
        home_page.navigate(base_url)

    with allure.step("Fill contact form"):
        home_page.fill_name("Sachin Tendulkar")
        home_page.fill_email("sachin.tendulkar@example.com")
        home_page.fill_phone("9876543210")
        home_page.fill_message("This is a test message.")

    with allure.step("Select gender radio button"):
        home_page.select_male_radio()
    
    with allure.step("Select checkboxes"):
        home_page.select_check_boxes(["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
    
    with allure.step("Select country"):
        home_page.select_country("india")
        
    with allure.step("Select date from calendar"):
        home_page.calendar_select_date("March","2026","25")

    with allure.step("Upload a file"):
        # Create a sample file to upload
        sample_file_path = Path(__file__).parent / "sample_upload.txt"
        with open(sample_file_path, "w") as f:
            f.write("This is a sample file for upload testing.")
        logger.info(f"Uploading file: {sample_file_path}")
        home_page.upload_file(str(sample_file_path))   

    with allure.step("Submit the form"):
        home_page.submit_form()
        logger.info("Form submitted successfully")

    # Clean up the sample file after upload
    if sample_file_path.exists():
        sample_file_path.unlink()
        logger.info("Sample file cleaned up")
    
    page.wait_for_timeout(4000) 
    