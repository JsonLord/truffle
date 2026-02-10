from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Login
        page.goto("http://localhost:8001/login/")
        time.sleep(2)
        # Use fill if needed, although they are pre-filled
        page.fill('input[name="username"]', 'admin')
        page.fill('input[name="password"]', 'admin123')
        page.click('button:has-text("Sign In")')
        time.sleep(2)

        # Go to add post
        page.goto("http://localhost:8001/add_post/")
        time.sleep(2)
        page.screenshot(path="add_post_page.png")

        # Go to home
        page.goto("http://localhost:8001/")
        time.sleep(2)
        page.screenshot(path="home_page_final.png")

        browser.close()

if __name__ == "__main__":
    run()
