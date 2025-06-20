# Code Quality Combined

A comprehensive, dynamic code quality analysis suite that can analyze **any Python project** using multiple analysis tools. Built with a modern 2-step configuration system for maximum flexibility.

## 🚀 **Quick Start - Analyze Any Repository**

### **Step 1: Configure the Project** 🔧
```bash
python3 cq_set_config.py --project /path/to/your/repository
```

### **Step 2: Run Analysis** 🚀
```bash
# Quick analysis (code metrics + docstrings)
python3 cq_run_analysis.py --preset quick

# Comprehensive analysis (all 6 tools)
python3 cq_run_analysis.py --preset comprehensive

# Interactive mode (choose tools with menu)
python3 cq_run_analysis.py --interactive
```

**That's it!** Just 2 simple commands to analyze any Python repository! 🎉

## ✨ **Key Features**

- ✅ **Dynamic project targeting** - Analyze ANY Python project by absolute path
- ✅ **Smart auto-detection** - Automatically finds source directories and project type
- ✅ **Virtual environment exclusion** - Intelligent filtering of venv, __pycache__, etc.
- ✅ **Persistent configuration** - JSON-based config that remembers your settings
- ✅ **Multiple execution modes** - Presets, custom tools, interactive menus
- ✅ **Comprehensive reporting** - Structured JSON reports for all tools
- ✅ **No import conflicts** - Clean relative imports system

## 📊 **Available Analysis Tools**

| Tool | Description | What it analyzes |
|------|-------------|------------------|
| `code_metrics` | Code structure & complexity | Files, lines, functions, classes |
| `docstrings` | Documentation coverage | Missing docstrings percentage |
| `pylint` | Code quality & style | PEP8, errors, warnings, score |
| `unused` | Dead code detection | Unused imports, variables, functions |
| `test_coverage` | Test coverage analysis | Code covered by tests |
| `api_doc` | API documentation | OpenAPI specification coverage |

## 🎯 **Preset Combinations**

| Preset | Tools Included | Best For | Speed |
|--------|---------------|----------|-------|
| `quick` | code_metrics, docstrings | Fast feedback during development | ⚡ Fast |
| `standard` | code_metrics, docstrings, pylint | Regular development workflow | 🟡 Medium |
| `comprehensive` | All 6 tools | Full project analysis | 🔴 Slow |
| `documentation` | docstrings, api_doc | Documentation quality focus | ⚡ Fast |
| `quality` | pylint, unused | Code quality focus | 🟡 Medium |
| `all` | All 6 tools | Same as comprehensive | 🔴 Slow |

## 🔧 **Installation**

1. **Clone and navigate:**
```bash
git clone <repository-url>
cd cerebrum/code_quality_combined
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Ready to use!** No additional setup needed.

## 💡 **Complete Usage Examples**

### **Basic Workflow**
```bash
# 1. Configure a Django project
python3 cq_set_config.py --project /Users/john/my-django-app

# 2. Run quick analysis first
python3 cq_run_analysis.py --preset quick

# 3. If satisfied, run full analysis
python3 cq_run_analysis.py --preset comprehensive
```

### **Advanced Configuration**
```bash
# Custom include directories
python3 cq_set_config.py --project /path/to/repo --include src,app,lib

# Additional exclude patterns
python3 cq_set_config.py --project /path/to/repo --exclude temp,backup

# Show auto-detection results
python3 cq_set_config.py --project /path/to/repo --show-detection
```

### **Flexible Analysis Options**
```bash
# Specific tools only
python3 cq_run_analysis.py --tools code_metrics,docstrings,pylint

# Interactive mode with menu
python3 cq_run_analysis.py --interactive

# All available tools
python3 cq_run_analysis.py --preset all
```

### **Multiple Projects**
```bash
# Switch between projects easily
python3 cq_set_config.py --project /path/to/project1
python3 cq_run_analysis.py --preset quick

python3 cq_set_config.py --project /path/to/project2  
python3 cq_run_analysis.py --preset comprehensive
```

## 🔧 **Configuration System**

### **Step 1: Project Configuration (`cq_set_config.py`)**

**Auto-Detection Features:**
- 🔍 **Project Type Detection**: Django, Flask, FastAPI, Generic Python
- 📁 **Smart Directory Discovery**: Automatically finds src/, app/, lib/, core/ etc.
- 🚫 **58+ Exclude Patterns**: venv, __pycache__, .git, node_modules, build/, etc.
- 💾 **Persistent Storage**: Saves to `cq_active_config.json`

**Command Options:**
```bash
python3 cq_set_config.py [OPTIONS]

