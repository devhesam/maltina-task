import requests
from bs4 import BeautifulSoup


def crawl_amazon(product_code):
    url = f"https://www.amazon.com/dp/{product_code}"
    headers = {"accept-language": "en-US,en;q=0.9", "accept-encoding": "gzip, deflate, br",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
               "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise ValueError(f"Failed to fetch product: {product_code}")

    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find('h1', {'id': 'title'}).text.lstrip().rstrip()
    name = " ".join(title.split()[:5])
    price = soup.find("span", {"class": "a-price"}).find("span").text

    return {
        'name': name,
        'price': float(price.replace('$', '').replace(',', '')),
    }
