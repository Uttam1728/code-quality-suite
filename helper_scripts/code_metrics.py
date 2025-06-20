import ast
import json
from pathlib import Path

from utils.file_discovery import get_python_files_from_config


def analyze_code_metrics(config):
    """
    Analyze code metrics including file count, lines of code, functions, and classes.
    
    :param config: Configuration dictionary containing include_dirs, exclude_dirs, etc.
    :return: Dictionary with code metrics
    """
    report_file = Path(config["report_dir"]) / config["code_metrics_output"]

    def count_lines_of_code(file_path):
        """
        Count different types of lines in a Python file:
        - total_lines: All lines in the file (including everything)
        - code_lines: Lines containing actual Python code (excluding comments and empty lines)  
        - comment_lines: Lines starting with # (pure comment lines)
        - empty_lines: Completely empty lines or lines with only whitespace
        """
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                
            total_lines = len(lines)
            code_lines = 0
            comment_lines = 0
            empty_lines = 0
            
            for line in lines:
                stripped = line.strip()
                if not stripped:
                    empty_lines += 1
                elif stripped.startswith('#'):
                    comment_lines += 1
                else:
                    code_lines += 1
                    
            return {
                "total_lines": total_lines,
                "code_lines": code_lines,
                "comment_lines": comment_lines,
                "empty_lines": empty_lines
            }
        except (UnicodeDecodeError, FileNotFoundError):
            return {"total_lines": 0, "code_lines": 0, "comment_lines": 0, "empty_lines": 0}

    def analyze_ast_elements(file_path):
        """Count functions and classes using AST parsing"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                tree = ast.parse(f.read(), filename=str(file_path))
                
            functions = 0
            async_functions = 0
            classes = 0
            methods = 0
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    functions += 1
                    # Check if it's a method (inside a class)
                    for parent in ast.walk(tree):
                        if isinstance(parent, ast.ClassDef):
                            if node in ast.walk(parent):
                                methods += 1
                                break
                elif isinstance(node, ast.AsyncFunctionDef):
                    async_functions += 1
                    # Check if it's an async method
                    for parent in ast.walk(tree):
                        if isinstance(parent, ast.ClassDef):
                            if node in ast.walk(parent):
                                methods += 1
                                break
                elif isinstance(node, ast.ClassDef):
                    classes += 1
                    
            return {
                "functions": functions,
                "async_functions": async_functions,
                "classes": classes,
                "methods": methods
            }
        except (SyntaxError, UnicodeDecodeError, FileNotFoundError):
            return {"functions": 0, "async_functions": 0, "classes": 0, "methods": 0}

    # Initialize counters
    total_files = 0
    total_lines = 0
    total_code_lines = 0
    total_comment_lines = 0
    total_empty_lines = 0
    total_functions = 0
    total_async_functions = 0
    total_classes = 0
    total_methods = 0
    
    # Track biggest files
    biggest_file_by_total_lines = {"file": "", "lines": 0}
    biggest_file_by_code_lines = {"file": "", "lines": 0}
    
    file_details = []
    
    print("📊 Analyzing code metrics...")
    
    # Process all Python files
    python_files = [Path(f) for f in get_python_files_from_config(config)]
    total_files = len(python_files)
    
    if total_files == 0:
        return {"error": "No Python files found"}
    
    for file_path in python_files:
        print(f"⏳ Processing: {file_path}")
        
        # Count lines
        line_metrics = count_lines_of_code(file_path)
        total_lines += line_metrics["total_lines"]
        total_code_lines += line_metrics["code_lines"]
        total_comment_lines += line_metrics["comment_lines"]
        total_empty_lines += line_metrics["empty_lines"]
        
        # Track biggest files
        if line_metrics["total_lines"] > biggest_file_by_total_lines["lines"]:
            biggest_file_by_total_lines = {
                "file": str(file_path),
                "lines": line_metrics["total_lines"]
            }
            
        if line_metrics["code_lines"] > biggest_file_by_code_lines["lines"]:
            biggest_file_by_code_lines = {
                "file": str(file_path),
                "lines": line_metrics["code_lines"]
            }
        
        # Count AST elements
        ast_metrics = analyze_ast_elements(file_path)
        total_functions += ast_metrics["functions"]
        total_async_functions += ast_metrics["async_functions"]
        total_classes += ast_metrics["classes"]
        total_methods += ast_metrics["methods"]
        
        # Store file details
        file_details.append({
            "file": str(file_path),
            "line_metrics": line_metrics,
            "ast_metrics": ast_metrics
        })

    # Calculate averages
    avg_lines_per_file = round(total_lines / total_files, 2) if total_files > 0 else 0
    avg_functions_per_file = round(total_functions / total_files, 2) if total_files > 0 else 0
    avg_classes_per_file = round(total_classes / total_files, 2) if total_files > 0 else 0

    # Prepare result
    result = {
        "summary": {
            "total_files": total_files,
            "total_lines": total_lines,
            "total_code_lines": total_code_lines,
            "total_comment_lines": total_comment_lines,
            "total_empty_lines": total_empty_lines,
            "total_functions": total_functions,
            "total_async_functions": total_async_functions,
            "total_classes": total_classes,
            "total_methods": total_methods,
            "avg_lines_per_file": avg_lines_per_file,
            "avg_functions_per_file": avg_functions_per_file,
            "avg_classes_per_file": avg_classes_per_file,
            "biggest_file_by_total_lines": biggest_file_by_total_lines,
            "biggest_file_by_code_lines": biggest_file_by_code_lines
        },
        "file_details": file_details[:10]  # Only include first 10 files in report to keep it manageable
    }

    # Save report
    report_file.parent.mkdir(parents=True, exist_ok=True)
    with open(report_file, "w") as f:
        json.dump(result, f, indent=2)

    print(f"✅ Code metrics analysis complete!")
    print(f"📁 Files: {total_files}")
    print(f"📝 Code Lines: {total_code_lines}")
    print(f"🔧 Functions: {total_functions} + {total_async_functions} async = {total_functions + total_async_functions} total")
    print(f"🏗️ Classes: {total_classes}")
    print(f"⚙️ Methods: {total_methods}")
    print(f"📊 Biggest File: {biggest_file_by_code_lines['file']} ({biggest_file_by_code_lines['lines']} code lines)")
    print(f"📄 Report saved to: {report_file}")
    
    return result


if __name__ == "__main__":
    # For independent testing - import config here to avoid circular imports
    import sys
    from pathlib import Path
    
    # Add the parent directory to path to import config
    sys.path.append(str(Path(__file__).parent.parent))
    
    print("🧪 Running Code Metrics Analysis independently...")
    print(f"🔍 Analyzing directories: {CONFIG['include_dirs']}")
    print(f"🚫 Excluding: {CONFIG['exclude_dirs']}")
    
    result = analyze_code_metrics(CONFIG)
    
    if "error" not in result:
        print("\n📊 SUMMARY:")
        print(f"Files: {result['summary']['total_files']}")
        print(f"Code Lines: {result['summary']['total_code_lines']}")
        print(f"Functions: {result['summary']['total_functions']} + {result['summary']['total_async_functions']} async")
        print(f"Classes: {result['summary']['total_classes']}")
        print(f"Biggest File: {result['summary']['biggest_file_by_code_lines']['file']} ({result['summary']['biggest_file_by_code_lines']['lines']} code lines)")
    else:
        print("❌ Analysis failed - check your configuration paths")

