from playwright.sync_api import Page,expect


class HomePage:

    PHONE_INPUT = "input#phone"
    MESSAGE_TEXTAREA = "textarea.form-control"
    RADIO_BUTTON_MALE = "input[type=radio][value=male]"
    COUNTRY_DROPDOWN = "//select[@id='country']"
    DATEPICKER_INPUT = "#datepicker"
    NEXT_BUTTON = "//div[@id='ui-datepicker-div']/descendant::a[@title='Next']"
    DATE_CELLS = "(//a[@class='ui-state-default'])"
    MONTH = "span.ui-datepicker-month"
    YEAR = "span.ui-datepicker-year"

    def __init__(self, page: Page) -> None:
        self.page = page
    
    def navigate(self, url) -> None:
        self.page.goto(url, timeout=4000)

    def fill_name(self, name: str) -> None:
        self.page.get_by_placeholder("Enter Name").fill(name)
        self.page.wait_for_timeout(2000)
    
    def fill_email(self, email: str) -> None:
        self.page.get_by_placeholder("Enter Email").fill(email)
        self.page.wait_for_timeout(2000)

    def fill_phone(self, phone: str) -> None:
        self.page.locator(self.PHONE_INPUT).fill(phone)
        self.page.wait_for_timeout(2000)

    def fill_message(self, message: str) -> None:
        self.page.locator(self.MESSAGE_TEXTAREA).fill(message)
        self.page.wait_for_timeout(2000)

    def select_male_radio(self) -> None:
        radio_btn=self.page.locator(self.RADIO_BUTTON_MALE)
        radio_btn.check()
        radio_btn.scroll_into_view_if_needed()
        expect(radio_btn).to_be_checked()
        self.page.wait_for_timeout(2000)

    def select_country(self,country_value: str) -> None:
        self.page.locator(self.COUNTRY_DROPDOWN).select_option(country_value)
        self.page.wait_for_timeout(2000)
    
    def select_check_boxes(self, days: list[str]) -> None:
        for day in days:
            check_box = self.page.locator(f"input[type=checkbox][value={day.lower()}]")
            check_box.check()
            expect(check_box).to_be_checked()
            self.page.wait_for_timeout(500)

    def calendar_select_date(self, target_month: str, target_year: str, target_day: str) -> None:

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