import subprocess
import re
import json
from pathlib import Path
from collections import defaultdict
import math
from typing import Dict, List, Any

from utils.file_discovery import get_python_files_from_config

def run_pylint_analysis(config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Run pylint analysis on Python files and generate a comprehensive report.
    
    :param config: Configuration dictionary containing analysis settings
    :return: Dictionary with pylint analysis results
    """
    batch_size = config["batch_size"]
    report_file = Path(config["report_dir"]) / config["pylint_output"]

    def run_batches(files: List[str]) -> str:
        """
        Process files in batches to avoid command line length limits.
        
        :param files: List of Python file paths to analyze
        :return: Combined pylint output from all batches
        """
        output = ""
        total_files = len(files)
        total_batches = math.ceil(total_files / batch_size)
        
        print(f"📊 Starting pylint analysis on {total_files} Python files")
        print(f"🔄 Processing in {total_batches} batches of up to {batch_size} files each")
        
        for i in range(0, len(files), batch_size):
            batch_num = (i // batch_size) + 1
            batch = files[i:i + batch_size]
            batch_file_count = len(batch)
            
            print(f"⏳ Processing batch {batch_num}/{total_batches} ({batch_file_count} files)...")
            
            result = subprocess.run(["pylint", *batch], capture_output=True, text=True)
            output += result.stdout
            
            print(f"✅ Batch {batch_num}/{total_batches} completed")
            
        print(f"🎉 All {total_batches} batches processed successfully!")
        return output

    def parse_output(output: str) -> Dict[str, Any]:
        """
        Parse pylint output and extract structured results.
        
        :param output: Raw pylint output text
        :return: Structured dictionary with analysis results
        """
        # Map pylint category codes to descriptive names
        category_map = {
            'C': 'Convention',
            'R': 'Refactor', 
            'W': 'Warning',
            'E': 'Error',
            'F': 'Fatal'
        }
        
        results = {
            "score": None,
            "score_percentage": None,
            "category_counts": defaultdict(int),
            "total_issues": 0,
            "issue_locations": []
        }
        scores = re.findall(r"Your code has been rated at ([\d\.]+)/10", output)
        if scores:
            avg_score = round(sum(map(float, scores)) / len(scores), 2)
            results["score"] = avg_score
            results["score_percentage"] = round(avg_score * 10, 1)  # Convert to percentage

        for line in output.splitlines():
            match = re.match(r"(.+?):(\d+):(\d+): ([CRWEF])\d+: (.+?) \((.+)\)", line)
            if match:
                file_path, line_no, col, code_type, message, msg_symbol = match.groups()
                # Use descriptive category name instead of single letter
                category_name = category_map.get(code_type, code_type)
                results["category_counts"][category_name] += 1
                results["total_issues"] += 1
                results["issue_locations"].append({
                    "file": file_path,
                    "line": int(line_no),
                    "col": int(col),
                    "type": code_type,
                    "type_name": category_name,
                    "message": message,
                    "symbol": msg_symbol
                })
        return results

    files = get_python_files_from_config(config)
    if not files:
        return {"score": 0.0, "error": "No Python files found."}

    output = run_batches(files)
    
    print("📈 Parsing pylint results...")
    result = parse_output(output)

    report_file.parent.mkdir(parents=True, exist_ok=True)
    with open(report_file, "w") as f:
        json.dump(result, f, indent=2)

    print(f"✅ Pylint analysis complete! Score: {result['score_percentage']}% ({result['score']}/10) with {result['total_issues']} issues")
    print(f"📄 Report saved to: {report_file}")
    return result
