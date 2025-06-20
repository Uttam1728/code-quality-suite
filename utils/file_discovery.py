"""
Common file discovery utilities for code quality tools.

This module provides centralized file discovery logic to avoid duplication
across multiple code quality scripts.
"""

import os
from pathlib import Path
from typing import List


def should_exclude_dir(path: Path, exclude_patterns: List[str]) -> bool:
    """
    Check if directory should be excluded from scanning.
    
    :param path: Path to check
    :param exclude_patterns: List of directory patterns to exclude
    :return: True if directory should be excluded
    """
    path_str = str(path)
    path_parts = path.parts
    path_name = path.name
    
    for pattern in exclude_patterns:
        # Exact match of directory name
        if path_name == pattern:
            return True
            
        # Exact match in any path part
        if pattern in path_parts:
            return True
            
        # Handle wildcard patterns (like *.pyc)
        if pattern.startswith('*'):
            if path_name.endswith(pattern[1:]):
                return True
        
        # Handle virtual environment patterns specifically
        venv_patterns = ['venv', '.venv', 'env', '.env', 'virtualenv', '.virtualenv']
        if pattern in venv_patterns:
            # Check if any part of the path contains this virtual env pattern
            for part in path_parts:
                if part == pattern or part.startswith(pattern + '_') or part.endswith('_' + pattern):
                    return True
        
        # General substring check for patterns in path
        if pattern in path_str:
            return True
    
    return False


def get_python_files(include_dirs: List[str], exclude_patterns: List[str]) -> List[str]:
    """
    Get Python files efficiently by skipping excluded directories during traversal.
    
    This function uses os.walk() for compatibility with older Python versions
    and implements the optimized file discovery algorithm that skips excluded
    directories entirely rather than filtering them after discovery.
    
    :param include_dirs: List of directories to scan
    :param exclude_patterns: List of directory patterns to exclude
    :return: List of Python file paths
    """
    py_files = []
    
    for base_dir in include_dirs:
        base_path = Path(base_dir).resolve()
        print(f"🔍 Scanning: {base_path}")
        
        # Walk through directory tree using os.walk for compatibility
        for root, dirs, files in os.walk(base_path):
            root_path = Path(root)
            
            # Remove excluded directories from dirs list to prevent traversal
            dirs[:] = [d for d in dirs if not should_exclude_dir(root_path / d, exclude_patterns)]
            
            # Skip if current directory is excluded
            if should_exclude_dir(root_path, exclude_patterns):
                continue
            
            # Add Python files from current directory
            for file in files:
                if file.endswith('.py'):
                    py_files.append(str(root_path / file))
    
    return py_files


def get_python_files_from_config(config: dict) -> List[str]:
    """
    Get Python files using configuration dictionary.
    
    :param config: Configuration dictionary containing 'include_dirs' and 'exclude_patterns'
    :return: List of Python file paths
    """
    include_dirs = config.get("include_dirs", [])
    exclude_patterns = config.get("exclude_patterns", [])
    
    files = get_python_files(include_dirs, exclude_patterns)
    
    if not files:
        print("❌ No Python files found to analyze")
    else:
        print(f"📁 Found {len(files)} Python files to analyze")
    
    return files 