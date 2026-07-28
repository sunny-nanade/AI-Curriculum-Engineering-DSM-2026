# Student Notebooks - Dynamic Systems Modeling

Welcome! This folder contains all student versions of the course notebooks. Work through these systematically to build your understanding of dynamic systems.

## Getting Started

### Prerequisites
1. Python 3.10+ installed
2. VS Code with Python and Jupyter extensions
3. Virtual environment activated (see main README.md)
4. All packages installed: `pip install -r requirements.txt`

### How to Use These Notebooks

Each notebook contains:
- **Theory**: Complete explanations and equations (read carefully!)
- **Examples**: Worked solutions you can study
- **Exercises**: Code cells with `# TODO:` comments - this is where YOU work
- **Hints**: Guidance on approach and methods

**Learning Strategy**:
1. Read all theory sections first
2. Study the worked examples thoroughly
3. Try exercises WITHOUT looking at teacher solutions
4. Test your code frequently (run cells as you go)
5. Compare with teacher version only after attempting yourself

## Course Structure (36 hours total)

### Unit 1: Introduction to Kinematics (3 hours)
**What you'll learn**: Position, velocity, acceleration in different coordinate systems

- `S_U1_L1_Introduction_Position.ipynb` - Position vectors and paths
- `S_U1_L2_Velocity_Acceleration.ipynb` - Time derivatives
- `S_U1_L3_Coordinate_Systems.ipynb` - Cartesian, polar, cylindrical, spherical
- `S_U1_P1_Introduction_to_Colab.ipynb` - Environment setup
- `S_U1_P2_Custom_Motion_Design.ipynb` - Design your own motion

**Skills**: Vector calculus, coordinate transformations, Python basics

---

### Unit 2: Lagrangian Mechanics (4 hours)
**What you'll learn**: Energy-based approach to dynamics

- `S_U2_L1_Newtons_Laws_Force_Formulation.ipynb` - Force-based approach
- `S_U2_L2_Lagrangian_Mechanics.ipynb` - Energy-based approach
- `S_U2_P1_Newton_vs_Lagrange.ipynb` - Compare both methods

**Skills**: Kinetic/potential energy, Euler-Lagrange equations, generalized coordinates

---

### Unit 3: Rigid Body Kinematics (5.5 hours)
**What you'll learn**: Rotation matrices, angular velocity, moving reference frames

- `S_U3_L1_Fixed_Frame_Kinematics.ipynb` - Rigid body motion basics
- `S_U3_L2_Acceleration_Fixed_Frame.ipynb` - Acceleration analysis
- `S_U3_L3_Rotating_Frames_Part1.ipynb` - Moving reference frames
- `S_U3_L4_Coriolis_Acceleration.ipynb` - Coriolis and centrifugal effects
- `S_U3_L5_Euler_Angles.ipynb` - 3D rotation representations
- `S_U3_P1_Rotating_Frames_Practical.ipynb` - Practical applications

**Skills**: Rotation matrices, angular velocity vectors, reference frame transformations

---

### Unit 4: Particle Kinetics (4.5-5.5 hours)
**What you'll learn**: Forces, constraints, and motion of particles

- `S_U4_L1_Constrained_Particle_Motion.ipynb` - Constraints and forces
- `S_U4_L2_Pulley_Systems.ipynb` - Pulley mechanics
- `S_U4_L3_3D_Motion_CNC.ipynb` - 3D trajectory following
- `S_U4_P1_Particle_Kinetics_Workshop.ipynb` - Integrated problems

**Skills**: Free body diagrams, constraint forces, 3D dynamics

---

### Unit 5: Rigid Body Kinetics & Vibrations (9.5 hours)
**What you'll learn**: Equations of motion for rigid bodies, vibration analysis

- `S_U5_L1_Rigid_Body_Equations_of_Motion.ipynb` - Newton-Euler equations
- `S_U5_L2_Coupled_Systems_and_Mechanisms.ipynb` - Multiple connected bodies
- `S_U5_L3_Multi_DOF_Rigid_Body_Systems.ipynb` - Complex systems
- `S_U5_L4_Single_DOF_Vibrations.ipynb` - Natural frequency, damping
- `S_U5_L5_MDOF_Modal_Analysis.ipynb` - Mode shapes and frequencies
- `S_U5_P1_Modal_Testing_Practical.ipynb` - Experimental modal analysis

**Skills**: Inertia tensors, Euler's equations, modal analysis, frequency response

---

### Unit 6: Work & Energy Methods (4 hours)
**What you'll learn**: Alternative approaches using energy and momentum

- `S_U6_L1_Work_Energy_Theorem.ipynb` - Work, energy, power
- `S_U6_L2_Impulse_Momentum.ipynb` - Impulse-momentum, collisions
- `S_U6_P1_Energy_Momentum_Methods.ipynb` - Method selection and comparison

**Skills**: Energy conservation, momentum conservation, impact analysis, method selection

---

