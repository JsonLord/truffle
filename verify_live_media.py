from playwright.sync_api import sync_playwright
import time
import requests

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Login
        print("Logging in...")
        page.goto("https://harvesthealth-dashboards-plotly.hf.space/login/")
        page.fill('input[name="username"]', "admin")
        page.fill('input[name="password"]', "admin123")
        page.click('button:has-text("Sign In")')
        page.wait_for_url("https://harvesthealth-dashboards-plotly.hf.space/")

        # Add Post
        print("Adding post with media...")
        page.goto("https://harvesthealth-dashboards-plotly.hf.space/add_post/")
        page.fill('input[name="title"]', "Playback Test Post")

        # We need small dummy files
        with open("test_audio.mp3", "wb") as f:
            f.write(b"dummy audio content")
        with open("test_video.mp4", "wb") as f:
            f.write(b"dummy video content")

        page.set_input_files('input[name="audio"]', "test_audio.mp3")
        page.set_input_files('input[name="video"]', "test_video.mp4")

        page.click('button:has-text("Post")')
        page.wait_for_url("https://harvesthealth-dashboards-plotly.hf.space/")

        # Check feed
        print("Checking feed for media URLs...")

        # Get audio/video URLs from the page
        audio_src = page.eval_on_selector('audio source', 'el => el.src')
        video_src = page.eval_on_selector('video source', 'el => el.src')

        print(f"Audio URL: {audio_src}")
        print(f"Video URL: {video_src}")

        # Check accessibility
        audio_resp = requests.head(audio_src)
        video_resp = requests.head(video_src)

        if audio_resp.status_code == 200:
            print("SUCCESS: Audio URL returns 200 OK")
        else:
            print(f"FAILURE: Audio URL returns {audio_resp.status_code}")

        if video_resp.status_code == 200:
            print("SUCCESS: Video URL returns 200 OK")
        else:
            print(f"FAILURE: Video URL returns {video_resp.status_code}")

        page.screenshot(path="media_playback_verification.png", full_page=True)
        print("Screenshot taken: media_playback_verification.png")

        browser.close()

if __name__ == "__main__":
    run()
