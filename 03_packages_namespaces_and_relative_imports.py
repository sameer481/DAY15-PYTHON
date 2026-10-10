"""
Day 15 - Python Modules & Packages Masterclass
File 3: Packages, Hierarchical Namespaces, Relative Imports & PEP 420

This script covers:
1. Package Anatomy: Directories, `__init__.py` role, initialization side-effects.
2. Absolute vs Relative Import Mechanics (`.` current package, `..` parent package).
3. PEP 420: Implicit Namespace Packages (packages without `__init__.py`) vs Regular Packages.
4. Package metadata attributes (`__package__`, `__path__`, `__version__`).
5. Hierarchical package traversal and nested module consumption.
"""

import sys
import os
import types
from typing import Any

# Ensure current working directory is in sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Absolute imports of package and subpackage
import sample_modules
import sample_modules.subpackage.analytics as analytics


def print_section(title: str) -> None:
    """Print formatted section banner."""
    print(f"\n{'=' * 75}\n  {title}\n{'=' * 75}")


# ==============================================================================
# 1. Package Anatomy & __init__.py Role
# ==============================================================================
def section_1_package_anatomy() -> None:
    print_section("1. Package Anatomy & __init__.py Initialization")

    print(f"Package Object                    : {sample_modules}")
    print(f"Package Metadata __version__     : {sample_modules.__version__}")
    print(f"Package Metadata __author__      : {sample_modules.__author__}")
    print(f"Package Search Path (__path__)   : {sample_modules.__path__}")
    print(f"Package Name (__name__)          : {sample_modules.__name__}")

    # Accessing package-level exposed APIs via __init__.py exports
    val1 = sample_modules.add(10, 20)
    val2 = sample_modules.multiply(6, 7)
    txt = sample_modules.reverse_string("Package Exported")

    print(f"\nExposed Package API Calls:")
    print(f"  sample_modules.add(10, 20)        = {val1}")
    print(f"  sample_modules.multiply(6, 7)     = {val2}")
    print(f"  sample_modules.reverse_string(...) = '{txt}'")


# ==============================================================================
# 2. Subpackages & Relative vs Absolute Imports
# ==============================================================================
def section_2_subpackages_and_relative_imports() -> None:
    print_section("2. Subpackages & Relative vs Absolute Imports")

    # Sample dataset
    dataset = [10.5, 20.0, 15.5, 30.2, 25.8, 18.0]

    # Calling subpackage analytics function (which internally used relative import `from ..math_utils import add`)
    stats = analytics.calculate_summary_stats(dataset)

    print(f"Subpackage analytics module      : {analytics}")
    print(f"Calculated Summary Statistics    :")
    for k, v in stats.items():
        print(f"  {k:10s} : {v}")

    print("\n--- Absolute vs Relative Import Syntax Summary ---")
    print("  Absolute Import : `import sample_modules.math_utils`")
    print("                    Explicit, unambiguous, works from any location in codebase.")
    print("  Relative Import : `from . import math_utils`  (current directory)")
    print("                    `from ..subpackage import analytics` (parent package level)")
    print("                    Only usable inside package modules, clean for internal refactoring.")


# ==============================================================================
# 3. PEP 420: Regular Packages vs Implicit Namespace Packages
# ==============================================================================
def section_3_namespace_packages_pep420() -> None:
    print_section("3. PEP 420: Regular Packages vs Implicit Namespace Packages")

    print("Comparison of Package Types in Python 3.3+:")
    print("\n1. Regular Package:")
    print("   - Directory contains an `__init__.py` file.")
    print("   - Has a single `__file__` attribute pointing to `__init__.py`.")
    print("   - Executed once when package is imported.")

    print("\n2. Implicit Namespace Package (PEP 420):")
    print("   - Directory does NOT contain an `__init__.py` file.")
    print("   - Useful for splitting a single logical package across multiple separate zip files or directories.")
    print("   - `__file__` is None, `__path__` is a _NamespacePath iterable extending across search directories.")

    # Verification of sample_modules package type
    is_regular = hasattr(sample_modules, "__file__") and sample_modules.__file__ is not None
    print(f"\nIs 'sample_modules' a Regular Package with __init__.py? {is_regular}")
    if is_regular:
        print(f"Location of __init__.py: {sample_modules.__file__}")


# ==============================================================================
# Main Execution Entry Point
# ==============================================================================
if __name__ == "__main__":
    print("[>>>] DAY 15: MASTERING PYTHON PACKAGES & NAMESPACES")
    section_1_package_anatomy()
    section_2_subpackages_and_relative_imports()
    section_3_namespace_packages_pep420()
    print("\n[OK] Section 3 completed successfully.")
