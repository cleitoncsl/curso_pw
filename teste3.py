import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


@pytest.fixture(scope="function", autouse=True)
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Log In").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    # page.get_by_test_id("emailAuth").get_by_label("Email").fill("symon.storozhenko@gmail.com")
    page.fill('input:below(:text("Email"))', "symon.storozhenko@gmail.com")
    # page.pause()
    page.get_by_label("Password").fill("test123")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    page.wait_for_load_state("networkidle")
    #expect(page.get_by_role("button", name="Log Ins")).to_be_hidden()
    assert page.is_visible("[aria-label=\"symon.storozhenko account menu\"]")


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
