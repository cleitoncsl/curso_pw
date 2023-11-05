from playwright.sync_api import Playwright, sync_playwright, expect


def about_us_section_verbiage(plawright: Playwright):
    browser = plawright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    #assert page.is_visible("text=Celebrating Beauty and Style")

    expect(page.locator("text=Celebrating Beauty and Style")).to_be_hidden()

with sync_playwright() as playwright:
    about_us_section_verbiage(playwright)