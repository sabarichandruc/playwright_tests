from playwright.sync_api import Page
import pytest

@pytest.mark.Reression
def test_first_program(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    assert page.title() == "Automation Testing Practice"
    page.locator("#name").fill("Playwright")
    #page.pause()
    page.locator("#email").fill("y0A7o@example.com")

@pytest.mark.smoke
def test_second_program(page:Page):
    page.goto("https://demo.automationtesting.in/Register.html")
    assert page.title() == "Register"
