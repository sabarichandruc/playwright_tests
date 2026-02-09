from playwright.sync_api import Page, expect
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from config.config import Config, logger


class HomePage:
    """Home page object model for test automation"""

    # Selectors
    PHONE_INPUT = "input#phone"
    MESSAGE_TEXTAREA = "textarea.form-control"
    RADIO_BUTTON_MALE = "input[type=radio][value=male]"
    COUNTRY_DROPDOWN = "//select[@id='country']"
    DATEPICKER_INPUT = "#datepicker"
    NEXT_BUTTON = "//div[@id='ui-datepicker-div']/descendant::a[@title='Next']"
    DATE_CELLS = "(//a[@class='ui-state-default'])"
    MONTH = "span.ui-datepicker-month"
    YEAR = "span.ui-datepicker-year"
    UPLOAD_FILE_INPUT = "input#singleFileInput"
    UPLOAD_SUBMIT_BUTTON = "//form[@id='singleFileForm']/child::button[@type='submit']"

    def __init__(self, page: Page, config: Config = None) -> None:
        """
        Initialize HomePage with page object and optional config
        
        Args:
            page: Playwright Page object
            config: Configuration object with timeout settings
        """
        self.page = page
        self.config = config or Config
        self.wait_time = self.config.DEFAULT_TIMEOUT // 1000  # Convert to seconds for wait_for_timeout
    
    def navigate(self, url: str) -> None:
        """Navigate to the given URL"""
        logger.info(f"Navigating to {url}")
        self.page.goto(url, timeout=self.config.PAGE_LOAD_TIMEOUT)

    def fill_name(self, name: str) -> None:
        """Fill name field"""
        logger.info(f"Filling name: {name}")
        self.page.get_by_placeholder("Enter Name").fill(name)
        self.page.wait_for_timeout(2000)
    
    def fill_email(self, email: str) -> None:
        """Fill email field"""
        logger.info(f"Filling email: {email}")
        self.page.get_by_placeholder("Enter Email").fill(email)
        self.page.wait_for_timeout(2000)

    def fill_phone(self, phone: str) -> None:
        """Fill phone field"""
        logger.info(f"Filling phone: {phone}")
        self.page.locator(self.PHONE_INPUT).fill(phone)
        self.page.wait_for_timeout(2000)

    def fill_message(self, message: str) -> None:
        """Fill message textarea"""
        logger.info(f"Filling message: {message}")
        self.page.locator(self.MESSAGE_TEXTAREA).fill(message)
        self.page.wait_for_timeout(2000)

    def select_male_radio(self) -> None:
        """Select male radio button"""
        logger.info("Selecting male radio button")
        radio_btn = self.page.locator(self.RADIO_BUTTON_MALE)
        radio_btn.check()
        radio_btn.scroll_into_view_if_needed()
        expect(radio_btn).to_be_checked()
        self.page.wait_for_timeout(2000)

    def select_country(self, country_value: str) -> None:
        """Select country from dropdown"""
        logger.info(f"Selecting country: {country_value}")
        self.page.locator(self.COUNTRY_DROPDOWN).select_option(country_value)
        self.page.wait_for_timeout(2000)
    
    def select_check_boxes(self, days: list[str]) -> None:
        """Select multiple checkboxes by day names"""
        logger.info(f"Selecting checkboxes: {', '.join(days)}")
        for day in days:
            check_box = self.page.locator(f"input[type=checkbox][value={day.lower()}]")
            check_box.check()
            expect(check_box).to_be_checked()
            self.page.wait_for_timeout(500)

    def calendar_select_date(self, target_month: str, target_year: str, target_day: str) -> None:
        """Select a date from the calendar picker"""
        logger.info(f"Selecting date: {target_month} {target_day}, {target_year}")
        
        self.page.locator(self.DATEPICKER_INPUT).click()

        while True:
            month = self.page.locator(self.MONTH).text_content()
            year = self.page.locator(self.YEAR).text_content()

            if month == target_month and year == target_year:
                break
            self.page.wait_for_timeout(1000)
            self.page.locator(self.NEXT_BUTTON).click()

        dates = self.page.locator(self.DATE_CELLS)

        for date in range(dates.count()):
            if dates.nth(date).text_content() == target_day:
                dates.nth(date).click()
                break

    def upload_file(self, file_path: str) -> None:
        """Upload a file"""
        logger.info(f"Uploading file: {file_path}")
        self.page.locator(self.UPLOAD_FILE_INPUT).set_input_files(file_path)
        self.page.wait_for_timeout(2000)

    def submit_form(self) -> None:
        """Submit the form"""
        logger.info("Submitting form")
        self.page.locator(self.UPLOAD_SUBMIT_BUTTON).click()
        self.page.wait_for_timeout(4000)