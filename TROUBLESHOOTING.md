# 🚨 Troubleshooting Guide

## ⚠️ **Common Pitfalls**

### **1. Analyzing projects with restricted permissions**
**Symptoms**: "No Python files found" or "Permission denied" errors

```bash
# ❌ Common cause of analysis failures
# ✅ Solution: Ensure read access to target project
chmod -R +r /path/to/target/project

# ✅ Alternative: Check specific directory permissions
ls -la /path/to/target/project
find /path/to/target/project -name "*.py" -type f | head -5
```

### **2. Large project performance expectations**
**Symptoms**: Analysis takes much longer than expected

```bash
# ⚠️ EXPECTATION: Enterprise projects (5K+ files) 
# May take 3-8 minutes for comprehensive analysis

# ✅ Solution: Use appropriate preset for project size
python3 cq_run_analysis.py --preset quick      # <1 min for large projects
python3 cq_run_analysis.py --preset standard   # 1-3 min for large projects
python3 cq_run_analysis.py --preset comprehensive  # 3-8 min for large projects
```

### **3. Missing tool dependencies**
**Symptoms**: ImportError or "Tool not found" messages

```bash
# ⚠️ Tools gracefully fail if dependencies missing
# ✅ Solution: Install missing dependencies
pip install pylint vulture pytest pytest-cov

# ✅ Check what's installed
pip list | grep -E "(pylint|vulture|pytest|coverage)"

# ✅ Install all optional dependencies at once
pip install pylint vulture pytest pytest-cov bandit safety
```

### **4. Configuration persistence confusion**
**Symptoms**: Tool analyzes wrong directory or can't find config

```bash
# ℹ️ Configuration is saved per workspace
# Each terminal session remembers the last --project setting

# ✅ Solution: Verify current configuration
cat cq_active_config.json

# ✅ Show what will be detected
python3 cq_set_config.py --project /your/project --show-detection

# ✅ Reset configuration if needed
rm cq_active_config.json
python3 cq_set_config.py --project /correct/project
```

---

## 🔧 **Common Issues & Solutions**

### **Issue 1: No Python files found**
**Error Message**: `❌ No Python files found in the specified directories`

#### **Diagnosis**
```bash
# Check current configuration
python3 cq_set_config.py --project /your/project --show-detection

# Manually verify Python files exist
find /your/project -name "*.py" -type f | head -10

# Check if files are being excluded
ls -la /your/project
```

#### **Solutions**
```bash
# Solution A: Include specific directories
python3 cq_set_config.py --project /your/project --include src,app,lib

# Solution B: Reduce exclusions
python3 cq_set_config.py --project /your/project --exclude __pycache__

# Solution C: Check project structure
tree /your/project -I "__pycache__|*.pyc" | head -20
```

### **Issue 2: Virtual environment pollution**
**Symptoms**: Analysis includes venv files, very slow performance

#### **Diagnosis**
```bash
# Check if venv directories are being analyzed
grep -r "venv\|virtualenv" cq_active_config.json

# Look for common venv indicators
ls -la /your/project | grep -E "(venv|env|virtualenv)"
```

#### **Solutions**
```bash
# Solution A: Automatic exclusion should work
python3 cq_set_config.py --project /your/project --show-detection

# Solution B: Manual exclusion if automatic fails
python3 cq_set_config.py --project /your/project \
    --exclude venv,.venv,env,.env,virtualenv

# Solution C: Move venv outside project directory (best practice)
mv /your/project/venv /your/venvs/project_venv
```

### **Issue 3: Tool import errors**
**Error Message**: `ModuleNotFoundError: No module named 'pylint'`

#### **Diagnosis**
```bash
# Check Python environment
which python3
python3 -c "import sys; print(sys.path)"

# Check installed packages
pip list | grep -E "(pylint|vulture|pytest)"

# Verify virtual environment
echo $VIRTUAL_ENV
```

#### **Solutions**
```bash
# Solution A: Install missing dependencies
pip install pylint vulture pytest pytest-cov

# Solution B: Install in correct environment
pip install --user pylint vulture pytest pytest-cov

# Solution C: Use specific Python version
python3.9 -m pip install pylint vulture pytest pytest-cov

# Solution D: Tools gracefully fail - check reports
ls cq_reports/
cat cq_reports/analysis_summary.json
```

### **Issue 4: Permission errors**
**Error Message**: `PermissionError: [Errno 13] Permission denied`

#### **Diagnosis**
```bash
# Check directory permissions
ls -la /path/to/target/project

# Check file permissions
find /path/to/target/project -name "*.py" ! -readable

# Check ownership
ls -la /path/to/target/project | head -5
```

#### **Solutions**
```bash
# Solution A: Fix permissions
chmod -R +r /path/to/target/project

# Solution B: Change ownership (if you're admin)
sudo chown -R $USER:$USER /path/to/target/project

# Solution C: Copy to accessible location
cp -r /restricted/project /tmp/project_copy
python3 cq_set_config.py --project /tmp/project_copy
```

### **Issue 5: Memory/performance issues**
**Symptoms**: System runs out of memory, very slow analysis

#### **Diagnosis**
```bash
# Check system resources
free -h
df -h

# Monitor during analysis
top -p $(pgrep -f cq_run_analysis)

# Check project size
find /your/project -name "*.py" | wc -l
du -sh /your/project
```

