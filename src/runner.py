thonimport json
import os
from extractors.spotlight_extractor import SpotlightExtractor
from outputs.exporters import DataExporter

def run_scraper(input_file):
    # Read the input file containing spotlight URLs
    with open(input_file, 'r') as f:
        spotlight_urls = f.readlines()

    # Initialize extractor and exporter
    extractor = SpotlightExtractor()
    exporter = DataExporter()

    # Extract and export data for each spotlight URL
    for url in spotlight_urls:
        spotlight_data = extractor.extract_data(url.strip())
        exporter.export_to_json(spotlight_data, f"output_{os.path.basename(url.strip())}.json")

if __name__ == '__main__':
    input_file = 'data/inputs.sample.txt'  # Example input file
    run_scraper(input_file)