import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

# Set Firefox options
firefox_options = Options()
firefox_options.binary_location = "/data/data/com.termux/files/usr/bin/firefox"  # Path to Firefox
firefox_options.add_argument("--headless")  # Run in headless mode (optional)
firefox_options.add_argument("--no-sandbox")
firefox_options.add_argument("--disable-dev-shm-usage")

# Manually specify Geckodriver path
geckodriver_path = "/data/data/com.termux/files/usr/bin/geckodriver"
service = Service(geckodriver_path)

# Start Firefox WebDriver with the specified Geckodriver path
driver = webdriver.Firefox(service=service, options=firefox_options)

# Open a website
driver.get("https://example.com")
print("Page title:", driver.title)

# Close the browser
driver.quit()
