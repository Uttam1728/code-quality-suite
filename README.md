# 🚀 Code Quality Combined - Python Static Code Analysis Suite

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Analysis Tools](https://img.shields.io/badge/Analysis%20Tools-6-orange)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)

**🔍 Automated Python Code Quality Analysis | Static Code Analysis | CI/CD Integration | Code Metrics & Linting Automation**

</div>

---

> ### 💡 **Why Code Quality Combined?**
> 
> **Comprehensive Python static code analysis tool** that combines **6+ powerful analysis engines** including Pylint, code coverage, documentation analysis, and dead code detection. Perfect for **automated code review**, **CI/CD pipelines**, and **technical debt management**.
> 
> ✨ **No more juggling multiple tools** - get everything in one unified analysis suite!

---

## 🏷️ **Keywords & Tags**
<div align="center">

`python-code-analysis` `static-analysis` `code-quality` `pylint-automation` `code-coverage` `ci-cd-integration` `code-metrics` `automated-testing` `technical-debt` `code-review-automation` `python-linting` `documentation-analysis` `dead-code-detection` `software-quality`

</div>

---

## 🌟 **What Makes This Special**

<table>
<tr>
<td width="50%">

### 🎯 **For Developers**
- ⚡ **2-minute setup** - From zero to analysis
- 🔄 **Works with ANY Python project**
- 📊 **6 tools in 1** - No tool switching needed
- 🎮 **Interactive mode** - User-friendly menus

</td>
<td width="50%">

### 🏢 **For Teams & CI/CD**  
- 🤖 **Perfect for automation** - CI/CD ready
- 📈 **Consistent quality metrics** across projects
- 🚫 **Smart exclusions** - No venv pollution
- 📋 **JSON reports** - Easy integration

</td>
</tr>
</table>

---

A comprehensive, dynamic code quality analysis suite that can analyze **any Python project** using multiple analysis tools. Built with a modern 2-step configuration system for maximum flexibility.

## 🚀 **Quick Start - Automated Python Code Analysis**

<div align="center">

### ⚡ **From Zero to Analysis in 3 Commands!**

</div>

<table>
<tr>
<td width="5%"><strong>1️⃣</strong></td>
<td width="25%"><strong>📦 Install Dependencies</strong></td>
<td width="70%">

```bash
pip install -r requirements.txt
```
</td>
</tr>

<tr>
<td><strong>2️⃣</strong></td>
<td><strong>🔧 Configure Project</strong></td>
<td>

```bash
python3 cq_set_config.py --project /path/to/your/repository
```
</td>
</tr>

<tr>
<td><strong>3️⃣</strong></td>
<td><strong>🚀 Run Analysis</strong></td>
<td>

```bash
# Quick analysis (recommended for first-time users)
python3 cq_run_analysis.py --preset quick

# OR: Full comprehensive analysis  
python3 cq_run_analysis.py --preset comprehensive

# OR: Interactive mode (guided experience)
python3 cq_run_analysis.py --interactive
```
</td>
</tr>
</table>

<div align="center">

🎉 **That's it!** Your Python project analysis is complete!

💡 **Tip**: Start with `--preset quick` for instant feedback, then upgrade to `comprehensive` for deep insights.

</div>

## ✨ **Python Code Quality Features**

<div align="center">

### 🎯 **Everything You Need for Perfect Code Quality**

</div>

<table>
<tr>
<td width="50%">

### 🚀 **Smart & Fast**
- ✅ **Dynamic project targeting** - Analyze ANY Python project by absolute path
- ✅ **Smart auto-detection** - Automatically finds source directories and project type  
- ✅ **Virtual environment exclusion** - Intelligent filtering of venv, __pycache__, etc.
- ✅ **No import conflicts** - Clean relative imports system

</td>
<td width="50%">

### 🔧 **Flexible & Powerful**
- ✅ **Persistent configuration** - JSON-based config that remembers your settings
- ✅ **Multiple execution modes** - Presets, custom tools, interactive menus
- ✅ **Comprehensive reporting** - Structured JSON reports for all tools
- ✅ **Production ready** - Battle-tested across project sizes

</td>
</tr>
</table>

---

## 📸 **Demo**

<div align="center">

### 🎬 **See It In Action!**

</div>

<details>
<summary><strong>🎮 Interactive Mode in Action</strong> (Click to expand)</summary>

```bash
$ python3 cq_run_analysis.py --interactive

🔧 CODE QUALITY ANALYSIS SUITE
================================================================

📋 Available Analysis Tools:
  📊 code_metrics    - Code Metrics
  📝 docstrings      - Docstring Coverage  
  🔍 pylint          - Pylint Analysis

🎯 Predefined Combinations:
  ⚡ quick           - Fast tools for quick feedback
  📋 comprehensive   - All analysis tools

Your choice: comprehensive
```

</details>

<details>
<summary><strong>📊 Sample Terminal Output</strong> (Click to expand)</summary>

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

</details>

<details>
<summary><strong>🔍 Configuration Auto-Detection Example</strong> (Click to expand)</summary>

```bash
$ python3 cq_set_config.py --project /path/to/django-project --show-detection

🔍 AUTO-DETECTION RESULTS:
📁 Project Type: Django (detected manage.py, settings.py)
📂 Include Directories: ['myapp', 'core', 'utils']
🚫 Excluded Patterns: ['venv', '__pycache__', 'migrations', 'static']
💾 Configuration saved to: cq_active_config.json
```

</details>

## 📊 **Python Static Analysis Tools Overview**

<div align="center">

### 🛠️ **6 Powerful Tools - All In One Suite**

</div>

| 🎯 **Tool** | 📝 **What It Does** | 🔍 **What It Analyzes** | ⚡ **Speed** |
|-------------|---------------------|-------------------------|-------------|
| 📊 `code_metrics` | **Code Structure & Complexity** | Files, lines, functions, classes | 🟢 Instant |
| 📚 `docstrings` | **Documentation Coverage** | Missing docstrings percentage | 🟢 Fast |
| 🔍 `pylint` | **Code Quality & Style** | PEP8, errors, warnings, score | 🔴 Slow |
| 🗑️ `unused` | **Dead Code Detection** | Unused imports, variables, functions | 🟡 Medium |
| 🧪 `test_coverage` | **Test Coverage Analysis** | Code covered by tests | 🔴 Slow |
| 📖 `api_doc` | **API Documentation** | OpenAPI specification coverage | 🟢 Fast |

<div align="center">

💡 **Pro Tip**: Each tool can run independently or in combination with others!

</div>

---

## 🎯 **Code Analysis Preset Combinations**

<div align="center">

### ⚡ **Choose Your Perfect Workflow**

</div>

<table>
<tr>
<td width="20%" align="center"><strong>🚀 Preset</strong></td>
<td width="35%" align="center"><strong>🛠️ Tools Included</strong></td>
<td width="25%" align="center"><strong>🎯 Best For</strong></td>
<td width="20%" align="center"><strong>⏱️ Speed</strong></td>
</tr>

<tr>
<td align="center">⚡ <code>quick</code></td>
<td>code_metrics, docstrings</td>
<td>🔄 Development workflow</td>
<td>🟢 <strong>Fast</strong></td>
</tr>

<tr>
<td align="center">📋 <code>standard</code></td>
<td>code_metrics, docstrings, pylint</td>
<td>👥 Code reviews</td>
<td>🟡 <strong>Medium</strong></td>
</tr>

<tr>
<td align="center">🔬 <code>comprehensive</code></td>
<td>🌟 <strong>All 6 tools</strong></td>
<td>🚀 Releases & CI/CD</td>
<td>🔴 <strong>Thorough</strong></td>
</tr>

<tr>
<td align="center">📚 <code>documentation</code></td>
<td>docstrings, api_doc</td>
<td>📖 Doc quality focus</td>
<td>🟢 <strong>Fast</strong></td>
</tr>

<tr>
<td align="center">🏆 <code>quality</code></td>
<td>pylint, unused</td>
<td>🔍 Code quality focus</td>
<td>🟡 <strong>Medium</strong></td>
</tr>

</table>

---

## 🔧 **Python Code Analysis Installation & Setup**

1. **Clone and navigate:**
```bash
git clone <repository-url>
cd cerebrum/code_quality_combined
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Verify installation:**
```bash
# Test both main scripts
python3 cq_set_config.py --help
python3 cq_run_analysis.py --help

# Quick functionality test
python3 cq_set_config.py --project . --show-detection
```

4. **Ready to use!** No additional setup needed.

✅ **Successful installation shows:**
- Both help commands display usage information
- Configuration test detects current directory structure
- No import errors or missing dependencies

## 💡 **Python Project Analysis Examples**

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

## 📋 **Tested Compatibility**

### **Python Versions**
- ✅ **Python 3.7** - Fully supported
- ✅ **Python 3.8** - Fully supported  
- ✅ **Python 3.9** - Fully supported
- ✅ **Python 3.10** - Fully supported
- ✅ **Python 3.11** - Fully supported
- ⚠️ **Python 3.12** - Compatible (some tools may have minor issues)

### **Operating Systems**
- ✅ **macOS** - 10.15+ (Catalina and newer)
- ✅ **Linux** - Ubuntu 18.04+, CentOS 7+, Debian 10+
- ✅ **Windows** - Windows 10+ (PowerShell or WSL recommended)

### **Framework Support**
- ✅ **Django** - 2.2+ (LTS versions tested)
- ✅ **Flask** - 1.1+ (all recent versions)
- ✅ **FastAPI** - 0.65+ (modern async features)
- ✅ **Generic Python** - Any standard Python project structure
- ✅ **Packages/Libraries** - pip installable packages

### **Project Sizes Tested**
- ✅ **Small Projects** - <500 files, <50K lines
- ✅ **Medium Projects** - 500-2K files, 50K-200K lines  
- ✅ **Large Projects** - 2K-5K files, 200K-500K lines
- ✅ **Enterprise** - 5K+ files, 500K+ lines (performance may vary)

## 🚨 **Troubleshooting**

### **⚠️ Common Pitfalls**

**1. Analyzing projects with restricted permissions:**
```bash
# ❌ Common cause of "No Python files found" errors
# ✅ Ensure read access to target project
chmod -R +r /path/to/target/project
```

**2. Large project performance expectations:**
```bash
# ⚠️ EXPECTATION: Enterprise projects (5K+ files) 
# May take 3-8 minutes for comprehensive analysis
# Use --preset quick for faster feedback during development
```

**3. Missing tool dependencies:**
```bash
# ⚠️ Tools gracefully fail if dependencies missing
# But install them for full functionality:
pip install pylint vulture pytest pytest-cov
```

**4. Configuration persistence confusion:**
```bash
# ℹ️ Configuration is saved per workspace
# Each terminal session remembers the last --project setting
# Use --show-detection to verify current configuration
```

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

## 🏗️ **Python Static Analysis Architecture**

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

## 🤝 **Contributing to Python Code Quality Tools**

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes following the existing patterns
4. Test with multiple project types
5. Submit a pull request

### **Adding New Analysis Tools**
1. Create tool script in `helper_scripts/`
2. Add tool definition to `cq_run_analysis.py`
3. Follow existing patterns for configuration and reporting
4. Update documentation

## 📄 **License**

This project is licensed under the MIT License - see the LICENSE file for details.

## 🎯 **Python Code Quality Summary**

**What makes this special:**
- 🚀 **2-step simplicity**: Configure once, analyze many times
- 🎯 **Universal compatibility**: Works with any Python project structure  
- 🧹 **Smart filtering**: No more virtual environment pollution
- 📊 **Comprehensive analysis**: 6 different quality tools
- 🔧 **Flexible execution**: From quick checks to deep analysis
- 📋 **Production ready**: Clean, modern, well-documented codebase

**Perfect for:**
- 👨‍💻 **Python Developers**: Quick quality checks during development
- 🏢 **Development Teams**: Standardized quality analysis across projects
- 🤖 **CI/CD Pipelines**: Automated quality gates in deployment workflows
- 📊 **Technical Managers**: Quality metrics and technical debt tracking
- 🔍 **Code Review Process**: Automated static analysis for pull requests

Start analyzing your Python projects in seconds! 🎉

## ⚡ **Python Code Analysis Performance Guide**

<div align="center">

### 📈 **Know What to Expect**

</div>

<details>
<summary><strong>⏱️ Execution Times by Project Size</strong> (Click to expand)</summary>

| 📊 **Project Size** | 📁 **Files** | ⚡ **Quick** | 📋 **Standard** | 🔬 **Comprehensive** |
|---------------------|--------------|-------------|-----------------|---------------------|
| 🏠 **Small** | <500 files | ~5-10s | ~10-20s | ~15-30s |
| 🏢 **Medium** | 500-2K files | ~10-20s | ~20-40s | ~30-60s |
| 🏭 **Large** | 2K-5K files | ~20-45s | ~45-90s | ~1-3min |
| 🌆 **Enterprise** | 5K+ files | ~1-2min | ~2-4min | ~3-8min |

</details>

<table>
<tr>
<td width="50%">

### 💡 **Performance Tips**
- 🚀 **Start with `quick`** preset for development
- 🎯 **Use `standard`** for regular code reviews  
- 🔍 **Reserve `comprehensive`** for releases & CI/CD
- ⚡ **Interactive mode** has no performance overhead
- 📁 **Exclude large directories** with `--exclude`

</td>
<td width="50%">

### 🏆 **Tool Speed Ranking** 
1. 🥇 `code_metrics` - Nearly instant
2. 🥈 `docstrings` - Very fast  
3. 🥉 `api_doc` - Fast
4. 🟡 `unused` - Medium (codebase dependent)
5. 🟠 `test_coverage` - Slow (runs tests)
6. 🔴 `pylint` - Slowest (comprehensive)

</td>
</tr>
</table>

---