Required:
  --project PATH        Absolute path to the project directory

Optional:
  --include DIRS        Custom include directories (comma-separated)
  --exclude PATTERNS    Additional exclude patterns (comma-separated)  
  --show-detection      Show what was auto-detected
```

### **Step 2: Analysis Execution (`cq_run_analysis.py`)**

**Execution Modes:**
```bash
python3 cq_run_analysis.py [OPTIONS]

Preset Options:
  --preset quick|standard|comprehensive|documentation|quality|all

Tool Selection:
  --tools tool1,tool2,tool3     # Specific tools
  --interactive                 # Menu-based selection

Other Options:
  --help                       # Show all available tools and presets
```

## 📁 **Output and Reports**

### **Report Location**
```bash
code_quality_combined/cq_reports/
├── analysis_summary.json      # Overall summary with metadata
├── code_metrics_report.json   # Code structure metrics
├── docstring_report.json      # Documentation coverage
├── pylint_report.json         # Code quality issues
├── unused_report.json         # Dead code detection
├── test_coverage_report.json  # Test coverage analysis
└── api_doc_report.json        # API documentation coverage
```

### **Sample Output**
```bash
============================================================
📊 ANALYSIS RESULTS SUMMARY
============================================================
🎯 Project: my-django-app
📁 Root: /Users/john/my-django-app

✅ Successful Tools (6):
   ✅ code_metrics     (Files: 167, Code Lines: 7781)
   ✅ docstrings       (Coverage: 30.72%)
   ✅ pylint          (Score: 8.5/10)
   ✅ unused          (Issues: 12)
   ✅ test_coverage   (Coverage: 85.3%)
   ✅ api_doc         (Coverage: 92.1%)

📈 Success Rate: 100.0% (6/6)
📄 Reports saved to: code_quality_combined/cq_reports
============================================================
```

## 🎛️ **Interactive Mode**

Run `python3 cq_run_analysis.py --interactive` for a user-friendly menu:

```
🔧 CODE QUALITY ANALYSIS SUITE
================================================================

📋 Available Analysis Tools:
  📊 code_metrics    - Code Metrics
                      Analyzes codebase structure and complexity
  📝 docstrings      - Docstring Coverage  
                      Measures documentation completeness
  🔍 pylint          - Pylint Analysis
                      Code style, conventions, and error detection

🎯 Predefined Combinations:
  ⚡ quick           - Quick Analysis
                      Fast tools for quick feedback
  📋 comprehensive   - Comprehensive Analysis
                      All analysis tools

Select analysis tools:
• Enter tool names separated by commas (e.g., pylint,unused)
• Enter a predefined combination (e.g., quick, comprehensive)  
• Enter 'all' for all tools

