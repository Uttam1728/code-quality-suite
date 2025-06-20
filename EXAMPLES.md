# 📖 Complete Usage Examples

## 💡 **Basic Workflow Examples**

### **Django Project Analysis**
```bash
# 1. Configure a Django project
python3 cq_set_config.py --project /Users/john/my-django-app

# 2. Run quick analysis first
python3 cq_run_analysis.py --preset quick

# 3. If satisfied, run full analysis
python3 cq_run_analysis.py --preset comprehensive
```

### **Flask Application**
```bash
# Configure Flask project with custom includes
python3 cq_set_config.py --project /path/to/flask-app --include app,config,migrations

# Run documentation-focused analysis
python3 cq_run_analysis.py --preset documentation
```

### **Generic Python Package**
```bash
# Auto-detect package structure
python3 cq_set_config.py --project /path/to/package --show-detection

# Run quality-focused analysis
python3 cq_run_analysis.py --preset quality
```

---

## 🔧 **Advanced Configuration Examples**

### **Custom Include Directories**
```bash
# Include specific source directories
python3 cq_set_config.py --project /path/to/repo --include src,app,lib

# Include multiple app directories for Django
python3 cq_set_config.py --project /django-project --include myapp,core,utils,api
```

### **Advanced Exclude Patterns**
```bash
# Exclude temporary and backup directories
python3 cq_set_config.py --project /path/to/repo --exclude temp,backup,archive

# Exclude specific patterns for data science projects
python3 cq_set_config.py --project /ml-project --exclude data,models,notebooks,experiments
```

### **Project Detection Examples**
```bash
# Show what will be detected before configuring
python3 cq_set_config.py --project /path/to/repo --show-detection

# Example output for Django project:
# 🔍 AUTO-DETECTION RESULTS:
# 📁 Project Type: Django (detected manage.py, settings.py)
# 📂 Include Directories: ['myapp', 'core', 'utils']
# 🚫 Excluded Patterns: ['venv', '__pycache__', 'migrations', 'static']
```

---

## 🎯 **Flexible Analysis Options**

### **Specific Tool Selection**
```bash
# Run only code metrics and documentation analysis
python3 cq_run_analysis.py --tools code_metrics,docstrings

# Comprehensive code quality check
python3 cq_run_analysis.py --tools pylint,unused,test_coverage

# Quick structure analysis
python3 cq_run_analysis.py --tools code_metrics
```

### **Interactive Mode Examples**
```bash
# Start interactive mode
python3 cq_run_analysis.py --interactive

# Example interaction:
# 🔧 CODE QUALITY ANALYSIS SUITE
# ================================================================
# 
# 📋 Available Analysis Tools:
#   📊 code_metrics    - Code Metrics
#   📝 docstrings      - Docstring Coverage  
#   🔍 pylint          - Pylint Analysis
#   🗑️ unused          - Unused Code Detection
#   🧪 test_coverage   - Test Coverage
#   📖 api_doc         - API Documentation
# 
# 🎯 Predefined Combinations:
#   ⚡ quick           - Fast tools for quick feedback
#   📋 standard        - Balanced analysis
#   🔬 comprehensive   - All analysis tools
# 
# Your choice: standard
```

### **All Available Presets**
```bash
# Ultra-fast feedback (2 tools)
python3 cq_run_analysis.py --preset quick

# Balanced analysis (3 tools)
python3 cq_run_analysis.py --preset standard

# Complete analysis (all 6 tools)
python3 cq_run_analysis.py --preset comprehensive

# Documentation focus (2 tools)
python3 cq_run_analysis.py --preset documentation

# Code quality focus (2 tools)  
python3 cq_run_analysis.py --preset quality

# Same as comprehensive
python3 cq_run_analysis.py --preset all
```

---

## 🏢 **Team & CI/CD Examples**

### **CI/CD Integration**
```bash
# In your CI pipeline
pip install -r requirements.txt
python3 cq_set_config.py --project $GITHUB_WORKSPACE
python3 cq_run_analysis.py --preset comprehensive

# Check if reports were generated
ls cq_reports/
# Expected: analysis_summary.json, pylint_report.json, etc.
```

### **GitHub Actions Example**
```yaml
name: Code Quality Analysis
on: [push, pull_request]

jobs:
  quality-check:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pylint vulture pytest pytest-cov
    
    - name: Run code quality analysis
      run: |
        python3 cq_set_config.py --project $GITHUB_WORKSPACE
        python3 cq_run_analysis.py --preset comprehensive
    
    - name: Upload reports
      uses: actions/upload-artifact@v3
      with:
        name: quality-reports
        path: cq_reports/
```

### **Multiple Project Workflow**
```bash
# Team lead analyzing multiple projects
for project in /projects/app1 /projects/app2 /projects/api; do
    echo "Analyzing $project..."
    python3 cq_set_config.py --project $project
    python3 cq_run_analysis.py --preset standard
    mv cq_reports/ "reports_$(basename $project)/"
done
```

---

## 📊 **Report Analysis Examples**

