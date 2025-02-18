
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

def create_chrome_instance():

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Headless mode for Termux
    options.add_argument("--no-sandbox")  
    options.add_argument("--disable-gpu")  
    options.add_argument("--disable-software-rasterizer")  
    options.add_argument("--disable-dev-shm-usage")  
    options.add_argument("--disable-infobars")  
    options.add_argument("--disable-blink-features=AutomationControlled")  
    options.add_argument("--window-size=400x640")  # Set window size

    user_agent = "Mozilla/5.0 (Linux; Android 11; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
    options.add_argument(f"user-agent={user_agent}")


    # Initialize Chrome WebDriver
    driver = webdriver.Chrome(options=options)
    return driver

browser=create_chrome_instance()
browser.get("https://www.google.com")
browser.save_screenshot("/sdcard/download/screenshot.png")
browser.quit()
