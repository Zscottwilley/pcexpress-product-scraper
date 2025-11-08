thonimport json
from extractors.pcexpress_parser import PcexpressParser
from outputs.exporters import Exporter
from config import settings

def main():
    # Initialize the scraper and exporter
    parser = PcexpressParser(settings.BANNER_ID, settings.STORE_URL)
    exporter = Exporter()

    # Scrape the product data
    product_data = parser.scrape()

    # Export the data
    exporter.export(product_data)

if __name__ == "__main__":
    main()