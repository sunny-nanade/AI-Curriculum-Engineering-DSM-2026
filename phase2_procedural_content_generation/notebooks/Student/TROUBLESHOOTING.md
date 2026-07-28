# Troubleshooting Guide - Dynamic Systems Modeling Course

When things go wrong (and they will!), this guide helps you fix them systematically.

---

## General Debugging Strategy

**STOP. THINK. DEBUG.**

1. **Read the error message carefully** - It usually tells you exactly what's wrong
2. **Check the obvious first** - Typos, missing imports, cell execution order
3. **Simplify** - Comment out code until minimal example works
4. **Test incrementally** - One change at a time
5. **Print everything** - When confused, print intermediate values
6. **Ask for help** - After trying above, ask with specific error message

---

## Python & Environment Issues

### Error: "ModuleNotFoundError: No module named 'numpy'"

**Cause**: Package not installed or wrong Python environment

**Solution**:
```powershell
# Check if virtual environment is activated
# Should see (.venv) in prompt

# If not activated, activate it:
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1

# Then install missing package:
pip install numpy scipy matplotlib
```

**Prevention**: Always activate virtual environment before starting work

---

### Error: "python: command not found" (Windows/Mac/Linux)

**Cause**: Python not installed or not in PATH

**Solution**:
1. Download Python from https://www.python.org/downloads/
2. During installation, CHECK "Add Python to PATH"
3. Restart terminal
4. Verify: `python --version`

---

### Error: "cannot be loaded because running scripts is disabled"

**Cause**: Windows PowerShell execution policy (first-time setup issue)

**Solution**:
```powershell
# Run PowerShell as Administrator, then:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Explanation**: This allows you to run local scripts (virtual environment activation)

---

### Error: "Kernel died" or "Kernel not responding"

**Cause**: Code crashed the Python kernel (infinite loop, out of memory, etc.)

**Solution**:
1. In Jupyter menu: `Kernel` → `Restart Kernel`
2. Rerun cells in order from top
3. If problem persists, check for:
   - Infinite loops
   - Very large arrays (memory issue)
   - Division by zero in ODE solver

**Prevention**: Test code on small examples first, then scale up

---

## Jupyter Notebook Issues

### Error: "NameError: name 'np' is not defined"

**Cause**: Forgot to run import cell or ran cells out of order

**Solution**:
```python
# Make sure this cell was run:
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
```

**Best practice**: Always run import cell first when opening notebook

---

### Error: Cell output shows "[*]" and never finishes

**Cause**: Code is stuck in infinite loop or very slow computation

**Solution**:
1. Click "Interrupt Kernel" button (square stop icon) or press `I` twice
2. Check your code for:
   - `while True:` without break condition
   - Very large array operations
   - Very small step size in numerical integration

**Debug approach**:
```python
# Add progress indicators
for i in range(n):
    if i % 100 == 0:
        print(f"Progress: {i}/{n}")
    # ... rest of code
```

---

### Error: "JavaScript output is disabled in JupyterLab"

**Cause**: Using Jupyter Lab instead of Jupyter Notebook with certain interactive plots

**Solution**: Use Jupyter Notebook (not Lab) or use different plotting backend

---

### Issue: Plots don't show up

**Cause**: Missing `plt.show()` or wrong backend

**Solution**:
```python
# At top of notebook, add:
%matplotlib inline

# At end of plotting code, add:
plt.show()
```

---

## numpy/Mathematics Issues

### Error: "ValueError: operands could not be broadcast together"

**Cause**: Trying to add/multiply arrays of incompatible shapes

**Solution**:
```python
# Check shapes of your arrays
print(f"Array a shape: {a.shape}")
print(f"Array b shape: {b.shape}")

# Common fixes:
# 1. If one is (3,) and other is (3,1), use reshape:
a = a.reshape(-1, 1)

# 2. If need to transpose:
b = b.T

# 3. If element-wise operation needed:
result = a * b  # element-wise multiplication
```

**Common mistake**:
```python
# Wrong: trying to multiply (3,) with (4,)
v1 = np.array([1,2,3])
v2 = np.array([1,2,3,4])
# result = v1 * v2  # ERROR!

# Right: ensure same size
v1 = np.array([1,2,3])
v2 = np.array([4,5,6])
result = v1 * v2  # OK
```

---

### Error: "LinAlgError: Singular matrix"

**Cause**: Trying to invert a matrix that's not invertible (determinant = 0)

**Solution**:
```python
# Check determinant first
det = np.linalg.det(M)
print(f"Determinant: {det}")

if abs(det) < 1e-10:
    print("Matrix is singular or nearly singular!")
    # Use pseudo-inverse instead:
    M_inv = np.linalg.pinv(M)
else:
    M_inv = np.linalg.inv(M)
