import subprocess
import json
import sys
from pathlib import Path
import re
from typing import Dict, List, Any

from utils.file_discovery import get_python_files_from_config


def analyze_unused_imports(config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Analyze unused imports and code using vulture.
    
    :param config: Configuration dictionary containing analysis settings
    :return: Dictionary with vulture analysis results
    """
    return run_vulture_analysis(config)


def run_vulture_analysis(config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Run vulture analysis to find unused code.
    
    :param config: Configuration dictionary containing analysis settings
    :return: Dictionary with vulture analysis results
    """
    vulture_output = config.get("unused_output", "unused_code_report.json")
    report_file = Path(config["report_dir"]) / vulture_output

    def run_vulture(files: List[str]) -> str:
        """
        Execute vulture on the provided files.
        
        :param files: List of Python file paths to analyze
        :return: Vulture output as string
        """
        print(f"📊 Running vulture on {len(files)} Python files")
        # Use python -m vulture to ensure we use the current environment
        result = subprocess.run([sys.executable, "-m", "vulture", *files], capture_output=True, text=True)
        
        # Debug: Print raw output info
        import os
        print(f"      🔍 Vulture stdout length: {len(result.stdout)}")
        print(f"      🔍 Vulture stderr: {result.stderr[:200] if result.stderr else 'None'}")
        print(f"      🔍 Vulture return code: {result.returncode}")
        print(f"      🔍 Working directory: {os.getcwd()}")
        if result.stdout:
            print(f"      🔍 First 200 chars of output: {result.stdout[:200]}")
        else:
            print(f"      🔍 No stdout output from vulture!")

        return result.stdout

    def parse_output(output: str) -> List[Dict[str, Any]]:
        """
        Parse vulture output to extract unused code items.
        
        :param output: Raw vulture output text
        :return: List of unused code items with details
        """
        unused = []
        for line in output.strip().splitlines():
            match = re.match(r"(.+?):(\d+): (.+) \((.+)\)", line)
            if match:
                file, line_no, message, symbol = match.groups()
                unused.append({
                    "file": file,
                    "line": int(line_no),
                    "message": message,
                    "symbol": symbol
                })
        return unused

    files = get_python_files_from_config(config)
    if not files:
        return {"error": "No Python files found."}
        
    output = run_vulture(files)
    unused_items = parse_output(output)

    result = {
        "total_defined_files": len(files),
        "unused_items_count": len(unused_items),
        "unused_items": unused_items[:5]
    }

    report_file.parent.mkdir(parents=True, exist_ok=True)
    with open(report_file, "w") as f:
        json.dump(result, f, indent=2)

    print(f"✅ Vulture complete. Found {len(unused_items)} unused items.")
    return result
#
# def get_python_files(include_dirs, should_exclude):
#     files = []
#     for dir in include_dirs:
#         for path in Path(dir).rglob("*.py"):
#             if not should_exclude(path):
#                 files.append(str(path))
#     return files
# if __name__ == "__main__":
#     include_dirs = [".."],
#     exclude_dirs = ["venv", "__pycache__", "build", "dist", "tests", "tree-sitter-grammar", "alembic"],
#
#     py_files = get_python_files(include_dirs, exclude_dirs)