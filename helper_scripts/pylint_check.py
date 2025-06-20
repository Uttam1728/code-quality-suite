import subprocess
import json
import sys
import re
import os
import concurrent.futures
from pathlib import Path
from typing import Dict, List, Any

from utils.file_discovery import get_python_files_from_config


def analyze_with_pylint(config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Run pylint analysis on Python files.
    
    :param config: Configuration dictionary containing analysis settings
    :return: Dictionary with pylint analysis results
    """
    report_file = Path(config["report_dir"]) / "pylint_report.json"
    
    def run_pylint_on_file(file_path: str) -> Dict[str, Any]:
        """
        Execute pylint on a single file.
        
        :param file_path: Path to Python file to analyze
        :return: Pylint results for the file
        """
        # Use the venv2 python to ensure we have pylint available
        venv_python = "/Users/ushankradadiya/Downloads/repos/cerebrum/venv2/bin/python3"
        cmd = [
            venv_python, "-m", "pylint", 
            "--output-format=json", 
            "--score=no",  # Don't need score for individual files
            "--persistent=no",
            "--disable=import-error",  # Disable import errors that might cause contamination
            file_path
        ]
        
        # Run from current working directory (cerebrum) to maintain venv context
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=os.getcwd())
        
        # Parse JSON from stdout with contamination filtering
        issues = []
        try:
            if result.stdout.strip():
                # Try to extract JSON from potentially contaminated output
                cleaned_output = extract_json_from_contaminated_output(result.stdout)
                if cleaned_output:
                    issues = json.loads(cleaned_output)
        except json.JSONDecodeError:
            # If JSON parsing still fails, try alternative extraction methods
            issues = extract_issues_from_mixed_output(result.stdout)
        
        return {
            "issues": issues,
            "return_code": result.returncode,
            "file_path": file_path,
            "raw_stdout": result.stdout[:200] if result.stdout else "",  # Keep first 200 chars for debugging
            "stderr": result.stderr[:200] if result.stderr else ""
        }

    def process_batch(batch_files: List[str]) -> tuple:
        """
        Process a batch of files in parallel.
        
        :param batch_files: List of file paths to process
        :return: Tuple of (all_issues, successful_count, failed_files)
        """
        batch_issues = []
        batch_successful = 0
        batch_failed = []
        
        # Use ThreadPoolExecutor for I/O bound tasks
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            # Submit all files in batch
            future_to_file = {executor.submit(run_pylint_on_file, file_path): file_path 
                            for file_path in batch_files}
            
            # Collect results
            for future in concurrent.futures.as_completed(future_to_file):
                file_path = future_to_file[future]
                try:
                    result = future.result()
                    # Check if pylint ran successfully (return codes 0-31 are valid)
                    if result["return_code"] <= 31:  # Valid pylint return codes
                        if result["issues"]:  # If we extracted any issues
                            batch_issues.extend(result["issues"])
                        batch_successful += 1
                    else:
                        # Debug info for failed files
                        print(f"      ⚠️ Failed to analyze {file_path}: return_code={result['return_code']}")
                        if result.get('raw_stdout'):
                            print(f"         stdout: {result['raw_stdout'][:100]}...")
                        batch_failed.append(file_path)
                except Exception as e:
                    print(f"      ⚠️ Exception analyzing {file_path}: {str(e)}")
                    batch_failed.append(file_path)
        
        return batch_issues, batch_successful, batch_failed
    
    def calculate_overall_score(all_issues: List[Dict], files_count: int) -> float:
        """
        Calculate overall pylint score based on issues.
        This is a simplified scoring - pylint's actual scoring is more complex.
        
        :param all_issues: List of all issues found
        :param files_count: Number of files analyzed
        :return: Estimated score out of 10
        """
        if files_count == 0:
            return 10.0
        
        # Count issues by severity (simplified scoring)
        error_count = sum(1 for issue in all_issues if issue.get("type") == "error")
        warning_count = sum(1 for issue in all_issues if issue.get("type") == "warning")
        convention_count = sum(1 for issue in all_issues if issue.get("type") == "convention")
        refactor_count = sum(1 for issue in all_issues if issue.get("type") == "refactor")
        
        # Simplified scoring (errors are weighted more heavily)
        penalty = (error_count * 2) + (warning_count * 1) + (convention_count * 0.5) + (refactor_count * 0.5)
        
        # Calculate score (rough approximation)
        base_score = 10.0
        penalty_per_file = penalty / files_count
        estimated_score = max(0.0, base_score - (penalty_per_file * 0.5))
        
        return round(estimated_score, 2)
    
    files = get_python_files_from_config(config)
    if not files:
        return {"error": "No Python files found."}
    
    # Get file limit from config or use default
    file_limit = config.get("pylint_file_limit", 100)  # Default to 100 files
    
    # Limit files to avoid excessive processing time
    if len(files) > file_limit:
        print(f"⚠️ Too many files ({len(files)}), analyzing first {file_limit}...")
        print(f"   💡 To analyze more files, add 'pylint_file_limit': {len(files)} to your config")
        files = files[:file_limit]
    
    print(f"📊 Running pylint on {len(files)} Python files (batch processing)")
    
    # Process files in batches of 50
    batch_size = 50
    all_issues = []
    total_successful = 0
    all_failed_files = []
    
    # Split files into batches
    for i in range(0, len(files), batch_size):
        batch_files = files[i:i + batch_size]
        batch_num = (i // batch_size) + 1
        total_batches = (len(files) + batch_size - 1) // batch_size
        
        print(f"   📦 Processing batch {batch_num}/{total_batches} ({len(batch_files)} files)...")
        
        # Process the batch
        batch_issues, batch_successful, batch_failed = process_batch(batch_files)
        
        # Accumulate results
        all_issues.extend(batch_issues)
        total_successful += batch_successful
        all_failed_files.extend(batch_failed)
        
        print(f"   ✅ Batch {batch_num} complete: {batch_successful} files analyzed, {len(batch_failed)} failed")
    
    # Calculate overall score
    estimated_score = calculate_overall_score(all_issues, total_successful)
    
    # Categorize issues by type
    issue_counts = {
        "convention": 0,
        "refactor": 0,
        "warning": 0,
        "error": 0,
        "fatal": 0
    }
    
    for issue in all_issues:
        issue_type = issue.get("type", "unknown")
        if issue_type in issue_counts:
            issue_counts[issue_type] += 1
    
    result = {
        "issues": all_issues,
        "issue_counts": issue_counts,
        "score": estimated_score,
        "total_issues": len(all_issues),
        "files_analyzed": total_successful,
        "failed_files": all_failed_files,
        "analysis_method": "batch_processing",
        "batch_size": batch_size
    }
    
    # Save detailed report
    report_file.parent.mkdir(parents=True, exist_ok=True)
    with open(report_file, "w") as f:
        json.dump(result, f, indent=2)
    
    # Display results
    score = result.get("score", "N/A")
    total_issues = result.get("total_issues", 0)
    issue_counts = result.get("issue_counts", {})
    
    print(f"✅ Pylint complete. Score: {score}/10, Issues: {total_issues}")
    if total_issues > 0 and issue_counts:
        print(f"   📊 Issue breakdown:")
        for issue_type, count in issue_counts.items():
            if count > 0:
                print(f"      {issue_type.capitalize()}: {count}")
    
    if all_failed_files:
        print(f"   ⚠️ Failed to analyze {len(all_failed_files)} files")
    
    return result 

def extract_json_from_contaminated_output(output: str) -> str:
    """
    Extract valid JSON from output that may contain print statements or other contamination.
    
    :param output: Raw output that may contain JSON mixed with other text
    :return: Clean JSON string or empty string if no valid JSON found
    """
    if not output:
        return ""
    
    lines = output.strip().split('\n')
    
    # Method 1: Look for lines that start with '[' (JSON array start)
    for i, line in enumerate(lines):
        line = line.strip()
        if line.startswith('['):
            # Try to parse from this line to end
            potential_json = '\n'.join(lines[i:])
            try:
                # Test if it's valid JSON
                json.loads(potential_json)
                return potential_json
            except json.JSONDecodeError:
                continue
    
    # Method 2: Look for complete JSON blocks between brackets
    json_start = -1
    bracket_count = 0
    for i, char in enumerate(output):
        if char == '[':
            if bracket_count == 0:
                json_start = i
            bracket_count += 1
        elif char == ']':
            bracket_count -= 1
            if bracket_count == 0 and json_start != -1:
                potential_json = output[json_start:i+1]
                try:
                    json.loads(potential_json)
                    return potential_json
                except json.JSONDecodeError:
                    continue
    
    # Method 3: Try to find JSON-like patterns and clean them
    import re
    json_pattern = r'\[(?:[^[\]]*|\[[^[\]]*\])*\]'
    matches = re.findall(json_pattern, output, re.DOTALL)
    
    for match in matches:
        try:
            json.loads(match)
            return match
        except json.JSONDecodeError:
            continue
    
    return ""

def extract_issues_from_mixed_output(output: str) -> List[Dict]:
    """
    Extract pylint issues from mixed output using pattern matching.
    
    :param output: Raw output containing mixed content
    :return: List of issue dictionaries
    """
    issues = []
    
    # If we can't parse JSON, try to extract individual issue lines
    # Look for pylint message patterns
    import re
    
    # Pattern for pylint messages (simplified)
    message_pattern = r'([^:]+):(\d+):(\d+):\s*([CRWEF]\d+):\s*(.+)'
    
    for line in output.split('\n'):
        match = re.match(message_pattern, line)
        if match:
            file_path, line_num, col_num, msg_id, message = match.groups()
            
            # Map pylint message types
            type_map = {
                'C': 'convention',
                'R': 'refactor', 
                'W': 'warning',
                'E': 'error',
                'F': 'fatal'
            }
            
            issue_type = type_map.get(msg_id[0], 'unknown')
            
            issues.append({
                "type": issue_type,
                "module": file_path,
                "obj": "",
                "line": int(line_num),
                "column": int(col_num),
                "path": file_path,
                "symbol": msg_id,
                "message": message.strip(),
                "message-id": msg_id
            })
    
    return issues 