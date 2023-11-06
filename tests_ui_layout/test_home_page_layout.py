from pom.home_page_elements import HomePage
from playwright.sync_api import Playwright, sync_playwright

def test_about_us_section_verbiage(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state('networkidle')

    assert page.is_visible(HomePage.celebrating_beauty_header)
    #assert page.is_visible(HomePage.celebrating_beauty_body)


    context.close()
    browser.close()


