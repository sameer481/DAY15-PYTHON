"""
Analytics Module inside Subpackage (sample_modules/subpackage/analytics.py)

Demonstrates relative imports from parent package (`from ..math_utils import add`)
and statistical calculations using built-in modules (`statistics`).
"""

import statistics
from typing import List, Dict, Union
# Relative import from parent package
from ..math_utils import add


def calculate_summary_stats(data: List[Union[int, float]]) -> Dict[str, float]:
    """Compute summary statistics for numerical data series."""
    if not data:
        raise ValueError("Cannot calculate statistics on empty dataset.")

    mean_val = statistics.mean(data)
    median_val = statistics.median(data)
    stdev_val = statistics.stdev(data) if len(data) > 1 else 0.0
    total_val = sum(data)

    # Use relative imported add function for a dummy demonstration
    adjusted_total = add(total_val, 0)

    return {
        "count": float(len(data)),
        "sum": float(adjusted_total),
        "mean": round(mean_val, 4),
        "median": round(median_val, 4),
        "stdev": round(stdev_val, 4),
        "min": float(min(data)),
        "max": float(max(data)),
    }
