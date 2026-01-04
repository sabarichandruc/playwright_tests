from playwright.sync_api import Page,expect
import pytest

def test_context(browser):
    context = browser.new_context()
    page1 =context.new_page()
    page2 =context.new_page()

    page1.goto("https://testautomationpractice.blogspot.com/")

    expect(page1).to_have_title("Automation Testing Practice")

    page1.wait_for_timeout(5000)

    page2.goto("https://demo.automationtesting.in/Register.html")

    expect(page2).to_have_title("Register")

    page1.wait_for_timeout(1000)
