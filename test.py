from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_data():
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    })
    response = session.get("https://www.gartner.com/reviews/market/observability-platforms")

    print(response.status_code)

    if response.status_code != 200:
        code = response.status_code
        return f"Failed to retrieve data {code}"
    
    content = response.text
    
    return content


print(get_data())