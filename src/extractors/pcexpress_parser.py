thonimport requests
from bs4 import BeautifulSoup
import logging

class PcexpressParser:
    def __init__(self, banner_id, store_url):
        self.banner_id = banner_id
        self.store_url = store_url

    def scrape(self):
        logging.info(f"Scraping products from {self.store_url}")
        response = self._get_store_page(self.store_url)

        if response.status_code != 200:
            logging.error("Failed to retrieve store page")
            return []

        products = self._parse_product_data(response.text)
        return products

    def _get_store_page(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching page: {e}")
            return None

    def _parse_product_data(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        product_list = []

        # Assuming the products are in a div with the class 'product-item'
        for product in soup.find_all('div', class_='product-item'):
            product_data = {
                "name": product.find('span', class_='product-name').text.strip(),
                "price": product.find('span', class_='product-price').text.strip(),
                "availability": "In Stock" in product.find('span', class_='availability').text.strip(),
                "image": product.find('img', class_='product-image')['src'],
                "description": product.find('div', class_='product-description').text.strip(),
            }
            product_list.append(product_data)

        logging.info(f"Found {len(product_list)} products.")
        return product_list