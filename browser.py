from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up Bromite as the browser
chrome_options = Options()
chrome_options.binary_location = "/data/data/com.termux/files/usr/bin/bromite"
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Start WebDriver
service = Service("/data/data/com.termux/files/usr/bin/geckodriver")  # Geckodriver is needed for some functionality
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open a website
driver.get("https://example.com")
print("Page title:", driver.title)

# Close the browser
driver.quit()
