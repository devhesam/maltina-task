import requests
from bs4 import BeautifulSoup


def crawl_amazon(product_code):
    url = f"https://www.amazon.com/dp/{product_code}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise ValueError(f"Failed to fetch product: {product_code}")

    soup = BeautifulSoup(response.content, 'html.parser')
    name = soup.find('span', {'id': 'productTitle'}).get_text(strip=True)
    price = soup.find('span', {'class': 'a-offscreen'}).get_text(strip=True)

    return {
        'name': name,
        'price': float(price.replace('$', '').replace(',', '')),
    }
