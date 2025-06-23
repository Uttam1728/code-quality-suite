#!/usr/bin/env python3
"""
CQ Analysis Runner - Run code quality analysis based on saved configuration

Usage:
    python3 cq_run_analysis.py
    python3 cq_run_analysis.py --tools pylint,docstrings
    python3 cq_run_analysis.py --preset quick
    python3 cq_run_analysis.py --interactive
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Dict

# Import analysis modules
from helper_scripts.code_metrics import analyze_code_metrics
from helper_scripts.dockstring import check_docstring_coverage
# Note: Import other modules as needed when they're available


def load_active_config(config_file: Optional[str] = None) -> dict:
    """
    Load the active configuration.
    
    :param config_file: Custom config file path
    :return: Configuration dictionary
    """
    if not config_file:
        suite_location = Path(__file__).parent.resolve()
        config_file = str(suite_location / 'cq_active_config.json')
    
    config_path = Path(config_file)
    if not config_path.exists():
        raise FileNotFoundError(
            f"No active configuration found at {config_file}. "
            f"Please run 'python3 cq_set_config.py --project /path/to/project' first."
        )
    
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    return config


def display_available_tools() -> Dict[str, str]:
    """Display available analysis tools."""
    tools = {
        'code_metrics': '📊 Code Metrics - Lines, functions, classes analysis',
        'docstrings': '📝 Docstring Coverage - Documentation coverage analysis',
        'pylint': '🔍 Pylint - Code quality and style analysis (requires pylint)',
        'unused': '🧹 Unused Code - Dead code detection (requires vulture)',
        'test_coverage': '🧪 Test Coverage - Test coverage analysis (requires coverage)',
        'api_doc': '📋 API Documentation - OpenAPI documentation coverage'
    }
    return tools


def display_presets() -> Dict[str, List[str]]:
    """Display available tool presets."""
    presets = {
        'quick': ['code_metrics', 'docstrings'],
        'standard': ['code_metrics', 'docstrings', 'pylint'],
        'comprehensive': ['code_metrics', 'docstrings', 'pylint', 'unused', 'api_doc'],
        'documentation': ['docstrings', 'api_doc'],
        'quality': ['pylint', 'unused'],
        'all': ['code_metrics', 'docstrings', 'pylint', 'unused', 'test_coverage', 'api_doc']
    }
    return presets


def run_code_metrics(config: dict) -> bool:
    """Run code metrics analysis."""
    try:
        print("📊 Running Code Metrics...")
        analyze_code_metrics(config)
        print("✅ Code Metrics completed")
        return True
    except Exception as e:
        print(f"❌ Code Metrics failed: {str(e)}")
        return False


def run_docstring_analysis(config: dict) -> bool:
    """Run docstring coverage analysis."""
    try:
        print("📝 Running Docstring Coverage...")
        check_docstring_coverage(config)
        print("✅ Docstring Coverage completed")
        return True
    except Exception as e:
        print(f"❌ Docstring Coverage failed: {str(e)}")
        return False


def run_pylint_analysis(config: dict) -> bool:
    """Run pylint analysis."""
    try:
        print("🔍 Running Pylint...")
        # Import here to avoid dependency issues
        from helper_scripts.pylint_check import analyze_with_pylint
        analyze_with_pylint(config)
        print("✅ Pylint completed")
        return True
    except ImportError:
        print("❌ Pylint not available - install with: pip install pylint")
        return False
    except Exception as e:
        print(f"❌ Pylint failed: {str(e)}")
        return False


def run_unused_code_analysis(config: dict) -> bool:
    """Run unused code analysis."""
    try:
        print("🧹 Running Unused Code Analysis...")
        from helper_scripts.unused import analyze_unused_imports
        analyze_unused_imports(config)
        print("✅ Unused Code Analysis completed")
        return True
    except ImportError:
        print("❌ Vulture not available - install with: pip install vulture")
        return False
    except Exception as e:
        print(f"❌ Unused Code Analysis failed: {str(e)}")
        return False


def run_test_coverage_analysis(config: dict) -> bool:
    """Run test coverage analysis."""
    try:
        print("🧪 Running Test Coverage...")
        from helper_scripts.test_covearge import run_coverage_analysis
        run_coverage_analysis(config)
        print("✅ Test Coverage completed")
        return True
    except ImportError:
        print("❌ Coverage not available - install with: pip install coverage pytest-cov")
        return False
    except Exception as e:
        print(f"❌ Test Coverage failed: {str(e)}")
        return False


def run_api_doc_analysis(config: dict) -> bool:
    """Run API documentation analysis."""
    try:
        print("📋 Running API Documentation Analysis...")
        from helper_scripts.api_doc import analyze_openapi_coverage
        analyze_openapi_coverage(config)
        print("✅ API Documentation completed")
        return True
    except Exception as e:
        print(f"❌ API Documentation failed: {str(e)}")
        return False


def run_analysis_tools(tool_names: List[str], config: dict) -> Dict[str, bool]:
    """
    Run specified analysis tools.
    
    :param tool_names: List of tool names to run
    :param config: Configuration dictionary
    :return: Dictionary of tool results
    """
    tool_runners = {
        'code_metrics': run_code_metrics,
        'docstrings': run_docstring_analysis,
        'pylint': run_pylint_analysis,
        'unused': run_unused_code_analysis,
        'test_coverage': run_test_coverage_analysis,
        'api_doc': run_api_doc_analysis
    }
    
    available_tools = display_available_tools()
    results = {}
    
    print(f"\n🚀 Running Selected Tools: {', '.join(tool_names)}")
    print()
    
    for tool_name in tool_names:
        if tool_name not in tool_runners:
            print(f"❌ Unknown tool: {tool_name}")
            print(f"Available tools: {', '.join(available_tools.keys())}")
            results[tool_name] = False
            continue
        
        runner = tool_runners[tool_name]
        results[tool_name] = runner(config)
    
    return results


def save_analysis_summary(results: Dict[str, bool], config: dict):
    """Save analysis summary."""
    try:
        summary = {
            'project_name': config['project_name'],
            'project_root': config['project_root'],
            'analysis_results': results,
            'successful_tools': [tool for tool, success in results.items() if success],
            'failed_tools': [tool for tool, success in results.items() if not success],
            'total_tools': len(results),
            'success_rate': sum(results.values()) / len(results) if results else 0
        }
        
        summary_file = Path(config['report_dir']) / 'analysis_summary.json'
        with open(summary_file, 'w') as f:
            json.dump(summary, f, indent=2)
        
        print(f"📄 Analysis summary saved to: {summary_file}")
        
    except Exception as e:
        print(f"⚠️ Could not save analysis summary: {str(e)}")


def generate_overall_numeric_summary(config: dict):
    """Generate overall numeric summary from all tool reports."""
    try:
        report_dir = Path(config['report_dir'])
        
        # Initialize summary structure
        overall_summary = {
            "project_name": config['project_name'],
            "project_root": config['project_root'],
            "analysis_date": json.loads(open(Path(__file__).parent / 'config.json').read() if (Path(__file__).parent / 'config.json').exists() else '{}').get('analysis_date', ''),
            "overall_scores": {},
            "metrics": {}
        }
        
        # Load individual tool reports and extract key metrics
        tool_files = {
            'pylint': config.get('pylint_output', 'pylint_report.json'),
            'test_coverage': config.get('test_coverage_output', 'test_coverage_report.json'),
            'docstrings': config.get('docstring_output', 'docstring_coverage_report.json'),
            'code_metrics': config.get('code_metrics_output', 'code_metrics_report.json'),
            'unused': config.get('unused_output', 'unused_code_report.json')
        }
        
        # Extract metrics from each tool
        for tool_name, filename in tool_files.items():
            tool_file = report_dir / filename
            if tool_file.exists():
                try:
                    with open(tool_file, 'r') as f:
                        tool_data = json.load(f)
                    
                    if tool_name == 'pylint':
                        overall_summary["overall_scores"]["pylint_score"] = tool_data.get("score", 0.0)
                        overall_summary["metrics"]["pylint_issues"] = tool_data.get("total_issues", 0)
                        overall_summary["metrics"]["pylint_files_analyzed"] = tool_data.get("files_analyzed", 0)
                        
                    elif tool_name == 'test_coverage':
                        overall_summary["overall_scores"]["coverage_percentage"] = tool_data.get("coverage_percentage", 0.0)
                        overall_summary["overall_scores"]["coverage_grade"] = tool_data.get("coverage_grade", "F")
                        overall_summary["metrics"]["total_files_coverage"] = tool_data.get("summary", {}).get("total_files", 0)
                        overall_summary["metrics"]["covered_statements"] = tool_data.get("summary", {}).get("statements", {}).get("covered", 0)
                        overall_summary["metrics"]["total_statements"] = tool_data.get("summary", {}).get("statements", {}).get("total", 0)
                        
                    elif tool_name == 'docstrings':
                        if tool_data.get("total_functions", 0) > 0:
                            overall_summary["overall_scores"]["docstring_coverage"] = tool_data.get("docstring_coverage_percent", 0.0)
                            overall_summary["metrics"]["documented_functions"] = tool_data.get("documented_functions", 0)
                            overall_summary["metrics"]["total_functions"] = tool_data.get("total_functions", 0)
                        
                    elif tool_name == 'code_metrics':
                        summary = tool_data.get("summary", {})
                        overall_summary["metrics"]["total_files"] = summary.get("total_files", 0)
                        overall_summary["metrics"]["total_code_lines"] = summary.get("total_code_lines", 0)
                        overall_summary["metrics"]["total_functions"] = summary.get("total_functions", 0)
                        overall_summary["metrics"]["total_classes"] = summary.get("total_classes", 0)
                        
                    elif tool_name == 'unused':
                        overall_summary["overall_scores"]["unused_items_count"] = tool_data.get("unused_items_count", 0)
                        overall_summary["metrics"]["unused_total_files"] = tool_data.get("total_defined_files", 0)
                        overall_summary["metrics"]["unused_items"] = tool_data.get("unused_items_count", 0)
                        
                except (json.JSONDecodeError, KeyError) as e:
                    print(f"⚠️ Warning: Could not parse {tool_name} report: {e}")
        
        # Individual tool scores (no composite calculation)
        scores = overall_summary["overall_scores"]
        
        # Add analysis metadata
        overall_summary["analysis_date"] = datetime.now().isoformat()
        overall_summary["tools_available"] = list(tool_files.keys())
        overall_summary["reports_location"] = str(report_dir)
        
        # Save numeric summary
        numeric_summary_file = report_dir / config.get('quality_numeric_output', 'code_quality_numeric_summary.json')
        with open(numeric_summary_file, 'w') as f:
            json.dump(overall_summary, f, indent=2)
        
        print(f"📊 Overall numeric summary saved to: {numeric_summary_file}")
        
        # Display key metrics
        print(f"\n📈 OVERALL NUMERIC SUMMARY:")
        if "pylint_score" in scores:
            print(f"   🔍 Pylint Score: {scores['pylint_score']}/10")
        if "coverage_percentage" in scores:
            print(f"   🧪 Test Coverage: {scores['coverage_percentage']}%")
        if "docstring_coverage" in scores:
            print(f"   📝 Docstring Coverage: {scores['docstring_coverage']}%")
        if "unused_items_count" in scores:
            print(f"   🧹 Unused Code Items: {scores['unused_items_count']}")
        
        return overall_summary
        
    except Exception as e:
        print(f"⚠️ Could not generate overall numeric summary: {str(e)}")
        return None


def print_analysis_results(results: Dict[str, bool], config: dict):
    """Print analysis results summary."""
    print("\n" + "=" * 60)
    print("📊 ANALYSIS RESULTS SUMMARY")
    print("=" * 60)
    print(f"🎯 Project: {config['project_name']}")
    print(f"📁 Root: {config['project_root']}")
    print()
    
    successful = [tool for tool, success in results.items() if success]
    failed = [tool for tool, success in results.items() if not success]
    
    if successful:
        print(f"✅ Successful Tools ({len(successful)}):")
        for tool in successful:
            print(f"   ✅ {tool}")
    
    if failed:
        print(f"\n❌ Failed Tools ({len(failed)}):")
        for tool in failed:
            print(f"   ❌ {tool}")
    
    success_rate = (len(successful) / len(results) * 100) if results else 0
    print(f"\n📈 Success Rate: {success_rate:.1f}% ({len(successful)}/{len(results)})")
    print(f"📄 Reports saved to: {config['report_dir']}")
    print("=" * 60)


def interactive_mode(config: dict):
    """Run interactive mode for tool selection."""
    tools = display_available_tools()
    presets = display_presets()
    
    while True:
        print("\n" + "=" * 60)
        print("🎯 CODE QUALITY ANALYSIS - INTERACTIVE MODE")
        print("=" * 60)
        print(f"📂 Project: {config['project_name']}")
        print(f"📁 Root: {config['project_root']}")
        print()
        
        print("🛠️  Available Tools:")
        for i, (tool, desc) in enumerate(tools.items(), 1):
            print(f"   {i}. {desc}")
        
        print("\n📋 Available Presets:")
        for preset, preset_tools in presets.items():
            print(f"   {preset}: {', '.join(preset_tools)}")
        
        print("\n" + "-" * 40)
        print("Options:")
        print("  • Enter tool numbers (e.g., 1,2,3)")
        print("  • Enter preset name (e.g., quick)")
        print("  • Type 'all' for all tools")
        print("  • Type 'menu' to see this menu again")
        print("  • Type 'exit' to quit")
        print("-" * 40)
        
        choice = input("\n🔧 Your choice: ").strip().lower()
        
        if choice == 'exit':
            print("👋 Goodbye!")
            break
        elif choice == 'menu':
            continue
        elif choice == 'all':
            selected_tools = list(tools.keys())
        elif choice in presets:
            selected_tools = presets[choice]
        elif choice.replace(',', '').replace(' ', '').isdigit():
            # Handle numeric selection
            try:
                tool_list = list(tools.keys())
                numbers = [int(x.strip()) for x in choice.split(',')]
                selected_tools = [tool_list[i-1] for i in numbers if 1 <= i <= len(tool_list)]
            except (ValueError, IndexError):
                print("❌ Invalid selection. Please try again.")
                continue
        else:
            # Handle tool names directly
            selected_tools = [t.strip() for t in choice.split(',') if t.strip() in tools]
            if not selected_tools:
                print("❌ Invalid selection. Please try again.")
                continue
        
        if selected_tools:
            print(f"\n🚀 Selected tools: {', '.join(selected_tools)}")
            confirm = input("Continue? (y/n): ").strip().lower()
            if confirm in ['y', 'yes', '']:
                results = run_analysis_tools(selected_tools, config)
                print_analysis_results(results, config)
                save_analysis_summary(results, config)
                generate_overall_numeric_summary(config)
                
                # Ask if user wants to continue
                continue_choice = input("\n🔄 Run another analysis? (y/n): ").strip().lower()
                if continue_choice not in ['y', 'yes', '']:
                    print("✅ Analysis complete!")
                    break


def main():
    """Main function for running analysis."""
    parser = argparse.ArgumentParser(
        description="Run code quality analysis based on saved configuration",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 cq_run_analysis.py                           # Interactive mode
  python3 cq_run_analysis.py --tools code_metrics     # Single tool
  python3 cq_run_analysis.py --tools pylint,docstrings # Multiple tools
  python3 cq_run_analysis.py --preset quick           # Preset combination
  python3 cq_run_analysis.py --preset all             # All tools
        """
    )
    
    parser.add_argument(
        '--tools',
        help='Comma-separated list of tools to run'
    )
    
    parser.add_argument(
        '--preset',
        help='Use a predefined tool combination (quick, standard, comprehensive, etc.)'
    )
    
    parser.add_argument(
        '--config-file',
        help='Custom path to configuration file'
    )
    
    parser.add_argument(
        '--interactive', '-i',
        action='store_true',
        help='Run in interactive mode'
    )
    
    parser.add_argument(
        '--list-tools',
        action='store_true',
        help='List available tools and presets'
    )
    
    args = parser.parse_args()
    
    try:
        # List tools and exit
        if args.list_tools:
            tools = display_available_tools()
            presets = display_presets()
            
            print("🛠️  Available Tools:")
            for tool, desc in tools.items():
                print(f"   {tool}: {desc}")
            
            print("\n📋 Available Presets:")
            for preset, preset_tools in presets.items():
                print(f"   {preset}: {', '.join(preset_tools)}")
            return
        
        # Load configuration
        print("🔧 Loading configuration...")
        config = load_active_config(args.config_file)
        print(f"✅ Configuration loaded for project: {config['project_name']}")
        
        # Determine which tools to run
        if args.interactive or (not args.tools and not args.preset):
            # Interactive mode
            interactive_mode(config)
        else:
            # Command line mode
            presets = display_presets()
            
            if args.preset:
                if args.preset not in presets:
                    print(f"❌ Unknown preset: {args.preset}")
                    print(f"Available presets: {', '.join(presets.keys())}")
                    sys.exit(1)
                selected_tools = presets[args.preset]
            else:
                selected_tools = [t.strip() for t in args.tools.split(',')]
            
            # Run analysis
            results = run_analysis_tools(selected_tools, config)
            print_analysis_results(results, config)
            save_analysis_summary(results, config)
            generate_overall_numeric_summary(config)
        
    except FileNotFoundError as e:
        print(f"❌ {str(e)}")
        print("\n💡 To get started:")
        print("   1. Set configuration: python3 cq_set_config.py --project /path/to/project")
        print("   2. Run analysis: python3 cq_run_analysis.py")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main() 