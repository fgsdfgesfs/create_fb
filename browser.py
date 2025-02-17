from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

firefox_options = Options()
firefox_options.binary_location = "/data/data/com.termux/files/usr/bin/bromite"  # Bromite binary
firefox_options.add_argument("--headless")  # Headless mode
firefox_options.add_argument("--no-sandbox")
firefox_options.add_argument("--disable-dev-shm-usage")

service = Service("/data/data/com.termux/files/usr/bin/geckodriver")  # Path to geckodriver
driver = webdriver.Firefox(service=service, options=firefox_options)

# Open a website
driver.get("https://example.com")
print("Page title:", driver.title)

# Close the browser
driver.quit()