### Unit 7: Numerical Simulations (4 hours)
**What you'll learn**: Simulate complex systems numerically

- `S_U7_L1_Numerical_ODE_Integration.ipynb` - Euler, RK4, scipy solvers
- `S_U7_L2_Multi_Body_Simulation.ipynb` - Double pendulum, mechanisms
- `S_U7_P1_Complete_System_Simulation.ipynb` - Complete system analysis

**Skills**: ODE integration, chaos, multi-body dynamics, method comparison

---

## Learning Path

### Recommended Sequence
Work through units in order (1 → 7). Each unit builds on previous concepts.

### Suggested Pace
- **Lectures**: 90 minutes each (study + exercises)
- **Practicals**: 150 minutes each (hands-on application)
- **Weekly**: Complete 1 unit per week (3-4 notebooks)

### Self-Assessment

After each unit, ask yourself:
- Can I explain the key concepts to someone else?
- Can I solve similar problems without hints?
- Do I understand why we use this approach?
- Can I apply this to a new system?

If not, review the theory and try more problems!

## Tips for Success

### 1. Active Learning
- Don't just read - WRITE code
- Modify examples to see what happens
- Break things intentionally to understand errors

### 2. Incremental Development
- Write code in small steps
- Test after EVERY change
- Use print statements liberally for debugging

### 3. Understand, Don't Memorize
- Focus on concepts, not formulas
- Draw diagrams for every problem
- Explain your approach in comments

### 4. Use Resources
- Consult teacher notebooks AFTER attempting
- Search documentation when stuck
- Discuss with classmates (learn together!)

### 5. Practice, Practice, Practice
- Redo problems without looking at solutions
- Try variations (different parameters, systems)
- Create your own examples

## Common Pitfalls to Avoid

1. **Skipping Theory**: Don't jump to code without understanding concepts
2. **Copy-Paste**: Type everything yourself to build muscle memory
3. **Not Testing**: Run cells frequently, don't wait until the end
4. **Ignoring Errors**: Read error messages - they tell you what's wrong!
5. **Working Alone**: Collaboration enhances learning (explain to teach yourself)

## Troubleshooting

### Code Won't Run
- Check for typos (Python is case-sensitive!)
- Verify all previous cells have been executed
- Make sure imports are at the top
- Restart kernel if strange errors persist

### Wrong Results
- Check units (meters vs millimeters, radians vs degrees)
- Verify signs (positive vs negative directions)
- Print intermediate values to find where it goes wrong
- Compare with worked examples

### Concepts Unclear
- Re-read theory sections slowly
- Draw diagrams and free body diagrams
- Work through examples step-by-step
- Ask questions in class or office hours

## Tools and Libraries

### Core Libraries Used
- **numpy**: Array operations, linear algebra, math functions
- **matplotlib**: Plotting and visualization
- **scipy**: ODE solvers, optimization, signal processing

### Quick References
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Common numpy operations
v = np.array([1, 2, 3])           # Vector
M = np.array([[1,2],[3,4]])       # Matrix
np.dot(v, v)                      # Dot product
np.cross(v1, v2)                  # Cross product
np.linalg.norm(v)                 # Magnitude
np.linalg.inv(M)                  # Matrix inverse

# Common matplotlib
plt.plot(t, x)                    # Line plot
plt.scatter(x, y)                 # Scatter plot
plt.xlabel('Time (s)')            # Labels
plt.legend()                      # Show legend
plt.grid(True)                    # Grid
plt.show()                        # Display
```

## Assessment

Your understanding will be evaluated through:
1. **In-notebook exercises**: Completion and correctness
2. **Practicals**: Application to integrated problems
3. **Final project**: Design and simulate your own system
4. **Exams**: Conceptual understanding and problem-solving

## Getting Help

- **During Labs**: Ask TA or instructor
- **Office Hours**: Posted on course website
- **Discussion Forum**: Collaborate with peers
- **Documentation**: Python docs, scipy docs, numpy docs

## Next Steps

1. Start with `S_U1_L1_Introduction_Position.ipynb`
2. Work through systematically
3. Complete all TODO sections
4. Check your work against teacher versions
5. Move to next unit when confident

**Remember**: The goal is UNDERSTANDING, not just completion. Take your time, think deeply, and enjoy the journey of learning dynamics!

---

## Additional Resources

### Course Materials
- Teacher notebooks in `notebooks/Teacher/` (reference after attempting)
- External references in `external/` folder
- Course syllabus and schedule on main page

### External Learning
- MIT OpenCourseWare: Dynamics and Control
- Khan Academy: Physics and Calculus
- 3Blue1Brown: Linear Algebra (YouTube)
- Scipy documentation and tutorials

### Python Help
- Official Python tutorial: docs.python.org
- Numpy quickstart: numpy.org
- Matplotlib gallery: matplotlib.org/gallery
- Stack Overflow: For specific coding questions

---

**Good luck and enjoy learning Dynamic Systems Modeling!**

*"The only way to learn mathematics is to do mathematics." - Paul Halmos*
