# Dynamic Systems Modeling (DSM) - Course Design Framework
## Outcome-Based Education (OBE) + Pedagogical Integration
### B.Tech Mechatronics Engineering, Sem IV

---

## EXECUTIVE SUMMARY

This document outlines a **unified, integrated course delivery system** combining:
- **VS Code + Jupyter Notebooks** (already native, no separate Jupyter server needed)
- **GitHub Classroom** (assessment, version control, peer review)
- **OBE methodology** (outcomes-driven, backward-designed curriculum)
- **Evidence-based pedagogy** (constructivism, scaffolding, active learning, Bloom's revised taxonomy)

**Technology Choice: VS Code REPLACES Jupyter's separate notebook server**
- VS Code natively supports Jupyter notebooks (`.ipynb` files) with full IDE capabilities
- Students install once, use one tool; no Jupyter server overhead
- Built-in Git integration for GitHub submissions
- Debugger, IntelliSense, terminal, and markdown rendering all in one editor

---

## PART 1: LEARNING SCIENCE FOUNDATION

### 1.1 Core Pedagogical Models Integrated

#### A. Constructivism (Piaget, von Glasersfeld)
**Principle:** Students build knowledge by actively engaging with problems and reflecting on experiences.
**Implementation in DSM:**
- Labs start with **concrete systems** (circular motion, mass-spring-damper) before abstract theory
- Students **modify parameters** and observe effects (constructive inquiry)
- Visualization of results encourages sense-making

#### B. Scaffolding (Vygotsky, Wood-Bruner)
**Principle:** Gradually reduce support as competence grows; respect the "Zone of Proximal Development."
**Implementation in DSM:**
- **Explain-Try-Challenge** structure in every lesson
  - *Explain:* Theory + visual context (5 min)
  - *Try:* Guided, fill-in-the-blank code (10 min)
  - *Challenge:* Open-ended problem, rubric provided (10 min)
- Each successive unit assumes mastery of prior scaffolds

#### C. Active Learning & Problem-Based Learning
**Principle:** Learning is enhanced when students engage in doing, not passively receiving.
**Implementation in DSM:**
- Every unit = hands-on simulation or measurement
- No passive lectures; all notebooks are interactive
- Homework = design/analyze novel systems (not memorization)

#### D. Bloom's Revised Taxonomy (Anderson & Krathwohl, 2001)
**Cognitive Levels (Bottom → Top):**
1. **Remember** (facts, terms) → Review cells in notebooks
2. **Understand** (explain concepts) → Watch animated Explain sections
3. **Apply** (use theory in new context) → Try sections with guided code
4. **Analyze** (break systems into components) → Challenge problems
5. **Evaluate** (make judgments with criteria) → Rubric-based grading
6. **Create** (design novel systems) → Semester capstone project

**Course Design:** Units spiral through these levels; early units focus on Understand→Apply; later units emphasize Analyze→Create.

---

## PART 2: OUTCOME-BASED EDUCATION (OBE) STRUCTURE

### 2.1 Course Learning Outcomes (CLOs) → Program Student Outcomes (PSOs)

| Course Learning Outcome | Description | Bloom Level | Program Outcome Mapping |
|---|---|---|---|
| **CO1** | Describe theoretical concepts in mathematical modelling (kinematics, kinetics, energy) | Understand, Apply | PSO3 (Math foundation), PSO4 (Problem-solving) |
| **CO2** | Analyze dynamic systems using constitutive laws (Newton's, Lagrange, energy methods) | Analyze, Evaluate | PSO4 (Analysis), PSO5 (Design) |
| **CO3** | Synthesize dynamic systems via modelling, simulation, and control design | Create, Evaluate | PSO5 (Synthesis), PSO6 (Tools & computing) |

### 2.2 Course Outcomes → Unit Outcomes → Learning Objectives (Micro)

Each unit maps outcomes to hourly micro-objectives:

**Example: Unit 1 (Kinematics, 3 hours)**
- CO1 (Describe theoretical concepts)
- **Unit Outcome:** Students will understand and convert between coordinate frames
- **Hour 1 Objective:** Convert circular motion between Cartesian and polar frames; interpret centripetal acceleration
- **Hour 2 Objective:** Extend to 3D cylindrical/spherical; relate angular rate to tangential speed
- **Hour 3 Objective:** Synthesize by converting user-designed trajectories; verify acceleration equivalence

### 2.3 NBA/ABET Alignment

India adopted NBA accreditation (signatory to Washington Accord, 2014). DSM maps to:

| NBA Criterion | DSM Component |
|---|---|
| **PO1:** Engineering knowledge (math, science, engineering) | Units 1-6: theoretical foundation |
| **PO2:** Problem analysis | Challenge sections; system analysis labs |
| **PO3:** Design/development of solutions | Unit 7; semester capstone |
| **PO4:** Investigation/experimentation | Hands-on labs with real data (Unit 7) |
| **PO5:** Tools & modern engineering tools | VS Code, Python, GitHub, simulation |
| **PO7:** Environment & sustainability | (Optional: energy-efficient system design challenges) |
| **PO8:** Ethics & social responsibility | (Optional: peer review, attribution, honest reporting) |

---

## PART 3: INTEGRATED COURSE DELIVERY SYSTEM

### 3.1 Technology Stack (Single, Unified)

```
┌─────────────────────────────────────────────────┐
│           STUDENT WORKFLOW                      │
├─────────────────────────────────────────────────┤
│                                                 │
│  1. Install VS Code (once)                     │
│  2. Clone student repo from GitHub Classroom   │
│  3. Create/activate venv in VS Code            │
│  4. Open notebook file (Unit X).ipynb          │
│     → VS Code + Jupyter extension renders      │
│       markdown, runs code cells, shows plots   │
│  5. Write code in "Try" and "Challenge" cells  │
│  6. Save, commit, push to GitHub               │
│  7. Auto-grading (GitHub Actions) + peer      │
│     review (pull requests)                     │
│                                                 │
└─────────────────────────────────────────────────┘
```

**Why NOT separate Jupyter server?**
- Students learn Git workflow (essential for engineering)
- One-time installation (less tech support)
- Version history, branching, collaboration built-in
- Institutional license allows unlimited private repos

### 3.2 GitHub Classroom Structure

```
GitHub Organization: YourUniversity/DSM-Sem4-Mechatronics

├── dsm-main (public, instructor reference)
│   ├── README.md (course overview, outcomes, grading)
│   ├── SYLLABUS_OBE.md (official syllabus + CO/PSO mapping)
│   ├── GETTING_STARTED.md (setup + troubleshooting)
│   ├── notebooks/
│   │   ├── 00_Unit1_[SOLUTION].ipynb
│   │   ├── 01_Unit2_[SOLUTION].ipynb
│   │   └── ... (all 7 units, fully worked examples)
│   ├── rubrics/
│   │   ├── unit_rubric_1.md
│   │   ├── assignment_rubric.md
│   │   └── project_rubric.md
│   └── src/ (helper functions, data)
│
├── dsm-student-template (private, starter repo)
│   ├── README.md (student instructions)
│   ├── notebooks/
│   │   ├── 00_Unit1_[BLANK].ipynb (empty Try/Challenge cells)
│   │   ├── 01_Unit2_[BLANK].ipynb
│   │   └── ...
│   ├── ASSIGNMENT_CHECKLIST.md
│   ├── .gitignore
│   └── src/ (starter code, helpers)
│
└── [Student-Name]-DSM-Sem4 (auto-created forks)
    ├── (copy of template)
    ├── notebooks/ (students work here)
    ├── SUBMIT.md (instructions for each assignment)
    └── auto-graded feedback (via GitHub Actions / comments)
```

### 3.3 Assessment Workflow

**Formative (In-progress):**
- Quick checks at end of each hour (auto-graded or self-checked)
- Peer review via pull requests (students comment on classmates' code)
- GitHub Issues for Q&A (tracked engagement)

**Summative (End of unit/course):**
- Unit labs: notebook submission + auto-grading + rubric feedback
- Semester project: design + simulation + presentation
- Final exam: theory + short code snippets (no rote memorization)

---

## PART 4: COURSE STRUCTURE (DETAILED)

### 4.1 Full Semester Roadmap

| Unit | Topic | Hours | CO | Key Activities | Assessment | Weight |
|---|---|---|---|---|---|---|
| **Pre** | Getting Started + Pre-course | 1 | - | Install, venv, first notebook run | Completion | - |
| **1** | Kinematics & Coordinate Frames | 3 | CO1 | Explain→Try→Challenge (circular, cylindrical, spherical motion) | Notebook + Quick Check | 5% |
| **2** | Constitutive Laws | 4 | CO1, CO2 | Derive Newton's 2nd law, Lagrange equations, examples | Problem set + Simulation | 10% |
| **3** | Rigid Body Kinematics | 5 | CO1 | DOF analysis, moving ref frames, Euler angles intro | Lab report | 10% |
| **4** | Particle Kinetics | 4 | CO2 | Pulley systems, 3D printer kinematics, constraint forces | Design challenge | 8% |
| **5** | Rigid Body Kinetics | 6 | CO1, CO2, CO3 | ODE-based 1 & 2-DOF systems, vibration, control intro | Simulation + analysis | 12% |
| **6** | Work & Energy | 4 | CO2 | Energy methods, power, dissipation, work-energy theorem | Lab + reflection | 10% |
| **7** | Advanced Topics | 4 | CO3 | Numerical ODE solvers, optimization, system ID, real data | Numerical project | 10% |
| **Semester Project** | Integrated Design | - | CO1, CO2, CO3 | Student-designed system (motor, arm, etc.) modeling & control | Final report + presentation | 25% |
| **Final Exam** | Written + Code | 2 hrs | All | Theory (short answer) + code reasoning (no memorization) | Exam | 10% |

### 4.2 Unit Template: Explain-Try-Challenge

**Every unit notebook follows this structure:**

```markdown
# Unit X: [Topic Name] (Y hours)

## Learning Outcomes
- Students will [specific observable action] by end of unit
- [Map to CO + Bloom level]

---

### Hour 1: [Subtopic]

#### Explain (5 min)
[Theory + intuition + visual or animation]
- Key equation: ... (with derivation or reference)
- Physical meaning: ...
- Real-world example: ...

#### Try (10 min)
[Guided, fill-in-the-blank code cells]
- Students complete missing parts (marked as TODO)
- Expected output shown
- Reflection prompt: "What changes if you modify X?"

#### Challenge (10 min)
[Open-ended, creative problem]
- Rubric provided inline
- Bonus extension (optional, +2%)

---

### Hour 2: [Subtopic]
[Same structure]

---

### Hour 3: [Subtopic]
[Synthesis/integration across hours]

---

## Quick Check (Self-assess or auto-graded)
[Simple problem to verify learning]
```

---

## PART 5: GRADING & ENGAGEMENT

### 5.1 Grading Rubric Example (Unit Lab)

| Criterion | Excellent (4) | Good (3) | Satisfactory (2) | Needs Improvement (1) |
|---|---|---|---|---|
| **Code Correctness** | All cells run, correct results, well-commented | Minor issues, mostly correct | Works but has bugs or unclear logic | Does not run or major errors |
| **Explanation** | Clear narrative, explains why (not just how) | Mostly explains concepts | Surface-level explanation | Missing or inaccurate |
| **Challenge Problem** | Creative solution, extends beyond spec | Meets all requirements | Partially complete | Incomplete or off-topic |
| **Git Practices** | Clear commits, good messages, clean history | Mostly clean commits | Vague messages, messy history | Single commit or no messages |

### 5.2 Engagement & Motivation

- **Weekly Wins:** Each hour-mark gets a emoji in README (visible progress)
- **Leaderboard (opt-in):** Fastest-running code, best visualization, peer review count
- **Bonus Labs:** +2% each for optional challenges (system ID from real data, Bode optimization, etc.)
- **Peer Review:** +1% per thoughtful review comment (GitHub Issues/PRs)
- **Milestone Badges:** "Kinematic Master," "Control Wizard," etc. (GitHub Discussions)

---

## PART 6: PRE-COURSE ONBOARDING (1 hour total)

### 6.1 Components

1. **Welcome Video (5 min)**
   - Course goals & structure
   - Weekly rhythm expectations
   - Grading overview
   - Link: embedded in README

2. **Setup Guide (15 min text + optional 10 min video walkthrough)**
   - Windows: install VS Code, Python, venv
   - Mac/Linux: same, with OS-specific notes
   - First notebook run checklist
   - Troubleshooting (common issues + fixes)

3. **GitHub Classroom Onboarding (10 min)**
   - How to accept assignment (link provided)
   - First push/commit
   - Submitting labs (PR workflow)

4. **Interactive Quick Start (15 min)**
   - Run your first code cell
   - Modify a parameter, re-run
   - Save & commit
   - Expected output screenshot

---

## PART 7: ALIGNMENT WITH BEST PRACTICES

### 7.1 How This Design Addresses Key Pedagogical Principles

| Principle | Implementation | Benefit |
|---|---|---|
| **Active Learning** | Every unit = hands-on code/simulation | 70% retention vs. 10% for passive |
| **Scaffolding** | Explain→Try→Challenge progression | Students don't get lost; confidence grows |
| **Constructivism** | Modify parameters, observe, reflect | Deep understanding, not surface memorization |
| **Immediate Feedback** | Auto-grading, inline quick checks, plots | Students adjust understanding real-time |
| **Social Learning** | Peer review, GitHub Issues Q&A | Collaborative problem-solving |
| **Transfer** | Challenge problems are novel contexts | Students apply theory beyond examples |
| **Metacognition** | Reflection prompts after Try sections | Students monitor own understanding |
| **OBE Clarity** | Outcomes stated upfront, rubric transparent | Students know exactly what is expected |

### 7.2 Common Misconceptions Avoided

**"Just give students code and they'll learn"**
→ Notebooks are **scaffolded**, not full solutions; Try/Challenge sections require active engagement

**"More theory makes stronger engineers"**
→ Theory + immediate practice with visualization = deeper learning

**"Grading only at end of course"**
→ Formative feedback throughout (quick checks, peer review); summative at milestones

---

## PART 8: IMPLEMENTATION PHASES

### Phase 0: NOW (1 week)
- [ ] Create OBE course document (this file + detailed outcomes)
- [ ] Create pre-course onboarding materials (GETTING_STARTED.md + optional video)
- [ ] Design grading rubrics (unit labs, project, exam)

### Phase 1: GitHub Setup (1 week)
- [ ] Create GitHub organization
- [ ] Create `dsm-main` (instructor reference repo)
- [ ] Create `dsm-student-template` (student starter template)
- [ ] Set up GitHub Classroom assignment

### Phase 2: Unit 1-3 Refactor (2-3 weeks)
- [ ] Refactor existing Unit 1 notebook to Explain-Try-Challenge
- [ ] Create Unit 2 (Constitutive Laws) notebook
- [ ] Create Unit 3 (Rigid Body Kinematics) notebook
- [ ] Populate `src/` with helper functions
- [ ] Test end-to-end: student clones, runs, submits

### Phase 3: Unit 4-7 + Capstone (3-4 weeks)
- [ ] Create Unit 4-7 notebooks
- [ ] Design semester capstone project brief
- [ ] Create autograding scripts (GitHub Actions, optional)
- [ ] Prepare final exam blueprint

### Phase 4: Soft Launch (1 week before semester)
- [ ] Test with 2-3 students (alpha test)
- [ ] Gather feedback, refine onboarding
- [ ] Fix any GitHub/venv issues
- [ ] Prepare video tutorials (record common errors)

---

## PART 9: INSTRUCTOR GUIDANCE

### 9.1 Lecture vs. Lab Delivery

**Lecture (2 hours/week):**
- Derive key equations on board (theory, intuition, physical meaning)
- No live coding; whiteboard + sketches
- Students take notes, ask questions
- Assign pre-lab reading (Explain section of notebook)

**Lab Practical (2 hours/week):**
- Students work through Try section with peer support
- Instructor circulates, helps debug, asks reflection questions
- Students start Challenge in class; finish at home
- Submit via GitHub by deadline

### 9.2 Handling Common Issues

| Issue | Solution |
|---|---|
| Student doesn't understand Explain section | Review lecture notes; point to textbook; offer office hours |
| Try section code doesn't run | Check venv activation, package versions; provide debugging checklist |
| Challenge problem too hard | Offer "scaffolding sheet" with hints; allow attempt at lower rubric level |
| Student copies peers' code | Emphasize Git history tracks authorship; discuss plagiarism policy upfront |
| Slow internet (can't push to GitHub) | Provide USB with starter repo; accept emailed .zip as backup |

### 9.3 Grading Workflow

1. **Student submits** (notebook pushed to GitHub by deadline)
2. **Auto-grading** (if set up): GitHub Actions checks for syntax, runs cells, captures outputs
3. **Manual rubric review** (instructor): Download notebook, check against rubric, add comments
4. **Feedback**: Post in GitHub Issues or PR comments (visible to student immediately)
5. **Revision allowed?** (Optional): For lower grades, allow resubmit with penalty

---

## PART 10: SAMPLE OUTCOMES MAPPING DOCUMENT

### Unit 1: Introduction to Kinematics & Coordinate Frames

**Unit Learning Outcomes (ULOs):**
- ULO1.1: Convert position, velocity, acceleration between Cartesian, polar, cylindrical, spherical frames
- ULO1.2: Interpret centripetal and tangential acceleration components in uniform circular motion
- ULO1.3: Distinguish between kinematics (motion description) and kinetics (causes of motion)

**Bloom Levels:**
- ULO1.1: Apply (students use formulas in new contexts)
- ULO1.2: Analyze (students relate components to physical phenomena)
- ULO1.3: Understand (students explain differences)

**Assessment Methods:**
- Quick Check (Hour 1): Compute centripetal acceleration for given circular motion (auto-graded)
- Challenge (Hour 2): Convert arbitrary 3D trajectory; verify equivalence (rubric-graded)
- Unit Lab (Summative): Design a spiral trajectory in cylindrical coords; code, visualize, explain (15 points)

**CO Mapping:**
- CO1 (Describe concepts) ← ULO1.1, ULO1.3
- Contributes to PSO3 (Math foundation) and PSO4 (Problem-solving)

---

## CONCLUSION

This framework integrates:
- **Evidence-based pedagogy** (constructivism, scaffolding, active learning, Bloom's taxonomy)
- **OBE methodology** (outcomes-driven, backward-designed, transparent assessment)
- **Modern engineering tools** (VS Code, GitHub, Python, Jupyter native)
- **Inclusive, low-barrier access** (single installation, free tools, academic license)
- **NBA/ABET alignment** (explicit mapping to program outcomes)

The result: **A coherent, engaging, rigorous course that students WANT to take and LEARN deeply from.**

---

## QUICK REFERENCE: Next Steps

1. **Review this document** with department chair and senior faculty
2. **Adjust outcomes** as needed per institutional requirements
3. **Create GitHub organization** (takes 10 minutes)
4. **Refactor Unit 1 notebook** to Explain-Try-Challenge (1-2 days)
5. **Test with alpha group** (3 students) 1 week before semester
6. **Launch** with confidence!

---

**Document Version:** 1.0  
**Last Updated:** December 2025  
**Author:** [Your Name]  
**Contact:** [Your Email]
