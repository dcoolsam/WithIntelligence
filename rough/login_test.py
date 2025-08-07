from sqlite3 import Time
from playwright.sync_api import sync_playwright

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://platform.withintelligence.com/login")

        ACCEPT_COOKIES = 'button:has-text("Accept All Cookies")'

        # if page.is_visible(ACCEPT_COOKIES, timeout=50000):
        #     print("Accepting cookies")
        #     # page.click(ACCEPT_COOKIES)
        page.wait_for_load_state("networkidle")

        button = page.get_by_role("button", name="Accept All Cookies")
        if button.is_visible():
            button.click()
            print("Cookies accepted")
        else:
            print("No cookie popup found")

        page.get_by_label("Email").fill("your_username")
        page.get_by_label("Password").fill("your_password")
        page.get_by_role("button", name="Sign In").click()

        page.wait_for_url("**/dashboard",timeout=30000)



        # page.wait_for_url("**/dashboard")
        # assert "Dashboard" in page.title()

        # browser.close()