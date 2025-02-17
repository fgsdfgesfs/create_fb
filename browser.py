from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Set up Firefox options
firefox_options = Options()
firefox_options.binary_location = "/data/data/com.termux/files/usr/bin/firefox"  # Correct Firefox binary location
firefox_options.add_argument("--headless")  # Headless mode (optional)
firefox_options.add_argument("--no-sandbox")
firefox_options.add_argument("--disable-dev-shm-usage")

# Set up geckodriver (ensure this path points to the correct geckodriver location)
service = Service("/data/data/com.termux/files/usr/bin/geckodriver")  # Path to geckodriver

# Initialize Firefox WebDriver
driver = webdriver.Firefox(service=service, options=firefox_options)

# Open a website
driver.get("https://example.com")
print("Page title:", driver.title)

# Close the browser
driver.quit()
