import subprocess
import re
import os
import sys
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime


def run_coverage_analysis(config):
    """
    Run test coverage analysis with comprehensive human-readable reporting.
    
    :param config: Configuration dictionary containing analysis settings
    :return: Dictionary with coverage results
    """
    return run_tests_with_coverage(config)


def run_tests_with_coverage(config):
    """
    Run tests with coverage and generate detailed human-readable reports.
    
    :param config: Configuration dictionary
    :return: Coverage analysis results
    """
    # Try to find test directory
    test_dir = config.get("test_dir")
    if not test_dir:
        # Look for common test directory names
        project_root = Path(config["project_root"])
        possible_dirs = ["tests", "test", "testing", "spec", "specs"]
        
        for dirname in possible_dirs:
            potential_dir = project_root / dirname
            if potential_dir.exists() and potential_dir.is_dir():
                test_dir = str(potential_dir)
                break
        
        if not test_dir:
            print("❌ No test directory found. Looked for:")
            for dirname in possible_dirs:
                print(f"   - {project_root / dirname}")
            return {"error": "No test directory found", "coverage_percent": 0.0}
    
    report_dir = Path(config["report_dir"])
    coverage_output = config.get("test_coverage_output", "test_coverage_report.json")
    coverage_xml = report_dir / "coverage.xml"
    coverage_html = report_dir / "htmlcov"
    coverage_json_file = report_dir / coverage_output

    os.makedirs(report_dir, exist_ok=True)
    os.chdir(config["project_root"])

    print(f"🧪 Running tests with coverage in: {test_dir}")

    try:
        # Use the venv2 python to ensure we have coverage available
        venv_python = "/Users/piyushtyagi/Desktop/Repository/code-quality-suite/venv/bin/python3"
        
        # Run tests with coverage
        print("   📊 Executing test suite...")
        result = subprocess.run(
            [venv_python, "-m", "coverage", "run", "--source=.", "-m", "pytest", test_dir, "-v"],
            capture_output=True,
            text=True,
        )

        print(f"   📋 Test execution completed")
        
        if "collected 0 items" in result.stdout:
            print("⚠️ No tests were collected. Skipping coverage report.")
            return {"coverage_percent": 0.0, "tests_found": 0}

        # Generate XML coverage report
        print("   📄 Generating XML coverage report...")
        subprocess.run([venv_python, "-m", "coverage", "xml", "-o", str(coverage_xml)], check=True)
        
        # Generate HTML coverage report
        print("   🌐 Generating HTML coverage report...")
        subprocess.run([venv_python, "-m", "coverage", "html", "-d", str(coverage_html)], check=False)
        
        # Generate JSON coverage report
        print("   📊 Generating JSON coverage report...")
        subprocess.run([venv_python, "-m", "coverage", "json", "-o", str(report_dir / "coverage.json")], check=False)
        
        # Parse coverage data and create comprehensive report
        coverage_data = parse_coverage_data(coverage_xml, report_dir / "coverage.json")
        
        # Generate human-readable report
        human_readable_report = generate_human_readable_report(coverage_data, config)
        
        # Save comprehensive JSON report
        save_comprehensive_report(human_readable_report, coverage_json_file)
        
        # Display summary
        display_coverage_summary(human_readable_report)
        
        return human_readable_report

    except subprocess.CalledProcessError as e:
        print(f"❌ Test run or coverage generation failed: {e}")
        return {"coverage_percent": 0.0, "error": "Coverage run failed"}
    except Exception as e:
        print(f"❌ Unexpected error during coverage analysis: {e}")
        return {"coverage_percent": 0.0, "error": f"Unexpected error: {str(e)}"}


