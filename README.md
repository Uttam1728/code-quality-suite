# 🚀 Code Quality Combined - Python Static Code Analysis Suite

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Analysis Tools](https://img.shields.io/badge/Analysis%20Tools-6-orange)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)

**🔍 One command to analyze any Python project with 6 powerful tools**

*Pylint + Code Coverage + Documentation + Dead Code Detection + Metrics + API Docs*

</div>

---

## ⚡ **Quick Start**

```bash
# 1. Install
pip install -r requirements.txt

# 2. Configure
python3 cq_set_config.py --project /path/to/your/project

# 3. Analyze  
python3 cq_run_analysis.py --preset quick
```

**That's it!** 🎉 Your analysis reports are in `cq_reports/`

---

## 🛠️ **6 Analysis Tools**

| Tool | What It Does | Speed |
|------|-------------|-------|
| 📊 `code_metrics` | Files, lines, complexity | 🟢 Instant |
| 📚 `docstrings` | Documentation coverage | 🟢 Fast |
| 🔍 `pylint` | Code quality & PEP8 | 🔴 Thorough |
| 🗑️ `unused` | Dead code detection | 🟡 Medium |
| 🧪 `test_coverage` | Test coverage analysis | 🔴 Thorough |
| 📖 `api_doc` | API documentation | 🟢 Fast |

---

## 🎯 **Choose Your Workflow**

```bash
# Quick feedback (2 tools, ~10 seconds)
python3 cq_run_analysis.py --preset quick

# Balanced analysis (3 tools, ~30 seconds)  
python3 cq_run_analysis.py --preset standard

# Complete analysis (all 6 tools, ~2 minutes)
python3 cq_run_analysis.py --preset comprehensive

# Pick your tools interactively
python3 cq_run_analysis.py --interactive
```

---

## ✨ **What Makes This Special**

<table>
<tr>
<td width="50%">

### 🎯 **For Developers**
- ⚡ Works with **any Python project**
- 🔄 **2-minute setup** - zero configuration needed
- 🎮 **Interactive mode** for beginners
- 📊 **Unified reports** - no tool juggling

</td>
<td width="50%">

### 🏢 **For Teams**  
- 🤖 **CI/CD ready** - JSON outputs
- 📈 **Consistent metrics** across projects
- 🚫 **Smart exclusions** - no venv pollution
- ⚙️ **Configurable presets** for different needs

</td>
</tr>
</table>

---

## 🔧 **Installation**

```bash
# Clone the repository
git clone <repository-url>
cd code-quality-suite

# Install dependencies  
pip install -r requirements.txt

# Verify installation
python3 cq_set_config.py --help
```

**Optional tools** (install as needed):
```bash
pip install pylint vulture pytest pytest-cov
```

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

## 🚨 **Troubleshooting**

**No Python files found?**
```bash
python3 cq_set_config.py --project /your/project --show-detection
```

**Tool import errors?**
```bash
pip install pylint vulture pytest pytest-cov
```

**Need help?** Run any command with `--help` or check our [detailed documentation](docs/).

---

## 📚 **Documentation**

- 📖 **[Complete Examples](EXAMPLES.md)** - Advanced usage patterns
- ⚡ **[Performance Guide](PERFORMANCE.md)** - Optimization tips  
- 🔧 **[Configuration](docs/configuration.md)** - Advanced setup
- 🤝 **[Contributing](CONTRIBUTING.md)** - Add new tools

---

## 🎯 **Perfect For**

- 👨‍💻 **Developers** - Quick quality checks during development
- 🏢 **Teams** - Standardized analysis across projects  
- 🤖 **CI/CD** - Automated quality gates
- 📊 **Managers** - Quality metrics and technical debt tracking

---

<div align="center">

**Start analyzing your Python projects in seconds!** 🚀

[⭐ Star this repo](../../stargazers) | [🐛 Report issues](../../issues) | [💡 Request features](../../issues/new)

</div>