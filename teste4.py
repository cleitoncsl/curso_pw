from pom.home_page_elements import HomePage
from playwright.sync_api import Playwright, sync_playwright

url_base = 'http://www.google.com.br'

def get_page(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    return context.new_page()

    #assert page.is_visible(HomePage.celebrating_beauty_header)
    #assert page.is_visible(HomePage.celebrating_beauty_body)


def abriritssagro(page):
    page.goto(url_base)
    page.pause()


if __name__ == "__main__":
    with sync_playwright() as playwright:
        page = get_page(playwright)
        abriritssagro(page)