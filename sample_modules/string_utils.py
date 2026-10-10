"""
String Utilities Module (sample_modules/string_utils.py)

Demonstrates string formatting, cleaning helpers, and module attribute introspection.
"""

import re


def clean_text(text: str) -> str:
    """Strip whitespace and remove non-alphanumeric characters except spaces."""
    cleaned = re.sub(r"[^\w\s]", "", text)
    return " ".join(cleaned.split())


def reverse_string(text: str) -> str:
    """Reverse the given string."""
    return text[::-1]


def truncate(text: str, max_len: int = 20) -> str:
    """Truncate text to max_len with ellipsis."""
    if len(text) <= max_len:
        return text
    return text[: max_len - 3] + "..."


if __name__ == "__main__":
    print("[MODULE TEST] Running standalone test for string_utils...")
    raw = "  Hello, World! Python Modules 101.  "
    print(f"Original : '{raw}'")
    print(f"Cleaned  : '{clean_text(raw)}'")
    print(f"Reversed : '{reverse_string('Python')}'")
