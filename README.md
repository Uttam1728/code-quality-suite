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
cd code-quality-suite
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

---

## 📚 **Documentation**

<div align="center">

### 📖 **Comprehensive Guides Available**

</div>

| 📋 **Document** | 🎯 **What You'll Find** | 🚀 **Best For** |
|-----------------|-------------------------|------------------|
| 📖 **[EXAMPLES.md](EXAMPLES.md)** | Complete usage patterns, workflows, advanced configurations | Learning all features |
| ⚡ **[PERFORMANCE.md](PERFORMANCE.md)** | Benchmarks, optimization tips, speed comparisons | Performance tuning |
| 🚨 **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** | Common issues, solutions, debug commands | Problem solving |
| 🏗️ **[ARCHITECTURE.md](ARCHITECTURE.md)** | Technical details, contributing, extending tools | Contributors & advanced users |

---

## 🚨 **Quick Troubleshooting**

**No Python files found?**
```bash
python3 cq_set_config.py --project /your/project --show-detection
```

**Tool import errors?**
```bash
pip install pylint vulture pytest pytest-cov
```

**Need detailed help?** Check **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** for comprehensive solutions.

---

## 📋 **Sample Output**

```bash
============================================================
📊 ANALYSIS RESULTS SUMMARY
============================================================
🎯 Project: my-django-app
📁 Root: /Users/john/my-django-app

✅ Successful Tools (3):
   ✅ code_metrics     (Files: 167, Lines: 7781)
   ✅ docstrings       (Coverage: 72.5%)  
   ✅ pylint          (Score: 8.5/10)

📈 Success Rate: 100% | 📄 Reports: cq_reports/
============================================================
```

---

## 🎯 **Perfect For**

- 👨‍💻 **Python Developers** - Quick quality checks during development
- 🏢 **Development Teams** - Standardized quality analysis across projects
- 🤖 **CI/CD Pipelines** - Automated quality gates in deployment workflows
- 📊 **Technical Managers** - Quality metrics and technical debt tracking
- 🔍 **Code Review Process** - Automated static analysis for pull requests

---

<div align="center">

**Start analyzing your Python projects in seconds!** 🚀

[⭐ Star this repo](../../stargazers) | [🐛 Report issues](../../issues) | [💡 Request features](../../issues/new)

</div>