```

**Common causes**:
- Rows or columns are linearly dependent
- Matrix represents degenerate constraint
- Numerical round-off errors

---

### Warning: "RuntimeWarning: divide by zero"

**Cause**: Division by zero in calculation

**Solution**:
```python
# Add checks before division
if abs(denominator) < 1e-10:
    print("Warning: denominator near zero!")
    result = 0  # or handle appropriately
else:
    result = numerator / denominator
```

**In ODE solvers**: Often indicates singularity in equations - check your formulation

---

### Warning: "RuntimeWarning: invalid value encountered in sqrt"

**Cause**: Taking square root of negative number

**Solution**:
```python
# Check before taking sqrt
if value < 0:
    print(f"Cannot take sqrt of {value}")
    # Handle appropriately
else:
    result = np.sqrt(value)
```

**Common in**: Constraint solving, inverse kinematics - may indicate infeasible configuration

---

## matplotlib/Visualization Issues

### Issue: Plot labels are cut off

**Solution**:
```python
plt.figure(figsize=(8, 6))
# ... plotting code ...
plt.tight_layout()  # Automatically adjust spacing
plt.show()
```

---

### Issue: Legend covers data

**Solution**:
```python
# Position legend outside plot area
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Or use best position automatically
plt.legend(loc='best')
```

---

### Issue: Axes scales are wrong (one axis tiny)

**Solution**:
```python
# Use equal aspect ratio for x-y plots
plt.axis('equal')

# Or set limits manually
plt.xlim(-5, 5)
plt.ylim(-3, 3)
```

---

### Issue: Too many subplots, can't see details

**Solution**:
```python
# Increase figure size
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Add spacing between subplots
plt.tight_layout(pad=2.0)
```

---

## scipy/ODE Solver Issues

### Error: "ValueError: y0 must be 1-dimensional"

**Cause**: Initial conditions not in correct format

**Solution**:
```python
# Wrong:
y0 = [[1], [0]]  # 2D array

# Right:
y0 = [1, 0]  # 1D list or array
# or
y0 = np.array([1, 0])  # 1D numpy array
```

---

### Error: "Required step size is less than spacing between numbers"

**Cause**: ODE is stiff or has numerical issues, solver can't proceed

**Solution**:
```python
# 1. Use stiff solver
sol = solve_ivp(ode, t_span, y0, method='Radau')

# 2. Loosen tolerances
sol = solve_ivp(ode, t_span, y0, rtol=1e-6, atol=1e-8)

# 3. Check ODE formulation for division by zero or singularities
```

---

### Warning: "The evaluation of the system of equations failed"

**Cause**: ODE function returned NaN or Inf

**Solution**:
```python
# Add checks in ODE function
def my_ode(t, y):
    # ... calculations ...
    
    # Check for problems
    if np.any(np.isnan(dydt)):
        print(f"NaN at t={t}, y={y}")
    if np.any(np.isinf(dydt)):
        print(f"Inf at t={t}, y={y}")
    
    return dydt
```

**Common causes**:
- Division by zero in denominator
- Square root of negative number
- Exponential overflow
- Constraint violation

---

### Issue: Simulation results look wrong (not physical)

**Check these systematically**:

1. **Units consistency**:
```python
# Are all quantities in SI units?
m = 1.0  # kg
g = 9.81  # m/s^2 (not cm/s^2!)
L = 0.5  # m (not mm!)
```

2. **Sign errors**:
```python
# Check signs in equations
# Gravity is usually negative:
F_grav = -m * g  # downward

# Spring restoring force opposes displacement:
F_spring = -k * x  # toward equilibrium
```

3. **Initial conditions**:
```python
# Check what initial conditions mean
y0 = [x0, theta0, v0, omega0]
# Are angles in radians? (not degrees!)
theta0 = 30 * np.pi/180  # Convert degrees to radians
```

4. **Conservation laws**:
```python
# Check if energy is conserved (for conservative systems)
E_initial = compute_energy(y0)
E_final = compute_energy(y[-1])
print(f"Energy change: {abs(E_final - E_initial) / E_initial * 100:.3f}%")
# Should be < 0.01% for good accuracy
```

5. **Order of magnitude**:
```python
# Do results make physical sense?
print(f"Max velocity: {np.max(np.abs(v))} m/s")
# If 1000 m/s for a pendulum, something's wrong!
```

---

## Conceptual/Mathematical Issues

### Issue: "I don't understand what this equation means"

**Strategy**:
1. **Check dimensions**: Does left side have same units as right side?
2. **Look at limiting cases**: What happens if theta → 0? If m → 0?
3. **Draw a diagram**: Sketch the system, draw forces/vectors
4. **Check the theory**: Re-read markdown cells above the equation
5. **Compare to simple example**: How does it reduce to simpler system you know?

---

### Issue: "I don't know how to start this problem"

**Strategy**:
1. **Sketch the system**: Draw it, label coordinates
2. **Identify knowns and unknowns**: What's given? What are you solving for?
3. **Choose coordinates**: What variables describe configuration?
4. **Choose method**: Lagrangian? Newton? Energy? Which is easiest?
5. **Start simple**: Can you solve simpler version first?

**Example**:
```
Problem: Double pendulum dynamics
Too hard? Start with:
  - Single pendulum first
  - Then add second pendulum
  - Build up complexity
