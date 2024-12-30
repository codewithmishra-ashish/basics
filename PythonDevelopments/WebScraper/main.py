import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the e-commerce website to scrape
URL = "http://books.toscrape.com/"

# Function to get the HTML content of the page
def get_html(url):
    response = requests.get(url)
    return response.text

# Function to parse the HTML content and extract product information
def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    products = []

    for item in soup.select('.product_pod'):
        name = item.select_one('h3 a').get('title')
        price = item.select_one('.price_color').get_text(strip=True)
        rating = item.select_one('.star-rating').get('class')[1]

        products.append({
            'name': name,
            'price': price,
            'rating': rating
        })

    return products

# Function to save the extracted product information to a CSV file
def save_to_csv(products, filename='products.csv'):
    df = pd.DataFrame(products)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

# Main script
html_content = get_html(URL)
products = parse_html(html_content)
save_to_csv(products)
