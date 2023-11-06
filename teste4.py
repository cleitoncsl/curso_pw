from pom.home_page_elements import HomePage
from playwright.sync_api import Playwright, sync_playwright

def about_us_section_verbiage(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    assert page.is_visible(HomePage.celebrating_beauty_header)
    #assert page.is_visible(HomePage.celebrating_beauty_body)


    context.close()
    browser.close()



with sync_playwright() as playwright:
    about_us_section_verbiage(playwright)