```

---

### Issue: "My derivation doesn't match the expected result"

**Debug steps**:
1. **Check algebra carefully**: Go line by line
2. **Verify each differentiation**: d/dt of each term
3. **Check signs**: Easy to flip sign of term
4. **Verify trig identities**: sin²θ + cos²θ = 1, etc.
5. **Compare dimensions**: Each term same units?
6. **Try numerical values**: Plug in numbers, does it work?

---

### Issue: "Simulation explodes / goes to infinity"

**Causes and fixes**:

1. **Time step too large** (manual integration):
```python
# Try smaller step size
h = 0.001  # instead of 0.1
```

2. **Stiff system** (scipy):
```python
# Use stiff solver
sol = solve_ivp(ode, t_span, y0, method='Radau')
```

3. **Wrong sign in equation**:
```python
# Check: restoring forces should oppose motion
# If theta increases, torque should be negative
```

4. **Numerical instability**:
```python
# Use higher accuracy method
sol = solve_ivp(ode, t_span, y0, method='DOP853', rtol=1e-10)
```

---

## Performance Issues

### Issue: Code runs very slowly

**Optimization strategies**:

1. **Avoid loops in numpy**:
```python
# Slow (loop):
result = np.zeros(n)
for i in range(n):
    result[i] = x[i]**2

# Fast (vectorized):
result = x**2
```

2. **Use appropriate solver method**:
```python
# For non-stiff, RK45 is fast and accurate
sol = solve_ivp(ode, t_span, y0, method='RK45')

# For stiff, use Radau or BDF
sol = solve_ivp(ode, t_span, y0, method='Radau')
```

3. **Reduce output points**:
```python
# Don't need 10000 points usually
t_eval = np.linspace(0, 10, 1000)  # instead of 10000
sol = solve_ivp(ode, t_span, y0, t_eval=t_eval)
```

4. **Profile your code**:
```python
import time

start = time.time()
# ... code to time ...
end = time.time()
print(f"Elapsed: {end - start:.3f} seconds")
```

---

## Getting Help Effectively

When you need to ask for help, provide:

1. **Error message** (full text, including traceback)
2. **What you tried** (show your code)
3. **What you expected** (describe intended behavior)
4. **Minimal example** (simplest code that shows problem)

**Good help request**:
```
Problem: Getting ValueError when trying to simulate pendulum

Error message:
  ValueError: operands could not be broadcast together with shapes (3,) (4,)

My code:
  def pendulum(t, y):
      theta, omega = y
      g, L = 9.81, 1.0
      return [omega, -g/L * np.sin(theta)]
  
  y0 = [np.pi/4, 0, 0]  # Initial conditions
  
Expected: Pendulum oscillation
Tried: Checked numpy documentation, restarted kernel

What am I doing wrong?
```

**Bad help request**:
```
My code doesn't work. Help!
```

---

## Prevention Checklist

Use this before you start coding to prevent common issues:

- [ ] Virtual environment activated (`(.venv)` in prompt)
- [ ] Imports cell run first
- [ ] Problem sketched on paper
- [ ] Coordinates/variables defined clearly
- [ ] Units consistent (SI units recommended)
- [ ] Expected behavior estimated (order of magnitude)
- [ ] Testing approach planned (what to check?)

Use this after coding to catch errors:

- [ ] Code runs without errors
- [ ] Results have correct magnitude
- [ ] Units make sense
- [ ] Signs make sense (gravity negative, etc.)
- [ ] Conservation laws satisfied (if applicable)
- [ ] Limiting cases work (theta → 0, etc.)
- [ ] Visualizations look reasonable

---

## When All Else Fails

1. **Take a break** - Fresh eyes often spot the problem
2. **Explain to rubber duck** - Describe problem out loud, step by step
3. **Start over from scratch** - Sometimes faster than debugging
4. **Ask classmate** - Fresh perspective helps
5. **Attend office hours** - Instructor/TA can help
6. **Search online** - Stack Overflow has everything
7. **Check teacher notebook** - See how it should be done

---

**Remember**: Everyone debugs. Even experts spend 50% of time debugging. It's part of learning!

**Pro tip**: Keep notes of errors you encountered and how you fixed them. You'll encounter them again!
