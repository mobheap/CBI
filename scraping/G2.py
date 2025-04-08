from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# options
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
    # element to wait for
    wait = WebDriverWait(driver, 10)
    main_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.some-class')))
    print("Page loaded successfully!")
except Exception as e:
    print(f"Error loading page: {e}")

html = driver.page_source

driver.quit()

# print(html)

with open("data/raw/scraped_page.html", "w", encoding="utf-8") as file:
    file.write(html)

from bs4 import BeautifulSoup
import re
import pandas as pd

# with open('data/raw/scraped_page.html', 'r', encoding='utf-8') as file:
#     html = file.read()
    
# with open('original.html', 'r') as file:
#     original = file.read()

# if scraped == original:
#     print('Got the right html!')
# else:
#     print('Failed')


soup = BeautifulSoup(html, 'html.parser')

products = soup.find_all('div', class_="x-ordered-inputs-initialized")

names = []
ratings = []
nums_ratings = []

for product in products:
    
    try:    
        useful = product.find('div', class_="product-card__info")
        # if useful: print('ok')
        name_container = useful.find('div', class_="product-card__product-name")
        if name_container:
            name = name_container.find('div').text.strip()
            names.append(name)
        
        criticism = useful.find('div', class_="d-f ai-c fw-w")
        rating = criticism.find('span', class_="fw-semibold").text.strip()
        ratings.append(rating)
        
        num_ratings = criticism.find('span', class_='pl-4th').text.strip()
        num_ratings = re.search(r"\(([\d,]+)\)", num_ratings).group(1).replace(',', '')
        nums_ratings.append(num_ratings)
    
    except Exception as e:
        print(f'Error processing a product: {e}')
        continue

products_dict = {
    'Name': names,
    'Rating-5': ratings,
    'Number of reviews': nums_ratings
    }

products_df = pd.DataFrame(products_dict)

products_df.to_csv('data/raw/G2.csv', index=False)