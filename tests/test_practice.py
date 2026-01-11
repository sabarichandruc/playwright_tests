from playwright.sync_api import Page, expect
from pathlib import Path 
import sys
import allure
sys.path.append(str(Path(__file__).parent.parent))

from pages.Home import HomePage


def test_practice_page(page: Page, base_url: str) -> None:

    page.set_default_timeout(6000)
    #page.set_viewport_size({"width": 1920, "height": 1080})

    home_page = HomePage(page)
    with allure.step("Navigate to Practice Page and fill the form"):
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
