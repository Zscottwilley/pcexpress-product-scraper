thonfrom extractors.utils import save_json
import logging

class Exporter:
    def export(self, data):
        if not data:
            logging.warning("No data to export")
            return

        save_json(data, 'output/sample_output.json')
        logging.info("Data exported to output/sample_output.json")