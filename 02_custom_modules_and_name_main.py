"""
Day 15 - Python Modules & Packages Masterclass
File 2: Custom Modules, Scope, Private Members & `if __name__ == '__main__'`

This script covers:
1. Creating and consuming user-defined Python modules (`sample_modules.math_utils`).
2. Understanding the `if __name__ == "__main__":` entry point idiom.
3. Private variable and function conventions (`_private_var`) vs public module APIs.
4. Export control with `__all__` list and its effect on `from module import *`.
5. Dynamic module reloading at runtime using `importlib.reload()`.
"""

import sys
import os
import importlib
from typing import List

# Ensure parent directory is in sys.path so sample_modules can be imported cleanly
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Import custom module
import sample_modules.math_utils as math_utils
from sample_modules.string_utils import clean_text, reverse_string


def print_section(title: str) -> None:
    """Print formatted section banner."""
    print(f"\n{'=' * 75}\n  {title}\n{'=' * 75}")


# ==============================================================================
# 1. Consuming Custom Module Functions & Encapsulated Classes
# ==============================================================================
def section_1_consuming_custom_modules() -> None:
    print_section("1. Consuming Custom Modules & Encapsulated Logic")

    # Calling imported custom module functions
    sum_res = math_utils.add(45, 55)
    prod_res = math_utils.multiply(12, 5)
    print(f"[math_utils.add(45, 55)]       = {sum_res}")
    print(f"[math_utils.multiply(12, 5)]  = {prod_res}")

    # Instantiating/using class from custom module
    fact = math_utils.FactorialCalculator.compute(7)
    print(f"[FactorialCalculator.compute(7)] = {fact}")

    # String utils module calls
    dirty_str = "   <<< Python 3 Modules & Packages Masterclass!!! >>>   "
    cleaned = clean_text(dirty_str)
    reversed_str = reverse_string(cleaned)
    print(f"\n[string_utils] Original : '{dirty_str}'")
    print(f"[string_utils] Cleaned  : '{cleaned}'")
    print(f"[string_utils] Reversed : '{reversed_str}'")


# ==============================================================================
# 2. Understanding __name__ == "__main__" Behavior
# ==============================================================================
def section_2_name_main_explanation() -> None:
    print_section("2. The __name__ == '__main__' Execution Idiom")

    print(f"Current script's __name__ attribute  : '{__name__}'")
    print(f"Imported module math_utils __name__ : '{math_utils.__name__}'")

    print("\n--- Key Concept ---")
    print("1. When a Python file is executed directly (e.g. `python script.py`),")
    print("   Python sets its `__name__` attribute to `'__main__'`. Code inside `if __name__ == '__main__':` runs.")
    print("2. When a Python file is imported by another script, Python sets `__name__` to the module's name")
    print("   (e.g., `'sample_modules.math_utils'`). Code inside `if __name__ == '__main__':` is SKIPPED.")


# ==============================================================================
# 3. Private Encapsulation & __all__ Export Control
# ==============================================================================
def section_3_private_members_and_all() -> None:
    print_section("3. Private Conventions (_leading) & __all__ Export Control")

    # Inspecting public vs private attributes in custom module
    all_attrs = dir(math_utils)
    public_attrs = [a for a in all_attrs if not a.startswith("_")]
    private_attrs = [a for a in all_attrs if a.startswith("_") and not a.startswith("__")]

    print(f"Public members in math_utils  : {public_attrs}")
    print(f"Private members in math_utils : {private_attrs}")

    # Demonstrating __all__ attribute defined inside math_utils module
    defined_all = getattr(math_utils, "__all__", "Not Defined")
    print(f"\nExplicit __all__ export list in math_utils: {defined_all}")
    print("Explanation: `__all__` defines the explicit list of symbols exported when someone runs `from math_utils import *`.")


# ==============================================================================
# 4. Dynamic Module Reloading at Runtime (importlib.reload)
# ==============================================================================
def section_4_module_reloading() -> None:
    print_section("4. Dynamic Module Reloading with importlib.reload()")

    print(f"Original math_utils module object id in memory: {id(math_utils)}")

    # Reload module dynamically
    reloaded_module = importlib.reload(math_utils)
    print(f"Reloaded math_utils module object id in memory: {id(reloaded_module)}")
    print("Verify reloaded module function execution:")
    print(f"  reloaded_module.add(100, 200) = {reloaded_module.add(100, 200)}")

    print("\nUse Cases for importlib.reload():")
    print("  - Long-running server processes dynamically reloading configuration/plugins.")
    print("  - Interactive REPL/Jupyter Notebook development without restarting the kernel.")


# ==============================================================================
# Main Execution Entry Point
# ==============================================================================
if __name__ == "__main__":
    print("[>>>] DAY 15: MASTERING CUSTOM PYTHON MODULES & SCOPE MECHANICS")
    section_1_consuming_custom_modules()
    section_2_name_main_explanation()
    section_3_private_members_and_all()
    section_4_module_reloading()
    print("\n[OK] Section 2 completed successfully.")
