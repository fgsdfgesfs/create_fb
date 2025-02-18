import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

def create_chrome_instance():
    temp_dir = tempfile.mkdtemp()
    print(temp_dir)
    
    chrome_options = Options()
    chrome_options.add_argument(f"--user-data-dir={temp_dir}")  # Unique user data directory
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    
    chrome_options.add_argument("--headless")  # Run in headless mode (needed for Termux)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--window-size=400x640")

    random_user_agent = "Mozilla/5.0 (Linux; Android 11; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
    chrome_options.add_argument(f"user-agent={random_user_agent}")

    # Disable WebDriver detection
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--allow-running-insecure-content")
    chrome_options.add_argument("--disable-site-isolation-trials")

    # Start Xvfb (virtual display)
    import os
    os.system("Xvfb :99 -screen 0 1280x800x24 &")
    os.environ["DISPLAY"] = ":99"

    # Initialize the Chrome WebDriver
    browser = webdriver.Chrome(service=ChromeService("/data/data/com.termux/files/usr/bin/chromedriver"), options=chrome_options)
    return browser

browser=create_chrome_instance()
browser.get("https://www.google.com")
browser.save_screenshot("/sdcard/download/screenshot.png")
browser.quit()