### **JSON Report Structure**
```bash
# View analysis summary
cat cq_reports/analysis_summary.json
```

Example output:
```json
{
  "analysis_metadata": {
    "timestamp": "2024-01-15T10:30:45",
    "project_name": "my-django-app",
    "project_root": "/Users/john/my-django-app"
  },
  "tools_executed": [
    {"name": "code_metrics", "status": "success", "execution_time": 0.5},
    {"name": "docstrings", "status": "success", "execution_time": 1.2},
    {"name": "pylint", "status": "success", "execution_time": 15.7}
  ],
  "summary_stats": {
    "total_files": 167,
    "lines_of_code": 7781,
    "docstring_coverage": 72.5,
    "pylint_score": 8.5
  }
}
```

### **Individual Tool Reports**
```bash
# View specific tool reports
cat cq_reports/code_metrics_report.json    # File structure metrics
cat cq_reports/docstring_report.json       # Documentation analysis
cat cq_reports/pylint_report.json          # Code quality issues
cat cq_reports/unused_report.json          # Dead code findings
cat cq_reports/test_coverage_report.json   # Coverage statistics
cat cq_reports/api_doc_report.json         # API documentation
```

---

## 🔄 **Development Workflow Integration**

### **Pre-commit Hook Example**
```bash
# .git/hooks/pre-commit
#!/bin/bash
echo "Running code quality analysis..."
python3 cq_set_config.py --project .
python3 cq_run_analysis.py --preset quick

# Check if pylint score is acceptable (if available)
if [[ -f cq_reports/pylint_report.json ]]; then
    score=$(python3 -c "import json; print(json.load(open('cq_reports/pylint_report.json'))['score'])")
    if (( $(echo "$score < 7.0" | bc -l) )); then
        echo "❌ Pylint score too low: $score"
        exit 1
    fi
fi
echo "✅ Code quality check passed!"
```

### **VS Code Integration**
```bash
# Add to VS Code tasks.json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Quick Quality Check",
            "type": "shell",
            "command": "python3",
            "args": ["cq_run_analysis.py", "--preset", "quick"],
            "group": "build",
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "shared"
            }
        }
    ]
}
```

### **PyCharm External Tool**
```
Name: Code Quality Analysis
Program: python3
Arguments: cq_run_analysis.py --preset standard
Working directory: $ProjectFileDir$
```

---

## 🎯 **Specialized Use Cases**

### **Data Science Projects**
```bash
# Configure with typical data science structure
python3 cq_set_config.py --project /ml-project \
    --include src,models,preprocessing \
    --exclude data,notebooks,experiments,outputs

# Focus on code quality (skip tests for notebooks)
python3 cq_run_analysis.py --tools code_metrics,docstrings,pylint
```

### **Microservices Architecture**
```bash
# Analyze each service separately
for service in auth-service user-service payment-service; do
    python3 cq_set_config.py --project /microservices/$service
    python3 cq_run_analysis.py --preset standard
    mv cq_reports/ "${service}_reports/"
done
```

### **Legacy Code Assessment**
```bash
# Comprehensive analysis for legacy code
python3 cq_set_config.py --project /legacy-system --show-detection
python3 cq_run_analysis.py --preset comprehensive

# Focus on finding unused code and quality issues
python3 cq_run_analysis.py --tools unused,pylint
```

---

## 📈 **Performance Optimization Examples**

### **Large Project Strategy**
```bash
# For large projects (5K+ files), start with quick analysis
python3 cq_run_analysis.py --preset quick  # ~1-2 minutes

# Then run specific tools incrementally
python3 cq_run_analysis.py --tools pylint     # Most time-consuming
python3 cq_run_analysis.py --tools unused     # Medium time
python3 cq_run_analysis.py --tools test_coverage  # Depends on test suite
```

### **Selective Analysis**
```bash
# Exclude large directories for faster analysis
python3 cq_set_config.py --project /big-project \
    --exclude vendor,third_party,node_modules,static

# Focus on source code only
python3 cq_set_config.py --project /big-project \
    --include src,app --exclude tests,docs
```

---

## 💡 **Pro Tips & Best Practices**

### **Development Workflow**
1. **Daily**: Use `--preset quick` for fast feedback
2. **Before commits**: Use `--preset standard` 
3. **Before releases**: Use `--preset comprehensive`
4. **Documentation sprints**: Use `--preset documentation`

### **Team Standards**
```bash
# Establish team baseline
python3 cq_run_analysis.py --preset comprehensive
# Document baseline scores in team standards

# Regular team analysis
python3 cq_run_analysis.py --preset standard
# Compare against baseline metrics
```

### **Continuous Improvement**
```bash
# Track improvements over time
echo "$(date): $(python3 cq_run_analysis.py --preset quick)" >> quality_log.txt

# Monthly comprehensive analysis
python3 cq_run_analysis.py --preset comprehensive
# Archive reports with date stamps
cp -r cq_reports/ "monthly_reports/$(date +%Y%m)"
```

This comprehensive examples guide should help users understand all the different ways to use the code quality suite effectively! 