"""
Day 15 - Python Modules & Packages Masterclass
File 5: 4 Real-World Production Projects

Projects Included:
1. Dynamic Plugin Discovery & Execution Engine (`importlib` plugin architecture).
2. Cross-Platform System Diagnostics & Environment Profiler (`os`, `sys`, `platform`, `statistics`).
3. Layered Environment & Secrets Configuration Loader (Cascading config fallback system).
4. Package Integrity & API Verification Utility (`sys.modules`, `inspect`, export verification).
"""

import sys
import os
import glob
import json
import inspect
import platform
import statistics
import importlib
import importlib.util
from typing import Dict, List, Any, Type, Optional


def print_banner(title: str) -> None:
    """Print project header banner."""
    print(f"\n{'#' * 75}\n# PROJECT: {title}\n{'#' * 75}")


# ==============================================================================
# PROJECT 1: Dynamic Plugin Discovery & Execution Engine
# ==============================================================================
class PluginEngine:
    """Discovers, loads, and executes exporter plugins dynamically from a directory."""

    def __init__(self, plugin_dir: str):
        self.plugin_dir = os.path.abspath(plugin_dir)
        self.registered_plugins: Dict[str, Any] = {}

    def discover_and_load() -> None:
        pass

    def discover_and_load(self) -> None:
        if not os.path.exists(self.plugin_dir):
            print(f"[PluginEngine] Plugin directory '{self.plugin_dir}' does not exist.")
            return

        py_files = glob.glob(os.path.join(self.plugin_dir, "*.py"))
        for file_path in py_files:
            filename = os.path.basename(file_path)
            if filename.startswith("__"):
                continue

            module_name = f"plugins.{filename[:-3]}"
            try:
                # Dynamic load using importlib
                spec = importlib.util.spec_from_file_location(module_name, file_path)
                if spec and spec.loader:
                    mod = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(mod)

                    # Inspect module for plugin classes
                    for attr_name in dir(mod):
                        attr = getattr(mod, attr_name)
                        if inspect.isclass(attr) and hasattr(attr, "plugin_name") and hasattr(attr, "export"):
                            plugin_instance = attr()
                            self.registered_plugins[plugin_instance.plugin_name] = plugin_instance
                            print(f"  [Loaded Plugin] Name: '{plugin_instance.plugin_name}' | Class: {attr.__name__}")
            except Exception as e:
                print(f"  [Plugin Error] Failed loading '{filename}': {e}")

    def execute_exporter(self, plugin_name: str, data: List[Dict[str, Any]]) -> Optional[str]:
        if plugin_name not in self.registered_plugins:
            raise KeyError(f"Plugin '{plugin_name}' is not registered.")
        plugin = self.registered_plugins[plugin_name]
        return plugin.export(data)


def run_project_1() -> None:
    print_banner("1. Dynamic Plugin Discovery & Execution Engine")

    engine = PluginEngine("./plugins")
    print("Discovering and loading plugins dynamically from ./plugins ...")
    engine.discover_and_load()

    # Data payload to export
    sample_dataset = [
        {"id": 101, "name": "Alice Smith", "role": "Backend Engineer", "score": 98.5},
        {"id": 102, "name": "Bob Jones", "role": "DevOps Architect", "score": 94.2},
        {"id": 103, "name": "Charlie Brown", "role": "Data Scientist", "score": 99.1},
    ]

    print(f"\nRegistered Plugin Names: {list(engine.registered_plugins.keys())}")

    # Run JSON Exporter Plugin
    if "json" in engine.registered_plugins:
        json_output = engine.execute_exporter("json", sample_dataset)
        print(f"\n--- JSON Exporter Output ---")
        print(json_output)

    # Run CSV Exporter Plugin
    if "csv" in engine.registered_plugins:
        csv_output = engine.execute_exporter("csv", sample_dataset)
        print(f"\n--- CSV Exporter Output ---")
        print(csv_output)


