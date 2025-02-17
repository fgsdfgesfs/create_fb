import time
import os
import chromedriver_autoinstaller  # Auto-install correct ChromeDriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Ensure ChromeDriver is installed
chromedriver_autoinstaller.install()

# Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Required for Termux
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--disable-infobars")

# Mobile device emulation
mobile_emulation = {
    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.81 Mobile Safari/537.36"
}
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

# Set ChromeDriver path if needed
driver = webdriver.Chrome(options=chrome_options)

# Open a website
driver.get("https://example.com")
print("Page title:", driver.title)

# Close the browser
driver.quit()
