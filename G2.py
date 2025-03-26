from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
import pandas as pd
import time

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

# soup = BeautifulSoup(html, 'html.parser')

# products = soup.find_all('div', class_="product-card_productCard__zVsqD")

# names = []
# ratings = []
# nums_ratings = []
# descriptions = []

# for product in products:
    
#     name_container = product.find('h3', class_="product-card_productTitle__abSdH")
#     if name_container:
#         name = name_container.find('a').text.strip()
#         names.append(name)
    
#     criticism = product.find('div', class_="product-card_rating__0QJvM")
#     rating = criticism.find('div').text
#     ratings.append(rating)
    
#     num_ratings = criticism.find('a').text
#     num_ratings = re.search(r'\((\d+) Ratings\)', num_ratings).group(1) #regular expression to get num only
#     nums_ratings.append(num_ratings)
    
#     description_section = product.find('div', class_='product-card_content__cP10h')
#     description = description_section.find('span').text
#     descriptions.append(description)
    
#     products_dict = {'Name': names, 'Rating-5': ratings, 'Number of reviews': nums_ratings, 'Description': descriptions}
#     products_df = pd.DataFrame(products_dict)

# products_df.to_csv('APM tools Gartner.csv', index=False)