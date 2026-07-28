# Quick Start Guide - Getting Up and Running in 15 Minutes

This guide gets you from zero to running your first notebook in about 15 minutes.

---

## Step 1: Check Python Installation (2 minutes)

Open terminal (PowerShell on Windows, Terminal on Mac/Linux):

```powershell
# Check Python version (need 3.10 or higher)
python --version

# If not installed, download from https://www.python.org/downloads/
```

Expected output: `Python 3.10.x` or higher

---

## Step 2: Set Up Virtual Environment (3 minutes)

Navigate to course folder and create virtual environment:

```powershell
# Navigate to course folder
cd "D:\Sunny\DSM"

# Create virtual environment (one-time setup)
python -m venv .venv

# Activate virtual environment
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1

# Windows CMD:
.\.venv\Scripts\activate.bat

# Mac/Linux:
source .venv/bin/activate
```

You should see `(.venv)` before your command prompt.

---

## Step 3: Install Required Packages (5 minutes)

With virtual environment activated:

```powershell
# Install all required packages
pip install numpy scipy matplotlib jupyter notebook

# Verify installation
python -c "import numpy; import scipy; import matplotlib; print('All packages installed!')"
```

Expected output: `All packages installed!`

---

## Step 4: Launch Jupyter Notebook (1 minute)

```powershell
# Start Jupyter Notebook server
jupyter notebook
```

This opens your browser automatically. If not, copy the URL from terminal (looks like `http://localhost:8888/...`)

---

## Step 5: Open Your First Notebook (2 minutes)

In the Jupyter interface:

1. Navigate to `notebooks/Student/`
2. Click on `S_U1_L1_Position_Velocity_Acceleration.ipynb`
3. The notebook opens in a new tab

---

## Step 6: Run Your First Cell (2 minutes)

1. Click on the first code cell (has `import numpy as np`)
2. Press `Shift + Enter` to run it
3. Continue running cells with `Shift + Enter`

**Expected behavior**: Cell runs, output appears below, cursor moves to next cell.

---

## Common First-Time Issues

### Issue: "python: command not found"
**Solution**: Install Python from https://www.python.org/downloads/ and restart terminal

### Issue: "cannot activate virtual environment"
**Windows PowerShell Solution**:
```powershell
# May need to change execution policy (one-time)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Issue: "ModuleNotFoundError: No module named 'numpy'"
**Solution**: Ensure virtual environment is activated (see `(.venv)` in prompt), then install packages

### Issue: "Jupyter notebook won't start"
**Solution**:
```powershell
# Install/reinstall Jupyter
pip install --upgrade jupyter notebook
```

### Issue: "Kernel died" or "Kernel not responding"
**Solution**: In Jupyter menu, click `Kernel` → `Restart Kernel`

---

## VS Code Alternative Setup

If you prefer VS Code to browser-based Jupyter:

1. Install VS Code: https://code.visualstudio.com/
2. Install Python extension (Microsoft)
3. Install Jupyter extension (Microsoft)
4. Open folder: `File` → `Open Folder` → select `D:\Sunny\DSM`
5. Select Python interpreter:
   - `Ctrl+Shift+P` → "Python: Select Interpreter"
   - Choose the `.venv` interpreter
6. Open any `.ipynb` file and start coding!

**Advantages of VS Code**:
- Integrated terminal
- Better code completion
- Git integration
- All-in-one environment

---

## What to Do Next

### Option 1: Follow the Course Linearly
Start with Unit 1, Lecture 1 and work through systematically:
```
S_U1_L1 → S_U1_L2 → S_U1_P1 → S_U2_L1 → ...
```

### Option 2: Jump to Specific Topic
Use the README in Student folder to see unit topics and jump to what interests you.

### Option 3: Review Existing Teacher Notebooks First
If stuck, peek at `notebooks/Teacher/T_U1_L1_...` to see complete solutions, then try student version again.

---

## Keyboard Shortcuts (Jupyter)

Essential shortcuts to know:

| Action | Shortcut |
|--------|----------|
| Run cell, move to next | `Shift + Enter` |
| Run cell, stay in cell | `Ctrl + Enter` |
| Insert cell above | `A` (in command mode) |
| Insert cell below | `B` (in command mode) |
| Delete cell | `DD` (in command mode) |
| Enter edit mode | `Enter` |
| Enter command mode | `Esc` |
| Show shortcuts | `H` |
| Restart kernel | `00` (zero twice) |

**Command mode**: Blue cell border, can navigate/delete cells
**Edit mode**: Green cell border, can type code

---

## Your First Exercise

Try this in a new code cell to make sure everything works:

```python
import numpy as np
import matplotlib.pyplot as plt

# Create time vector
t = np.linspace(0, 2*np.pi, 100)

# Create position (circular motion)
x = np.cos(t)
y = np.sin(t)

# Plot trajectory
plt.figure(figsize=(6,6))
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('My First Trajectory!')
plt.grid(True)
plt.axis('equal')
plt.show()
```

**Expected**: A circular trajectory plot appears

If you see the circle, congratulations! You're ready to start the course!

---

## Getting Help

### During Setup
- Check this guide's "Common First-Time Issues" section
- Search error messages online (Stack Overflow usually has answers)
- Ask in course forum/Discord/Slack

### During Learning
- Read the Student README for learning strategies
- Check teacher notebooks AFTER attempting exercises
- Use SELF_ASSESSMENT.md to identify weak areas
- Attend office hours

---

## Important Files to Bookmark

- **Student README**: `notebooks/Student/README.md` - Comprehensive guide
- **Learning Objectives**: `LEARNING_OBJECTIVES.md` - What you'll learn
- **Self-Assessment**: `SELF_ASSESSMENT.md` - Check your understanding
- **This Guide**: `notebooks/Student/QUICK_START_GUIDE.md` - Come back if you need to set up again

---

## Pro Tips for Success

1. **Always activate virtual environment before starting**
   - Look for `(.venv)` in your prompt

2. **Run cells in order**
   - Jupyter cells have numbers [1], [2], etc.
   - Running out of order causes errors

3. **Restart kernel if confused**
   - Clears all variables
   - Fresh start

4. **Save often**
   - `Ctrl+S` or click save icon
   - Jupyter auto-saves but be safe

5. **Test frequently**
   - After every function definition
   - After every change
   - Print intermediate results

---

## Next Steps

After completing this quick start:

1. Read `notebooks/Student/README.md` for learning strategies
2. Review `LEARNING_OBJECTIVES.md` to see what you'll learn
3. Start with `S_U1_L1_Position_Velocity_Acceleration.ipynb`
4. Work through Unit 1 systematically
5. Use `SELF_ASSESSMENT.md` after completing each unit

---

**Welcome to the course! You're now ready to start learning. Good luck!**
