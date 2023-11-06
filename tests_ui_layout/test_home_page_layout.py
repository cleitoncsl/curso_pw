from playwright.sync_api import Playwright, sync_playwright, expect
from pom.home_page_elements import HomePage
from pom.shop_women_elements import ShopWomen

def about_us_section_verbiage(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://symonstorozhenko.wixsite.com/website-1')
    page.wait_for_load_state("networkidle")
    shop_women = ShopWomen(page)
    page.pause()
    expect(shop_women.celebrating_beauty_header).to_be_visible()


with sync_playwright() as playwright:
    about_us_section_verbiage(playwright)



