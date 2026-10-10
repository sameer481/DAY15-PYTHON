"""
Day 15 - Python Modules & Packages Masterclass
File 1: Built-in Modules, Import Syntax Variants & Module Mechanics

This script covers:
1. Standard built-in modules in Python (`math`, `sys`, `os`, `random`, `datetime`, `platform`, `statistics`).
2. The 5 key import syntax variants and their namespace impacts.
3. Why `from module import *` is a dangerous antipattern (namespace pollution & shadowing).
4. Module search path resolution order (`sys.path`), `sys.modules` cache, and dynamic module loading.
5. Introspection & Reflection: `dir()`, `getattr()`, `hasattr()`, `__name__`, `__file__`, `__doc__`.
"""

import sys
import os
import math
import random
import datetime
import platform
import statistics
from typing import Any, List, Dict


def print_section(title: str) -> None:
    """Print formatted section banner for clear terminal execution output."""
    print(f"\n{'=' * 75}\n  {title}\n{'=' * 75}")


# ==============================================================================
# 1. Essential Standard Library Modules
# ==============================================================================
def section_1_builtin_modules() -> None:
    print_section("1. Essential Standard Library Modules Overview")

    # Math module demonstration
    radius = 5.0
    area = math.pi * (radius ** 2)
    hypotenuse = math.hypot(3, 4)
    print(f"[math] Circle Area (r=5): {area:.4f} | Hypotenuse(3, 4): {hypotenuse}")

    # Random module demonstration
    random_int = random.randint(1, 100)
    samples = random.sample(range(100), 5)
    print(f"[random] Integer: {random_int} | 5 Random Samples: {samples}")

    # Statistics module demonstration
    data = [12.5, 15.0, 18.2, 11.4, 22.0, 15.0]
    mean_val = statistics.mean(data)
    mode_val = statistics.mode(data)
    stdev_val = statistics.stdev(data)
    print(f"[statistics] Mean: {mean_val:.2f} | Mode: {mode_val} | StDev: {stdev_val:.2f}")

    # Datetime module demonstration
    now = datetime.datetime.now()
    formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
    future_date = now + datetime.timedelta(days=30)
    print(f"[datetime] Current Time: {formatted_now} | +30 Days: {future_date.date()}")

    # OS & Platform demonstration
    cwd = os.getcwd()
    os_name = platform.system()
    python_ver = platform.python_version()
    print(f"[os/platform] OS: {os_name} | Python Ver: {python_ver} | CWD: {cwd}")


# ==============================================================================
# 2. Five Import Syntax Variants & Namespace Dynamics
# ==============================================================================
def section_2_import_variants() -> None:
    print_section("2. Import Syntax Variants & Namespace Isolation")

    # Variant 1: Full module import (Keeps module namespace clean)
    import math
    val1 = math.sqrt(144)
    print(f"Variant 1 (import math)                -> math.sqrt(144): {val1}")

    # Variant 2: Module import with alias (Shorthand namespace access)
    import statistics as stats
    val2 = stats.median([10, 20, 30, 40, 50])
    print(f"Variant 2 (import statistics as stats) -> stats.median(...): {val2}")

    # Variant 3: Specific function/symbol import (Direct name binding)
    from math import sqrt, ceil, floor
    val3 = sqrt(81) + ceil(4.2)
    print(f"Variant 3 (from math import sqrt...)   -> sqrt(81) + ceil(4.2): {val3}")

    # Variant 4: Specific symbol import with alias (Prevents naming conflicts)
    from datetime import datetime as dt
    val4 = dt.now().year
    print(f"Variant 4 (from datetime import dt)    -> dt.now().year: {val4}")

    # Variant 5: Star import (ANTIPATTERN - DEMONSTRATION ONLY)
    # WARNING: from math import * imports all public symbols into the global namespace.
    # It pollutes scope, hides function sources, and can overwrite built-in functions like pow() or min().
    print("Variant 5 (from module import *)        -> BAD PRACTICE: Namespace pollution!")


# ==============================================================================
# 3. Python Module Search Path (sys.path) & sys.modules Cache
# ==============================================================================
def section_3_sys_path_and_cache() -> None:
    print_section("3. Module Resolution (sys.path) & Caching (sys.modules)")

    print("--- Module Search Priority Order in sys.path ---")
    for idx, path_entry in enumerate(sys.path[:6]):
        desc = "Current Working Directory / Script Dir" if idx == 0 else "Standard Lib / Site-Packages"
        print(f"  [{idx}] {path_entry} ({desc})")

    # Inspecting loaded module cache sys.modules
    print("\n--- sys.modules In-Memory Cache Verification ---")
    print(f"Total modules currently cached in memory: {len(sys.modules)}")
    is_math_cached = "math" in sys.modules
    is_os_cached = "os" in sys.modules
    print(f"Is 'math' cached in sys.modules? {is_math_cached}")
    print(f"Is 'os' cached in sys.modules?   {is_os_cached}")
    if is_math_cached:
        print(f"Memory object reference for 'math': {sys.modules['math']}")

    # Dynamic manipulation of sys.path (Adding custom search directory at runtime)
    custom_dir = os.path.abspath("./custom_external_libs")
    if custom_dir not in sys.path:
        sys.path.insert(0, custom_dir)
        print(f"\n[sys.path] Dynamically prepended custom path: {custom_dir}")
        print(f"[sys.path] Highest priority search directory is now: {sys.path[0]}")


# ==============================================================================
# 4. Introspection & Reflection: Inspecting Module Metadata
# ==============================================================================
def section_4_introspection() -> None:
    print_section("4. Module Introspection & Reflection Tools")

    import math

    # 1. dir(): List all valid attributes/functions in module
    math_attributes = dir(math)
    public_funcs = [attr for attr in math_attributes if not attr.startswith("_")]
    print(f"Total attributes in 'math' module: {len(math_attributes)}")
    print(f"Sample public math functions      : {public_funcs[:8]}")

    # 2. Module Metadata Attributes (__name__, __doc__, __file__)
    print("\n--- Module Metadata Attributes ---")
    print(f"Module Name (__name__) : {math.__name__}")
    print(f"Module Docstring (__doc__): {math.__doc__.strip() if math.__doc__ else 'N/A'}")
    # Note: Built-in C modules (like math) may not have a __file__ attribute or show [built-in]
    file_path = getattr(math, "__file__", "[Built-in C Module]")
    print(f"Module File Path (__file__): {file_path}")

    # 3. Dynamic Reflection with hasattr() and getattr()
    function_to_call = "factorial"
    if hasattr(math, function_to_call):
        func_ref = getattr(math, function_to_call)
        result = func_ref(6)
        print(f"\n[getattr] Dynamically resolved math.{function_to_call}(6) = {result}")

    # 4. Current Script Metadata
    print("\n--- Current Script Metadata ---")
    print(f"Current Script __name__ : {__name__}")
    print(f"Current Script __file__ : {os.path.abspath(__file__)}")


# ==============================================================================
# Main Execution Entry Point
# ==============================================================================
if __name__ == "__main__":
    print("[>>>] DAY 15: MASTERING PYTHON BUILT-IN MODULES & IMPORT MECHANICS")
    section_1_builtin_modules()
    section_2_import_variants()
    section_3_sys_path_and_cache()
    section_4_introspection()
    print("\n[OK] Section 1 completed successfully.")