# ==============================================================================
# PROJECT 2: System Diagnostics & Environment Profiler
# ==============================================================================
class EnvironmentProfiler:
    """Gathers cross-platform system, Python runtime, and environment metrics."""

    @staticmethod
    def generate_report() -> Dict[str, Any]:
        simulated_latencies = [12.4, 15.8, 11.2, 14.5, 13.1, 16.0, 12.9]
        return {
            "platform": {
                "system": platform.system(),
                "release": platform.release(),
                "architecture": platform.architecture()[0],
                "processor": platform.processor() or "Generic CPU",
            },
            "python_runtime": {
                "version": platform.python_version(),
                "executable": sys.executable,
                "byteorder": sys.byteorder,
                "loaded_modules_count": len(sys.modules),
                "sys_path_entries": len(sys.path),
            },
            "latency_diagnostics_ms": {
                "sample_count": len(simulated_latencies),
                "mean_latency": round(statistics.mean(simulated_latencies), 2),
                "stdev_latency": round(statistics.stdev(simulated_latencies), 2),
                "max_latency": max(simulated_latencies),
                "min_latency": min(simulated_latencies),
            },
        }


def run_project_2() -> None:
    print_banner("2. Cross-Platform System Diagnostics & Environment Profiler")

    report = EnvironmentProfiler.generate_report()
    print(json.dumps(report, indent=2))


# ==============================================================================
# PROJECT 3: Layered Environment & Secrets Configuration Loader
# ==============================================================================
class ConfigurationLoader:
    """Cascading configuration engine (Defaults -> File Config -> Environment Overrides)."""

    def __init__(self, default_config: Dict[str, Any]):
        self._config = default_config.copy()

    def merge_file_config(self, file_path: str) -> None:
        if os.path.exists(file_path):
            try:
                with open(file_path, "r") as f:
                    file_data = json.load(f)
                    self._config.update(file_data)
                    print(f"[ConfigLoader] Merged file configuration from '{file_path}'")
            except Exception as e:
                print(f"[ConfigLoader] Error reading '{file_path}': {e}")

    def merge_env_overrides(self, prefix: str = "APP_") -> None:
        count = 0
        for env_key, env_val in os.environ.items():
            if env_key.startswith(prefix):
                config_key = env_key[len(prefix) :].lower()
                self._config[config_key] = env_val
                count += 1
        print(f"[ConfigLoader] Merged {count} environment variable overrides with prefix '{prefix}'")

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    def display() -> None:
        pass

    def display(self) -> None:
        print("\n--- Current Active Application Configuration ---")
        for k, v in self._config.items():
            print(f"  {k:20s} : {v}")


def run_project_3() -> None:
    print_banner("3. Layered Environment & Secrets Configuration Loader")

    defaults = {
        "host": "127.0.0.1",
        "port": 8080,
        "debug": True,
        "max_connections": 100,
        "environment": "development",
    }

    loader = ConfigurationLoader(defaults)

    # Set mock environment overrides for demonstration
    os.environ["APP_PORT"] = "9090"
    os.environ["APP_ENVIRONMENT"] = "production"

    loader.merge_env_overrides(prefix="APP_")
    loader.display()


# ==============================================================================
# PROJECT 4: Package Integrity & API Verification Utility
# ==============================================================================
def run_project_4() -> None:
    print_banner("4. Package Integrity & API Verification Utility")

    # Import target package to inspect
    import sample_modules

    print(f"Auditing package: '{sample_modules.__name__}'")

    # Check export integrity
    declared_all = getattr(sample_modules, "__all__", [])
    print(f"Declared __all__ exports ({len(declared_all)}): {declared_all}")

    export_audit = {}
    for symbol_name in declared_all:
        has_symbol = hasattr(sample_modules, symbol_name)
        if has_symbol:
            obj = getattr(sample_modules, symbol_name)
            obj_type = "class" if inspect.isclass(obj) else "function" if inspect.isfunction(obj) else "variable"
            sig = str(inspect.signature(obj)) if callable(obj) and not inspect.isclass(obj) else "N/A"
            export_audit[symbol_name] = {"status": "VALID", "type": obj_type, "signature": sig}
        else:
            export_audit[symbol_name] = {"status": "MISSING", "type": "UNKNOWN"}

    print("\nAPI Export Audit Results:")
    print(json.dumps(export_audit, indent=2))


# ==============================================================================
# Main Execution Entry Point
# ==============================================================================
if __name__ == "__main__":
    print("[>>>] DAY 15: RUNNING 4 REAL-WORLD PRODUCTION PROJECTS")
    run_project_1()
    run_project_2()
    run_project_3()
    run_project_4()
    print("\n[OK] Section 5 (Practical Projects) completed successfully.")
