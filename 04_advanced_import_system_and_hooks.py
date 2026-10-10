"""
Day 15 - Python Modules & Packages Masterclass
File 4: Advanced Import Mechanics, Dynamic Imports & Circular Dependency Resolution

This script covers:
1. Dynamic Imports at Runtime using `importlib.import_module()`.
2. Module Specification Inspection (`importlib.util.find_spec`, `spec_from_file_location`).
3. Circular Import Anatomy, Detection & 3 Resolution Strategies.
4. Custom Meta Path Import Hooks (`sys.meta_path`) for interception & virtual modules.
5. Defensive / Conditional Imports (`try ... except ImportError`) for optional dependencies.
"""

import sys
import os
import importlib
import importlib.util
import importlib.machinery
from typing import Any, Optional


def print_section(title: str) -> None:
    """Print formatted section banner."""
    print(f"\n{'=' * 75}\n  {title}\n{'=' * 75}")


# ==============================================================================
# 1. Dynamic Imports with importlib.import_module()
# ==============================================================================
def section_1_dynamic_imports() -> None:
    print_section("1. Programmatic Dynamic Imports with importlib")

    module_names = ["math", "json", "sample_modules.string_utils"]
    loaded_modules = {}

    for mod_name in module_names:
        # Dynamically import module from string name
        mod_obj = importlib.import_module(mod_name)
        loaded_modules[mod_name] = mod_obj
        print(f"[importlib] Dynamically loaded '{mod_name}' -> {mod_obj}")

    # Invoke function on dynamically loaded module
    json_mod = loaded_modules["json"]
    encoded = json_mod.dumps({"status": "SUCCESS", "code": 200})
    print(f"\n[json.dumps call] {encoded}")

    str_utils_mod = loaded_modules["sample_modules.string_utils"]
    cleaned = str_utils_mod.clean_text("  Dynamic Loading Works!  ")
    print(f"[string_utils call] Cleaned text: '{cleaned}'")


# ==============================================================================
# 2. Module Specifications (ModuleSpec) & Arbitrary File Loading
# ==============================================================================
def section_2_module_specs() -> None:
    print_section("2. Module Specifications (find_spec & spec_from_file_location)")

    # 1. Finding spec of existing module
    spec = importlib.util.find_spec("math")
    if spec:
        print(f"Spec Name    : {spec.name}")
        print(f"Spec Loader  : {spec.loader}")
        print(f"Spec Origin  : {spec.origin}")

    # 2. Loading a module from an arbitrary file path on disk
    target_file = os.path.abspath("./sample_modules/math_utils.py")
    spec_from_file = importlib.util.spec_from_file_location("custom_math_standalone", target_file)

    if spec_from_file and spec_from_file.loader:
        # Create module object from spec
        custom_mod = importlib.util.module_from_spec(spec_from_file)
        # Execute module code in its own namespace
        spec_from_file.loader.exec_module(custom_mod)
        print(f"\n[spec_from_file_location] Dynamically loaded file from disk:")
        print(f"  Module Object : {custom_mod}")
        print(f"  Function Call : custom_mod.add(50, 50) = {custom_mod.add(50, 50)}")


# ==============================================================================
# 3. Circular Imports: Anatomy, Diagnosis & Resolution Strategies
# ==============================================================================
def section_3_circular_imports() -> None:
    print_section("3. Circular Import Anatomy & 3 Resolution Strategies")

    print("--- How Circular Imports Cause AttributeError / ImportError ---")
    print("Scenario: Module A imports Module B at top-level; Module B imports Module A at top-level.")
    print("Execution Flow:")
    print("  1. Main starts importing A.")
    print("  2. A runs top-level code until `import B`.")
    print("  3. Python pauses A execution, adds uncompleted A to `sys.modules`, and begins loading B.")
    print("  4. B runs top-level code until `import A`.")
    print("  5. B looks up A in `sys.modules`, finds uncompleted A object, and tries to access functions from A.")
    print("  6. CRASH! Functions in A haven't been evaluated yet -> AttributeError / ImportError!")

    print("\n--- 3 Production Strategies to Resolve Circular Imports ---")
    print("Strategy 1: Function-Level (Deferred / Lazy) Imports")
    print("            Move `import B` inside the specific function that uses B, delaying import until call time.")
    print("Strategy 2: Structural Refactoring (Extract Shared Interface)")
    print("            Move common dependencies/classes into a third module (e.g. `base.py` or `models.py`).")
    print("Strategy 3: Bottom Import Placement (Post-Initialization)")
    print("            Place `import B` at the bottom of Module A after functions/classes are defined.")


# ==============================================================================
# 4. Custom Meta Path Import Hooks (sys.meta_path)
# ==============================================================================
class VirtualModuleFinder:
    """Custom import hook finder for intercepting imports of virtual modules."""

    virtual_module_name = "virtual_system_config"

    def find_spec(self, fullname: str, path: Any, target: Any = None):
        if fullname == self.virtual_module_name:
            # Create synthetic ModuleSpec for virtual module
            return importlib.machinery.ModuleSpec(fullname, VirtualModuleLoader())
        return None


class VirtualModuleLoader:
    """Custom loader that dynamically synthesizes module attributes in RAM without disk files."""

    def create_module(self, spec):
        return None  # Standard default module creation

    def exec_module(self, module):
        # Inject dynamic variables and functions into the virtual module
        module.APP_NAME = "Masterclass Virtual Engine"
        module.VERSION = "3.15.0"
        module.get_status = lambda: "VIRTUAL_MODULE_ACTIVE"


def section_4_import_hooks() -> None:
    print_section("4. Custom Meta Path Import Hooks (sys.meta_path)")

    # Install custom import finder into sys.meta_path
    finder = VirtualModuleFinder()
    sys.meta_path.insert(0, finder)
    print(f"[sys.meta_path] Installed VirtualModuleFinder into position 0")

    # Import non-existent virtual module dynamically!
    import virtual_system_config

    print(f"\n[Virtual Module Successfully Intercepted & Loaded!]")
    print(f"  Module Reference : {virtual_system_config}")
    print(f"  APP_NAME         : {virtual_system_config.APP_NAME}")
    print(f"  VERSION          : {virtual_system_config.VERSION}")
    print(f"  Status Function  : {virtual_system_config.get_status()}")

    # Clean up sys.meta_path
    sys.meta_path.remove(finder)


# ==============================================================================
# 5. Defensive & Conditional Imports (Optional Dependencies)
# ==============================================================================
def section_5_defensive_imports() -> None:
    print_section("5. Defensive & Conditional Imports for Optional Dependencies")

    # Pattern for handling optional third-party packages (e.g., numpy, pandas, or ujson)
    try:
        import ujson as json_engine
        engine_type = "ujson (High Speed C Engine)"
    except ImportError:
        import json as json_engine
        engine_type = "json (Standard Library Fallback)"

    print(f"Selected JSON Engine: {engine_type}")
    print(f"Engine Test Output  : {json_engine.dumps({'engine': engine_type})}")


# ==============================================================================
# Main Execution Entry Point
# ==============================================================================
if __name__ == "__main__":
    print("[>>>] DAY 15: ADVANCED IMPORT MECHANICS & CUSTOM HOOKS")
    section_1_dynamic_imports()
    section_2_module_specs()
    section_3_circular_imports()
    section_4_import_hooks()
    section_5_defensive_imports()
    print("\n[OK] Section 4 completed successfully.")
