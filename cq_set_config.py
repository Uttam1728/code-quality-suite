#!/usr/bin/env python3
"""
CQ Config Setter - Dynamically configure Code Quality Suite for any project

Usage:
    python3 cq_set_config.py --project /path/to/project
    python3 cq_set_config.py --project /path/to/project --include dir1,dir2 --exclude pattern1,pattern2
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import List, Optional


def detect_project_structure(project_path: str) -> dict:
    """
    Auto-detect project structure and suggest optimal configuration.
    
    :param project_path: Path to the project
    :return: Detected configuration
    """
    project_path = Path(project_path).resolve()
    
    # Common Python project indicators
    indicators = {
        'setup.py': 'setuptools project',
        'pyproject.toml': 'modern Python project',
        'requirements.txt': 'pip requirements',
        'Pipfile': 'pipenv project',
        'poetry.lock': 'poetry project',
        'manage.py': 'Django project',
        'app.py': 'Flask project',
        'main.py': 'FastAPI/general project',
        '.git': 'Git repository'
    }
    
    detected_features = []
    for indicator, description in indicators.items():
        if (project_path / indicator).exists():
            detected_features.append(description)
    
    # Auto-detect main source directories
    common_src_dirs = ['src', 'app', 'lib', 'core', 'api', 'backend', 'frontend']
    include_dirs = [str(project_path)]  # Always include root
    
    for dir_name in common_src_dirs:
        dir_path = project_path / dir_name
        if dir_path.exists() and dir_path.is_dir():
            # Check if it contains Python files
            python_files = list(dir_path.rglob('*.py'))
            if python_files:
                include_dirs.append(str(dir_path))
    
    return {
        'project_root': str(project_path),
        'detected_features': detected_features,
        'suggested_include_dirs': include_dirs,
        'project_name': project_path.name
    }


def create_dynamic_config(
    project_path: str,
    include_dirs: Optional[List[str]] = None,
    exclude_patterns: Optional[List[str]] = None,
    reports_dir: Optional[str] = None
) -> dict:
    """
    Create dynamic configuration for the project.
    
    :param project_path: Target project path
    :param include_dirs: Custom include directories
    :param exclude_patterns: Additional exclude patterns
    :param reports_dir: Custom reports directory
    :return: Complete configuration dictionary
    """
    project_path = Path(project_path).resolve()
    
    if not project_path.exists():
        raise ValueError(f"Project path does not exist: {project_path}")
    
    # Detect project structure
    detection = detect_project_structure(project_path)
    
    # Set include directories
    if include_dirs:
        # Convert relative paths to absolute
        final_include_dirs = []
        for inc_dir in include_dirs:
            if os.path.isabs(inc_dir):
                final_include_dirs.append(inc_dir)
            else:
                final_include_dirs.append(str(project_path / inc_dir))
    else:
        final_include_dirs = detection['suggested_include_dirs']
    
    # Set exclude patterns
    default_exclude = [
        'venv', 'venv2', '.venv', 'env', '.env', 'virtualenv', '.virtualenv',
        '__pycache__', '*.pyc', '*.pyo', '*.pyd', '.Python',
        'build', 'develop-eggs', 'dist', 'downloads', 'eggs', '.eggs',
        'lib', 'lib64', 'parts', 'sdist', 'var', 'wheels',
        '.installed.cfg', '*.egg-info', '.git', '.gitignore',
        'node_modules', '.npm', '.node_repl_history',
        '.coverage', 'htmlcov', '.pytest_cache', '.tox',
        '.cache', '.mypy_cache', '.dmypy.json', 'dmypy.json',
        '*.log', '*.tmp', '*.temp', '.DS_Store', 'Thumbs.db',
        '.idea', '.vscode', '*.swp', '*.swo', '*~'
    ]
    
    if exclude_patterns:
        final_exclude_patterns = default_exclude + exclude_patterns
    else:
        final_exclude_patterns = default_exclude
    
    # Set reports directory
    if not reports_dir:
        # Default to code_quality_combined/{project_name}_cq_reports in the suite location
        suite_location = Path(__file__).parent.resolve()
        project_name = detection['project_name']
        reports_dir = str(suite_location / 'reports' / f'{project_name}_cq_reports')
    
    # Create configuration
    config = {
        'project_root': str(project_path),
        'project_name': detection['project_name'],
        'include_dirs': final_include_dirs,
        'exclude_patterns': final_exclude_patterns,
        'report_dir': reports_dir,
        'detected_features': detection['detected_features'],
        'suite_location': str(Path(__file__).parent.resolve()),
        
        # Tool-specific outputs
        'pylint_output': 'pylint_report.json',
        'unused_output': 'unused_code_score_report.json',
        'docstring_output': 'docstring_coverage_report.json',
        'api_doc_output': 'api_doc_coverage_report.json',
        'test_coverage_output': 'test_coverage_report.json',
        'code_metrics_output': 'code_metrics_report.json',
        'quality_summary_output': 'code_quality_summary.json',
        'quality_numeric_output': 'code_quality_numeric_summary.json'
    }
    
    return config


def save_config(config: dict, config_file: Optional[str] = None) -> str:
    """
    Save configuration to file.
    
    :param config: Configuration dictionary
    :param config_file: Custom config file path
    :return: Path to saved config file
    """
    if not config_file:
        suite_location = Path(__file__).parent.resolve()
        config_file = str(suite_location / 'cq_active_config.json')
    
    # Ensure reports directory exists
    reports_dir = Path(config['report_dir'])
    reports_dir.mkdir(parents=True, exist_ok=True)
    
    # Save configuration
    with open(config_file, 'w') as f:
        json.dump(config, f, indent=2)
    
    return config_file


def print_config_summary(config: dict):
    """Print a summary of the configuration."""
    print("\n" + "=" * 60)
    print("🔧 CODE QUALITY SUITE CONFIGURATION SET")
    print("=" * 60)
    print(f"🎯 Project: {config['project_name']}")
    print(f"📁 Project Root: {config['project_root']}")
    print(f"🏗️ Suite Location: {config['suite_location']}")
    
    if config.get('detected_features'):
        print(f"🔍 Detected Features:")
        for feature in config['detected_features']:
            print(f"   ✅ {feature}")
    
    print(f"📂 Include Directories ({len(config['include_dirs'])}):")
    for inc_dir in config['include_dirs']:
        print(f"   ✅ {inc_dir}")
    
    print(f"🚫 Exclude Patterns ({len(config['exclude_patterns'])}):")
    for i, pattern in enumerate(config['exclude_patterns'][:5]):
        print(f"   ❌ {pattern}")
    if len(config['exclude_patterns']) > 5:
        print(f"   ... and {len(config['exclude_patterns']) - 5} more")
    
    print(f"📄 Reports Directory: {config['report_dir']}")
    print("=" * 60)
    print("✅ Configuration saved! Run 'python3 cq_run_analysis.py' to analyze.")
    print("=" * 60)


def main():
    """Main function for configuration setup."""
    parser = argparse.ArgumentParser(
        description="Configure Code Quality Suite for any project",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 cq_set_config.py --project /path/to/my/project
  python3 cq_set_config.py --project /path/to/my/project --include src,app --exclude tests
  python3 cq_set_config.py --project ../wayne --reports-dir ./reports
        """
    )
    
    parser.add_argument(
        '--project', '-p',
        required=True,
        help='Path to the project directory to analyze'
    )
    
    parser.add_argument(
        '--include',
        help='Comma-separated list of directories to include (relative to project root or absolute)'
    )
    
    parser.add_argument(
        '--exclude',
        help='Comma-separated list of additional patterns to exclude'
    )
    
    parser.add_argument(
        '--reports-dir',
        help='Directory to save analysis reports (default: suite_location/cq_reports)'
    )
    
    parser.add_argument(
        '--config-file',
        help='Custom path to save configuration file'
    )
    
    parser.add_argument(
        '--show-detection',
        action='store_true',
        help='Show project structure detection details'
    )
    
    args = parser.parse_args()
    
    try:
        # Parse include directories
        include_dirs = None
        if args.include:
            include_dirs = [d.strip() for d in args.include.split(',')]
        
        # Parse exclude patterns
        exclude_patterns = None
        if args.exclude:
            exclude_patterns = [p.strip() for p in args.exclude.split(',')]
        
        # Show detection details if requested
        if args.show_detection:
            print("🔍 Analyzing project structure...")
            detection = detect_project_structure(args.project)
            print(f"\n📂 Project: {detection['project_name']}")
            print(f"📁 Root: {detection['project_root']}")
            print(f"🔍 Detected Features:")
            for feature in detection['detected_features']:
                print(f"   ✅ {feature}")
            print(f"💡 Suggested Include Directories:")
            for inc_dir in detection['suggested_include_dirs']:
                print(f"   📂 {inc_dir}")
            print()
        
        # Create configuration
        config = create_dynamic_config(
            project_path=args.project,
            include_dirs=include_dirs,
            exclude_patterns=exclude_patterns,
            reports_dir=args.reports_dir
        )
        
        # Save configuration
        config_file = save_config(config, args.config_file)
        
        # Show summary
        print_config_summary(config)
        print(f"\n💾 Configuration saved to: {config_file}")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main() 