thonimport json

class DataExporter:
    def export_to_json(self, data, output_filename):
        with open(output_filename, 'w') as f:
            json.dump(data, f, indent=4)