from bs4 import BeautifulSoup
import requests
import pandas as pd

# def get_data():
#     session = requests.Session()
#     session.headers.update({
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
#     })
#     response = session.get("https://uptrace.dev/tools/top-apm-tools#detailed-comparison-of-apm-tools")

#     print(response.status_code)

#     if response.status_code != 200:
#         code = response.status_code
#         print(f"Failed to retrieve data {code}")
#         exit()
    
#     content = response.text
    
#     return content

# html = get_data()
# with open("data/raw/Uptrace.html", "w", encoding="utf-8") as file:
#     file.write(html)



# # Didn't think this would work bc it's so easy but it did
# tables = pd.read_html("https://uptrace.dev/tools/top-apm-tools#detailed-comparison-of-apm-tools")
# df = tables[0]
# print(df)



with open('data/raw/Uptrace.html', 'r', encoding='utf-8') as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table')

headers = [header.text.strip() for header in table.find_all("th")]

# Extract table rows
rows = []
for row in table.find_all("tr")[1:]:  # Skipping header row
    cells = [cell.text.strip() for cell in row.find_all("td")]
    rows.append(cells)

# Convert to DataFrame
df = pd.DataFrame(rows, columns=headers)
print(df)

df.to_csv("data/raw/Uptrace.csv", index=False)