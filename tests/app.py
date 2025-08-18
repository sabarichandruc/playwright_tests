from playwright.sync_api import sync_playwright

#launch the browser
with sync_playwright() as browser:
    # Launch the browser in headless mode
    browser = browser.chromium.launch(headless=False, slow_mo=500)
    #create a new page
    page = browser.new_page()
    # Navigate to a URL
    page.goto("https://playwright.dev/")
    #close the browser

    #go to the dev page
    #select or locate the link element with docs text

    docs_button = page.get_by_role("link", name="Get Started")

    #click on the link
    docs_button.click()

    #get the url
    page_url = page.url

    #print the url
    print(f"Current URL: {page_url}")

    browser.close()