#### **Solutions**
```bash
# Solution A: Exclude large directories
python3 cq_set_config.py --project /your/project \
    --exclude data,logs,node_modules,build,dist

# Solution B: Use faster presets
python3 cq_run_analysis.py --preset quick

# Solution C: Run tools individually
python3 cq_run_analysis.py --tools code_metrics
python3 cq_run_analysis.py --tools docstrings
python3 cq_run_analysis.py --tools pylint

# Solution D: Increase swap space (Linux)
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

---

## 🔍 **Debug Commands**

### **Configuration Debugging**
```bash
# Show current configuration
cat cq_active_config.json | python3 -m json.tool

# Test configuration detection
python3 cq_set_config.py --project /your/project --show-detection

# Validate project structure
tree /your/project -I "__pycache__|*.pyc|venv" | head -30

# Check Python files manually
find /your/project -name "*.py" -type f | head -10
```

### **Tool-Specific Debugging**
```bash
# Test individual tools
python3 cq_run_analysis.py --tools code_metrics
python3 cq_run_analysis.py --tools docstrings
python3 cq_run_analysis.py --tools pylint

# Check tool availability
python3 -c "import pylint; print('Pylint available')"
python3 -c "import vulture; print('Vulture available')"
python3 -c "import pytest; print('Pytest available')"

# Run tools with verbose output
python3 cq_run_analysis.py --tools pylint --verbose  # If available
```

### **Report Debugging**
```bash
# Check report generation
ls -la cq_reports/
cat cq_reports/analysis_summary.json | python3 -m json.tool

# Validate JSON reports
for report in cq_reports/*.json; do
    echo "Checking $report..."
    python3 -m json.tool "$report" > /dev/null && echo "✅ Valid" || echo "❌ Invalid"
done

# Check report timestamps
stat cq_reports/*.json
```

### **System Debugging**
```bash
# Check Python environment
python3 --version
which python3
echo $PYTHONPATH

# Check available disk space
df -h .
du -sh cq_reports/

# Check memory usage
free -h
ps aux | grep python3

# Check process limits
ulimit -a
```

---

## 🚨 **Error Message Reference**

### **Configuration Errors**

#### **`FileNotFoundError: No such file or directory`**
```bash
# Cause: Project path doesn't exist
# Solution:
ls -la /path/to/project  # Verify path exists
python3 cq_set_config.py --project /correct/path/to/project
```

#### **`ValueError: No Python files found`**
```bash
# Cause: No .py files in include directories
# Solution:
python3 cq_set_config.py --project /your/project --show-detection
python3 cq_set_config.py --project /your/project --include src,app
```

### **Analysis Errors**

#### **`ImportError: No module named 'pylint'`**
```bash
# Cause: Pylint not installed
# Solution:
pip install pylint
```

#### **`subprocess.CalledProcessError: Command 'pylint' failed`**
```bash
# Cause: Pylint execution error
# Solution:
pylint --version  # Test pylint directly
python3 cq_run_analysis.py --tools code_metrics,docstrings  # Skip pylint
```

#### **`MemoryError` or system freezing**
```bash
# Cause: Insufficient memory
# Solution:
python3 cq_set_config.py --project /your/project --exclude large_dir/
python3 cq_run_analysis.py --preset quick
```

### **Report Errors**

#### **`JSONDecodeError: Expecting value`**
```bash
# Cause: Corrupted report file
# Solution:
rm cq_reports/*.json
python3 cq_run_analysis.py --preset quick  # Regenerate
```

#### **`PermissionError: [Errno 13] Permission denied: 'cq_reports'`**
```bash
# Cause: No write permission for reports directory
# Solution:
chmod 755 .
mkdir -p cq_reports
chmod 755 cq_reports
```

---

## 💡 **Prevention Tips**

### **Before Running Analysis**
1. **Verify project path**: `ls -la /your/project`
2. **Check Python files**: `find /your/project -name "*.py" | head -5`
3. **Test configuration**: `python3 cq_set_config.py --project /your/project --show-detection`
4. **Check disk space**: `df -h .`
5. **Verify dependencies**: `pip list | grep -E "(pylint|vulture|pytest)"`

### **For Large Projects**
1. **Start with quick preset**: `python3 cq_run_analysis.py --preset quick`
2. **Exclude unnecessary directories**: `--exclude node_modules,venv,data`
3. **Monitor system resources**: `top` or `htop`
4. **Run tools incrementally**: One tool at a time for very large projects

### **For CI/CD**
1. **Pin dependency versions**: Include versions in requirements.txt
2. **Cache dependencies**: Use CI caching for pip installs
3. **Set timeouts**: Prevent infinite hangs
4. **Validate configuration**: Test locally first

---

## 🆘 **Getting Help**

### **Self-Diagnosis Checklist**
- [ ] Project path exists and is readable
- [ ] Python files exist in the project
- [ ] Configuration shows expected directories
- [ ] Required dependencies are installed
- [ ] Sufficient disk space and memory
- [ ] Reports directory is writable

### **Information to Gather**
When seeking help, please provide:

```bash
# System information
python3 --version
pip --version
uname -a  # (Linux/macOS)

# Project information
python3 cq_set_config.py --project /your/project --show-detection
find /your/project -name "*.py" | wc -l

# Error details
python3 cq_run_analysis.py --preset quick 2>&1 | tail -20

# Configuration
cat cq_active_config.json
```

### **Common Fixes Summary**
1. **No Python files**: Check includes/excludes with `--show-detection`
2. **Import errors**: Install dependencies with `pip install pylint vulture pytest pytest-cov`
3. **Permission errors**: Fix with `chmod -R +r /your/project`
4. **Performance issues**: Use `--preset quick` or exclude large directories
5. **Memory issues**: Run tools individually or exclude data directories

This troubleshooting guide should resolve 95% of common issues! 🚀 