"""
CSV Exporter Plugin (plugins/csv_exporter.py)

Dynamic plugin implementing the exporter contract.
"""

import csv
import io
from typing import List, Dict, Any


class CSVExporter:
    """Plugin implementation for exporting data records to CSV string."""

    plugin_name = "csv"
    description = "Exports list of dictionaries to Comma-Separated Values format."

    def export(self, data: List[Dict[str, Any]]) -> str:
        if not data:
            return ""

        output = io.StringIO()
        fieldnames = list(data[0].keys())
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
        return output.getvalue()
