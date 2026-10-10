"""
Sample Package Initialization File (sample_modules/__init__.py)

This package demonstrates package initialization, package-level exports (__all__),
and package versioning.
"""

from .math_utils import add, multiply, FactorialCalculator
from .string_utils import clean_text, reverse_string

__version__ = "1.0.0"
__author__ = "Sameer Mohammed"

# Control what is exported when a user does: from sample_modules import *
__all__ = [
    "add",
    "multiply",
    "FactorialCalculator",
    "clean_text",
    "reverse_string",
    "__version__",
]

print(f"[PACKAGE INIT] Loaded package 'sample_modules' v{__version__}")
