from bs4 import BeautifulSoup
import re
import pandas as pd

with open('scraped_page.html', 'r', encoding='utf-8') as file:
    html = file.read()
    
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

products_df.to_csv('APM tools G2.csv', index=False)