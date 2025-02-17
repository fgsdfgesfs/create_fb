from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.binary_location = "/data/data/com.termux/files/usr/bin/bromite"  # Bromite browser
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service("/data/data/com.termux/files/usr/bin/chromedriver")  # Path to chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open a website
driver.get("https://example.com")
print("Page title:", driver.title)

# Close the browser
driver.quit()
