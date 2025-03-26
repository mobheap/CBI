from bs4 import BeautifulSoup

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
# print(len(products))

names = []
ratings = []
nums_ratings = []

for product in products:
    
    useful = product.find('div', class_="product-card__info")
    # if useful: print('ok')
    name_container = useful.find('div', class_="product-card__product-name")
    if name_container:
        name = name_container.find('div').text
        print(name)
        # names.append(name)
    
#     criticism = product.find('div', class_="product-card_rating__0QJvM")
#     # rating = criticism.find('div').text
#     # ratings.append(rating)
    
#     num_ratings = criticism.find('span', class_='pl-4th').text
#     print(num_ratings)
# #     num_ratings = re.search(r'\((\d+) Ratings\)', num_ratings).group(1) #regular expression to get num only
# #     nums_ratings.append(num_ratings)
    
# #     description_section = product.find('div', class_='product-card_content__cP10h')
# #     description = description_section.find('span').text
# #     descriptions.append(description)
    
# #     products_dict = {'Name': names, 'Rating-5': ratings, 'Number of reviews': nums_ratings, 'Description': descriptions}
# #     products_df = pd.DataFrame(products_dict)

# # products_df.to_csv('APM tools Gartner.csv', index=False)
# file.close()