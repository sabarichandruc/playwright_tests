from playwright.sync_api import Page, expect

def test_practice_page(page: Page) -> None:
    # Set viewport size to fit the screen
    page.set_viewport_size({"width": 1920, "height": 1080})

    # Navigate to the admin page
    page.goto("https://testautomationpractice.blogspot.com/",timeout=4000)

    #. get_by_placeholder(text)
    page.get_by_placeholder("Enter Name").fill("Sachin Tendulkar")
    page.get_by_placeholder("Enter Email").fill("sachin@example.com")

    #page.set_default_timeout(5000)

    #<HTML tag><#><Value of ID attribute>
    page.locator("input#phone").fill("9876543210")

    #<HTML tag><.><Value of Class attribute>
    page.locator("textarea.form-control").fill("This is a test message.")

    #<HTML tag><[attribute=Value of attribute]> 
    radio_btn = page.locator("input[type=radio][value=male]")
    radio_btn.check()

    radio_btn.scroll_into_view_if_needed()

    #asseting the radio button is checked
    expect(radio_btn).to_be_checked()  

    
    #Select all the checkboxes one by one
    list_of_days =["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    for day in list_of_days:
        check_box = page.locator(f"input[type=checkbox][value={day.lower()}]")
        check_box.check()
        expect(check_box).to_be_checked()
        page.wait_for_timeout(500)

    #Select option India from the dropdown using XPath axes
    page.locator("//select[@id='country']").select_option("india")


    #calender
    page.locator("#datepicker").click()

    while True:
        month = page.locator("span.ui-datepicker-month").text_content()
        year = page.locator("span.ui-datepicker-year").text_content()

        if month == "March" and year == "2026":
           break
        page.wait_for_timeout(1000)
        page.locator("//div[@id='ui-datepicker-div']/descendant::a[@title='Next']").click()

    dates = page.locator("(//a[@class='ui-state-default'])")

    for date in range(dates.count()):
        if dates.nth(date).text_content() == "25":
            dates.nth(date).click()
            break
     #verify the selected date
    expect(page.locator("#datepicker")).to_have_value("03/25/2026")           
