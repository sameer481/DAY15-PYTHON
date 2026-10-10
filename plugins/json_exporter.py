"""
JSON Exporter Plugin (plugins/json_exporter.py)

Dynamic plugin implementing the exporter contract.
"""

import json
from typing import List, Dict, Any


class JSONExporter:
    """Plugin implementation for exporting data records to JSON string."""

    plugin_name = "json"
    description = "Exports list of dictionaries to formatted JSON format."

    def export(self, data: List[Dict[str, Any]]) -> str:
        return json.dumps(data, indent=2, default=str)
