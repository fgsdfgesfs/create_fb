import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Set Firefox options
firefox_options = Options()
firefox_options.binary_location = "/data/data/com.termux/files/usr/bin/firefox"  # Path to Firefox
firefox_options.add_argument("--headless")  # Run in headless mode (remove this for GUI)
firefox_options.add_argument("--no-sandbox")
firefox_options.add_argument("--disable-dev-shm-usage")

# Set mobile user-agent (optional)
firefox_options.set_preference("general.useragent.override", 
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/131.0 Mobile Safari/537.36")

# Start Firefox WebDriver
driver = webdriver.Firefox(options=firefox_options)

# Open a website
driver.get("https://example.com")
print("Page title:", driver.title)

# Close the browser
driver.quit()
