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
#to fix error when trying to press view more
chrome_options.add_argument("--ignore-certificate-errors")
# chrome_options.add_argument("--allow-running-insecure-content")
# chrome_options.add_argument("--disable-web-security")

service = Service("chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

url = "https://www.gartner.com/reviews/market/observability-platforms"
driver.get(url)

# Wait for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

while True:
    try:
        # Wait for the button to be clickable
        button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "products-section_viewMore__2rmUM")))
        button.click()
        
        # Wait for new products to load
        wait.until(EC.staleness_of(button))  # Wait until button updates or disappears
    except Exception as e:
        print("No more 'View More Products' button found or an error occurred.")
        break

html = driver.page_source

driver.quit()

#print(html)

soup = BeautifulSoup(html, 'html.parser')

products = soup.find_all('div', class_="product-card_productCard__zVsqD")

names = []
ratings = []
nums_ratings = []
descriptions = []

for product in products:
    
    name_container = product.find('h3', class_="product-card_productTitle__abSdH")
    if name_container:
        name = name_container.find('a').text.strip()
        names.append(name)
    
    criticism = product.find('div', class_="product-card_rating__0QJvM")
    rating = criticism.find('div').text
    ratings.append(rating)
    
    num_ratings = criticism.find('a').text
    num_ratings = re.search(r'\((\d+) Ratings\)', num_ratings).group(1) #regular expression to get num only
    nums_ratings.append(num_ratings)
    
    description_section = product.find('div', class_='product-card_content__cP10h')
    description = description_section.find('span').text
    descriptions.append(description)
    
    products_dict = {'Name': names, 'Rating-5': ratings, 'Number of reviews': nums_ratings, 'Description': descriptions}
    products_df = pd.DataFrame(products_dict)

products_df.to_csv('data/raw/APM tools Gartner.csv', index=False)