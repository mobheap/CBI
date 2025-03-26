from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# import re
import pandas as pd
# import time

# Chrome options
chrome_options = Options()
#chrome_options.add_argument("--headless")  # (no GUI)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent detection
chrome_options.add_argument("--start-maximized")

service = Service("chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

url = 'https://www.g2.com/categories/application-performance-monitoring-apm'
driver.get(url)

# Wait for the page to load by waiting for a specific element to be visible
try:
    # Use a suitable element to wait for (replace the element locator with something specific to the page)
    wait = WebDriverWait(driver, 10)
    main_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.some-class')))  # Example
    print("Page loaded successfully!")
except Exception as e:
    print(f"Error loading page: {e}")

html = driver.page_source

driver.quit()

print(html)

with open("scraped_page.html", "w", encoding="utf-8") as file:
    file.write(html)

