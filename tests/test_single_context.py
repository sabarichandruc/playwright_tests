from playwright.sync_api import Page,expect
import pytest

def test_context(browser):
    context = browser.new_context()
    page1 =context.new_page()

    page1.goto("https://testautomationpractice.blogspot.com/")

    expect(page1).to_have_title("Automation Testing Practice")

    page1.wait_for_timeout(5000)

