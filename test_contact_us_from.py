from playwright.sync_api import Playwright, sync_playwright, expect
import pytest
from pom.contact_us_page import ContactUsPage

def submit_form(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    contact_us = ContactUsPage(page)
    contact_us.navigate()
    page.wait_for_load_state("networkidle")
    page.pause
    contact_us.submit_form("Cleiton", "Rua", "cleitoncsl@gmail.com", "12345678", "Teste Mapeamento", "Teste")


#with sync_playwright() as playwright:
#    test_submit_form(playwright)