def parse_coverage_data(xml_file: Path, json_file: Path) -> Dict[str, Any]:
    """
    Parse coverage data from XML and JSON files.
    
    :param xml_file: Path to coverage XML file
    :param json_file: Path to coverage JSON file
    :return: Parsed coverage data
    """
    coverage_data = {
        "total_coverage": 0.0,
        "files": [],
        "summary": {},
        "metrics": {}
    }
    
    # Parse XML for detailed file information
    if xml_file.exists():
        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()
            
            # Parse package/file coverage
            packages = root.findall('.//package')
            all_files = []
            
            for package in packages:
                classes = package.findall('.//class')
                for cls in classes:
                    filename = cls.get('filename', '')
                    if filename:
                        lines = cls.findall('.//line')
                        total_lines = len(lines)
                        covered_lines = len([line for line in lines if line.get('hits', '0') != '0'])
                        
                        if total_lines > 0:
                            coverage_percent = (covered_lines / total_lines) * 100
                            
                            file_data = {
                                "filename": filename,
                                "total_lines": total_lines,
                                "covered_lines": covered_lines,
                                "missing_lines": total_lines - covered_lines,
                                "coverage_percent": round(coverage_percent, 2)
                            }
                            all_files.append(file_data)
            
            coverage_data["files"] = sorted(all_files, key=lambda x: x["coverage_percent"])
            
        except ET.ParseError as e:
            print(f"⚠️ Warning: Could not parse XML coverage file: {e}")
    
    # Parse JSON for overall metrics
    if json_file.exists():
        try:
            with open(json_file, 'r') as f:
                json_data = json.load(f)
                
            totals = json_data.get('totals', {})
            coverage_data["total_coverage"] = round(totals.get('percent_covered', 0.0), 2)
            coverage_data["summary"] = {
                "total_statements": totals.get('num_statements', 0),
                "covered_statements": totals.get('covered_lines', 0),
                "missing_statements": totals.get('missing_lines', 0),
                "excluded_statements": totals.get('excluded_lines', 0),
                "branches_total": totals.get('num_branches', 0),
                "branches_covered": totals.get('covered_branches', 0),
                "branches_missing": totals.get('missing_branches', 0)
            }
            
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"⚠️ Warning: Could not parse JSON coverage file: {e}")
    
    return coverage_data


