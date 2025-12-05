import pytest
from playwright.sync_api import Page, expect    



def test_verify_admin_page(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.locator("//input[@name='username']").fill('admin')
    page.locator("//input[@name='password']").fill('admin123')
    page.locator("//button[@type='submit']").click()

    #click admin
    page.locator("//span[text()='Admin']").click()

    #verify admin page
    expect(page.locator("//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")).to_be_visible()

    page.locator("//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']").click()

    page.locator("//a[text()='Logout']").click()