Your choice: 
```

## 🚫 **Smart Exclusion System**

The system automatically excludes 58+ common patterns:

**Virtual Environments:**
```
venv/, .venv/, env/, .env/, virtualenv/, .virtualenv/
```

**Build & Cache:**
```
__pycache__/, .pytest_cache/, build/, dist/, *.egg-info/
node_modules/, .mypy_cache/, .coverage
```

**Version Control & IDE:**
```
.git/, .svn/, .hg/, .vscode/, .idea/, .DS_Store
```

**Documentation & Config:**
```
docs/, .docs/, .tox/, .nox/, htmlcov/
```

## ⚙️ **Advanced Features**

### **Project Type Auto-Detection**
- **Django**: Detects `manage.py`, `settings.py` patterns
- **Flask**: Identifies Flask application structures  
- **FastAPI**: Recognizes FastAPI project patterns
- **Generic Python**: Fallback for other Python projects

### **Configuration Persistence**
- Settings saved to `cq_active_config.json`
- Automatically loads last configuration
- Switch between projects seamlessly

### **Error Handling**
- Graceful handling of missing tools
- Detailed error reporting
- Partial analysis completion (continues even if some tools fail)

## 🔧 **Tool-Specific Configuration**

### **Code Metrics**
- Analyzes: Files, lines of code, functions, classes, methods
- Tracks: Biggest files, complexity metrics
- Output: Comprehensive structure analysis

### **Docstring Coverage**  
- Checks: Functions, classes, methods
- Reports: Missing documentation percentage
- Ignores: Private methods, test files (configurable)

### **Pylint Analysis**
- Style: PEP 8 compliance
- Quality: Code smells, potential bugs
- Score: 0-10 rating system

### **Unused Code Detection**
- Finds: Dead code, unused imports
- Analyzes: Variables, functions, classes
- Smart filtering: Avoids false positives

### **Test Coverage**
- Requires: pytest, pytest-cov
- Measures: Line and branch coverage
- Reports: Detailed coverage analysis

### **API Documentation**
- Analyzes: OpenAPI/Swagger specifications
- Checks: Endpoint documentation completeness
- Requires: Valid OpenAPI JSON file

## 🛠️ **Requirements**

**Core Requirements:**
- Python 3.7+
- pathlib, json, ast (standard library)

**Optional Tool Dependencies:**
```bash
# Install as needed for specific tools
pip install pylint          # For pylint analysis
pip install vulture         # For unused code detection  
pip install pytest pytest-cov  # For test coverage
```

## 🚨 **Troubleshooting**

### **Common Issues**

**1. No Python files found:**
```bash
# Check configuration
python3 cq_set_config.py --project /path/to/project --show-detection

# Verify include directories are correct
```

**2. Virtual environment pollution:**
```bash
# The system should automatically exclude venv directories
# If not, add custom exclude patterns:
python3 cq_set_config.py --project /path/to/project --exclude venv,env
```

**3. Tool import errors:**
```bash
# Install missing dependencies
pip install pylint vulture pytest pytest-cov

# Tools gracefully fail if dependencies missing
```

**4. Permission errors:**
```bash
# Ensure read access to target project
chmod -R +r /path/to/project
```

### **Debug Commands**
```bash
# Show current configuration
cat cq_active_config.json

# Validate configuration
python3 cq_set_config.py --project /current/project --show-detection

# Test single tool
python3 cq_run_analysis.py --tools code_metrics
```

## 🏗️ **Architecture**

### **Modern 2-Step Design**
1. **Configuration Phase** (`cq_set_config.py`)
   - Project detection and analysis
   - Smart include/exclude pattern generation
   - JSON configuration persistence

2. **Execution Phase** (`cq_run_analysis.py`)  
   - Tool orchestration and execution
   - Report generation and aggregation
   - Multiple execution modes

### **Clean Import System**
- Relative imports throughout
- No circular dependencies
- Modular tool architecture

### **File Organization**
```
code_quality_combined/
├── cq_set_config.py         # Step 1: Project configuration
├── cq_run_analysis.py       # Step 2: Analysis execution  
├── helper_scripts/          # Individual analysis tools
├── utils/                   # Shared utilities
├── cq_active_config.json    # Active project configuration
└── cq_reports/              # Generated analysis reports
```

## 🤝 **Contributing**

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes following the existing patterns
4. Test with multiple project types
5. Submit a pull request

### **Adding New Tools**
1. Create tool script in `helper_scripts/`
2. Add tool definition to `cq_run_analysis.py`
3. Follow existing patterns for configuration and reporting
4. Update documentation

## 📄 **License**

This project is licensed under the MIT License - see the LICENSE file for details.

## 🎯 **Summary**

**What makes this special:**
- 🚀 **2-step simplicity**: Configure once, analyze many times
- 🎯 **Universal compatibility**: Works with any Python project structure  
- 🧹 **Smart filtering**: No more virtual environment pollution
- 📊 **Comprehensive analysis**: 6 different quality tools
- 🔧 **Flexible execution**: From quick checks to deep analysis
- 📋 **Production ready**: Clean, modern, well-documented codebase

**Perfect for:**
- 👨‍💻 **Developers**: Quick quality checks during development
- 🏢 **Teams**: Standardized quality analysis across projects
- 🤖 **CI/CD**: Automated quality gates in deployment pipelines
- 📊 **Managers**: Quality metrics and technical debt tracking

Start analyzing your Python projects in seconds! 🎉 