def generate_human_readable_report(coverage_data: Dict[str, Any], config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generate comprehensive human-readable coverage report.
    
    :param coverage_data: Parsed coverage data
    :param config: Configuration dictionary
    :return: Human-readable report data
    """
    total_coverage = coverage_data.get("total_coverage", 0.0)
    files = coverage_data.get("files", [])
    summary = coverage_data.get("summary", {})
    
    # Categorize files by coverage level
    excellent_files = [f for f in files if f["coverage_percent"] >= 90]
    good_files = [f for f in files if 70 <= f["coverage_percent"] < 90]
    fair_files = [f for f in files if 50 <= f["coverage_percent"] < 70]
    poor_files = [f for f in files if f["coverage_percent"] < 50]
    
    # Calculate coverage grade
    def get_coverage_grade(percentage):
        if percentage >= 90: return "A"
        elif percentage >= 80: return "B"
        elif percentage >= 70: return "C"
        elif percentage >= 60: return "D"
        else: return "F"
    
    # Generate recommendations
    recommendations = generate_coverage_recommendations(total_coverage, files)
    
    # Generate CONCISE report for JSON
    concise_report = {
        "project_name": config.get("project_name", "Unknown"),
        "analysis_date": datetime.now().isoformat(),
        "coverage_percentage": total_coverage,
        "coverage_grade": get_coverage_grade(total_coverage),
        "coverage_status": "Excellent" if total_coverage >= 90 else 
                         "Good" if total_coverage >= 80 else
                         "Fair" if total_coverage >= 70 else
                         "Needs Improvement",
        "summary": {
            "total_files": len(files),
            "files_by_category": {
                "excellent_90_plus": len(excellent_files),
                "good_70_to_89": len(good_files),
                "fair_50_to_69": len(fair_files),
                "poor_below_50": len(poor_files)
            },
            "statements": {
                "total": summary.get("total_statements", 0),
                "covered": summary.get("covered_statements", 0),
                "missing": summary.get("missing_statements", 0)
            }
        },
        "top_priorities": [
            {
                "filename": f["filename"].split("/")[-1],  # Just filename
                "full_path": f["filename"],
                "coverage_percent": f["coverage_percent"],
                "missing_lines": f["missing_lines"]
            }
            for f in poor_files[:10]  # Only top 10 worst files
        ],
        "quick_wins": [
            {
                "filename": f["filename"].split("/")[-1],
                "coverage_percent": f["coverage_percent"], 
                "missing_lines": f["missing_lines"]
            }
            for f in fair_files if f["missing_lines"] <= 20
        ][:5],  # Only top 5 quick wins
        "recommendations": recommendations[:3]  # Only top 3 recommendations
    }
    
    # Generate DETAILED report for console display (keep all the detailed info for console)
    detailed_report = {
        "project_name": config.get("project_name", "Unknown"),
        "analysis_date": datetime.now().isoformat(),
        "overall_coverage": {
            "percentage": total_coverage,
            "grade": get_coverage_grade(total_coverage),
            "status": "Excellent" if total_coverage >= 90 else 
                     "Good" if total_coverage >= 80 else
                     "Fair" if total_coverage >= 70 else
                     "Needs Improvement"
        },
        "summary_stats": {
            "total_files": len(files),
            "total_statements": summary.get("total_statements", 0),
            "covered_statements": summary.get("covered_statements", 0),
            "missing_statements": summary.get("missing_statements", 0),
            "branches_total": summary.get("branches_total", 0),
            "branches_covered": summary.get("branches_covered", 0)
        },
        "file_categories": {
            "excellent": {
                "count": len(excellent_files),
                "description": "90%+ coverage",
                "files": excellent_files[:10]  # Top 10
            },
            "good": {
                "count": len(good_files),
                "description": "70-89% coverage", 
                "files": good_files[:10]  # Top 10
            },
            "fair": {
                "count": len(fair_files),
                "description": "50-69% coverage",
                "files": fair_files[:10]  # Top 10
            },
            "poor": {
                "count": len(poor_files),
                "description": "Below 50% coverage",
                "files": poor_files[:20]  # Limit to top 20 worst files
            }
        },
        "top_priorities": {
            "most_critical": poor_files[:10],  # Files needing immediate attention
            "quick_wins": [f for f in fair_files if f["missing_lines"] <= 20][:10],  # Easy to improve
            "largest_files": sorted(files, key=lambda x: x["total_lines"], reverse=True)[:10]
        },
        "recommendations": recommendations,
        "coverage_percent": total_coverage  # For backward compatibility
    }
    
    # Store both versions - return detailed for console, but save concise for JSON
    detailed_report["_concise_version"] = concise_report
    
    return detailed_report


def generate_coverage_recommendations(total_coverage: float, files: List[Dict]) -> List[str]:
    """
    Generate actionable recommendations based on coverage analysis.
    
    :param total_coverage: Overall coverage percentage
    :param files: List of file coverage data
    :return: List of recommendations
    """
    recommendations = []
    
    # Overall coverage recommendations
    if total_coverage < 50:
        recommendations.append("🔴 CRITICAL: Coverage is below 50%. Implement comprehensive test strategy.")
        recommendations.append("📝 Start with unit tests for core business logic functions.")
        recommendations.append("🎯 Aim for at least 70% coverage as initial target.")
    elif total_coverage < 70:
        recommendations.append("🟡 Coverage needs improvement. Focus on untested critical paths.")
        recommendations.append("🧪 Add integration tests for main user workflows.")
    elif total_coverage < 85:
        recommendations.append("🟢 Good coverage! Focus on edge cases and error handling.")
        recommendations.append("🔄 Add tests for exception paths and boundary conditions.")
    else:
        recommendations.append("⭐ Excellent coverage! Maintain quality with mutation testing.")
        recommendations.append("🏆 Consider property-based testing for complex algorithms.")
    
    # File-specific recommendations
    poor_files = [f for f in files if f["coverage_percent"] < 50]
    if poor_files:
        recommendations.append(f"🎯 Priority: {len(poor_files)} files have <50% coverage")
        recommendations.append(f"📂 Focus on: {', '.join([f['filename'].split('/')[-1] for f in poor_files[:3]])}")
    
    # Large uncovered files
    large_uncovered = [f for f in files if f["total_lines"] > 100 and f["coverage_percent"] < 70]
    if large_uncovered:
        recommendations.append(f"📏 Large files needing attention: {len(large_uncovered)} files >100 lines with <70% coverage")
    
    return recommendations


def save_comprehensive_report(report_data: Dict[str, Any], output_file: Path) -> None:
    """
    Save concise coverage report to JSON file.
    
    :param report_data: Report data containing both detailed and concise versions
    :param output_file: Output file path
    """
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Extract concise version if available, otherwise use full report
    concise_data = report_data.get("_concise_version", report_data)
    
    with open(output_file, 'w') as f:
        json.dump(concise_data, f, indent=2)


def display_coverage_summary(report_data: Dict[str, Any]) -> None:
    """
    Display beautiful human-readable coverage summary.
    
    :param report_data: Report data to display
    """
    overall = report_data["overall_coverage"]
    stats = report_data["summary_stats"]
    categories = report_data["file_categories"]
    priorities = report_data["top_priorities"]
    
    print(f"\n" + "="*80)
    print(f"📊 TEST COVERAGE ANALYSIS SUMMARY")
    print(f"="*80)
    print(f"📂 Project: {report_data['project_name']}")
    print(f"📅 Analysis Date: {report_data['analysis_date']}")
    print(f"\n🎯 OVERALL COVERAGE: {overall['percentage']}% (Grade: {overall['grade']})")
    print(f"   Status: {overall['status']}")
    
    print(f"\n📈 STATISTICS:")
    print(f"   📁 Total Files: {stats['total_files']}")
    print(f"   📝 Total Statements: {stats['total_statements']:,}")
    print(f"   ✅ Covered Statements: {stats['covered_statements']:,}")
    print(f"   ❌ Missing Statements: {stats['missing_statements']:,}")
    if stats['branches_total'] > 0:
        branch_coverage = (stats['branches_covered'] / stats['branches_total']) * 100
        print(f"   🌿 Branch Coverage: {branch_coverage:.1f}% ({stats['branches_covered']}/{stats['branches_total']})")
    
    print(f"\n📋 FILE BREAKDOWN:")
    print(f"   ⭐ Excellent (90%+): {categories['excellent']['count']} files")
    print(f"   ✅ Good (70-89%): {categories['good']['count']} files") 
    print(f"   ⚠️  Fair (50-69%): {categories['fair']['count']} files")
    print(f"   🔴 Poor (<50%): {categories['poor']['count']} files")
    
    if priorities["most_critical"]:
        print(f"\n🚨 TOP PRIORITY FILES (Need immediate attention):")
        for i, file_data in enumerate(priorities["most_critical"][:5], 1):
            filename = file_data["filename"].split("/")[-1]  # Just filename
            print(f"   {i}. {filename}: {file_data['coverage_percent']}% ({file_data['missing_lines']} lines missing)")
    
    if priorities["quick_wins"]:
        print(f"\n🎯 QUICK WINS (Easy improvements):")
        for i, file_data in enumerate(priorities["quick_wins"][:3], 1):
            filename = file_data["filename"].split("/")[-1]
            print(f"   {i}. {filename}: {file_data['coverage_percent']}% (only {file_data['missing_lines']} lines to cover)")
    
    print(f"\n💡 RECOMMENDATIONS:")
    for i, rec in enumerate(report_data["recommendations"][:5], 1):
        print(f"   {i}. {rec}")
    
    print(f"\n📁 Reports saved to:")
    print(f"   📄 JSON Report: {report_data.get('json_file', 'test_coverage_report.json')}")
    print(f"   🌐 HTML Report: htmlcov/index.html (if generated)")
    print(f"   📊 XML Report: coverage.xml")
    print("="*80)
