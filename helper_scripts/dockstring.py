
import ast
import json
from pathlib import Path

from utils.file_discovery import get_python_files_from_config

def check_docstring_coverage(config):
    report_file = Path(config["report_dir"]) / config["docstring_output"]

    total_functions = 0
    documented_functions = 0
    undocumented_items = []

    for file in [Path(f) for f in get_python_files_from_config(config)]:
        try:
            with open(file, "r", encoding="utf-8") as f:
                tree = ast.parse(f.read(), filename=str(file))
                for node in ast.walk(tree):
                    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        total_functions += 1
                        if ast.get_docstring(node):
                            documented_functions += 1
                        else:
                            undocumented_items.append({
                                "file": str(file),
                                "function": node.name,
                                "line": node.lineno
                            })
        except (SyntaxError, UnicodeDecodeError):
            continue

    undocumented_count = len(undocumented_items)
    coverage = round((documented_functions / total_functions) * 100, 2) if total_functions else 100.0

    result = {
        "total_functions": total_functions,
        "documented_functions": documented_functions,
        "undocumented_functions": undocumented_count,
        "docstring_coverage_percent": coverage,
        "undocumented_function_details": undocumented_items
    }

    report_file.parent.mkdir(parents=True, exist_ok=True)
    with open(report_file, "w") as f:
        json.dump(result, f, indent=2)

    print(f"✅ Docstring coverage complete: {coverage}%")
    return result
