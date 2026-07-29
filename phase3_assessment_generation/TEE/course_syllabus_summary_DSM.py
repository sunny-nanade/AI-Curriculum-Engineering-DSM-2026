"""
DSM Course Information — Term-End Examination (TEE) Generator
================================================================
Dynamic Systems Modeling, B.Tech Mechatronics Engineering, Semester IV
SVKM's NMIMS, MPSTME, Mumbai

This is a DSM-only extract of the shared, multi-course `course_syllabus_summary.py`
engine used by the TEE generation tool (which also supports two other, unrelated
courses not included in this repository). Only the DSM entry is reproduced here.

NOTE ON COURSE CODE: the original multi-course file recorded this course's code as
"702MH0C025". Cross-checked against 42 independent occurrences elsewhere in the DSM
course-development archive and against the companion Frontiers-in-Education
manuscript (which consistently cites "702MH0C023"), "702MH0C025" appears to be an
isolated typo in that one auxiliary tool. The correct code, 702MH0C023, is used below.
"""

DSM_INFO = {
    "course_code": "702MH0C023",
    "course_name": "Dynamic Systems Modeling",
    "semester": "IV",
    "credits": 3,
    "course_outcomes": [
        "CO1: Understand and apply theoretical concepts in kinematics",
        "CO2: Analyze the given system using the Free Body Diagram",
        "CO3: Understand and calculate the forces acting on dynamic systems",
        "CO4: Apply the constitutive laws to analyze the dynamic systems of particles and rigid bodies",
        "CO5: Understand and calculate the energy of a dynamic system and power dissipated",
    ],
    "units": [
        {"unit": 1, "title": "Introduction",
         "topics": "Review of elementary dynamics, kinematics and kinetics, particles and rigid bodies, motion, position, velocity acceleration in Cartesian, Polar, Cylindrical and Spherical coordinate frames",
         "duration": 3},
        {"unit": 2, "title": "Constitutive Laws",
         "topics": "Force and Energy based formulations, Newton's Laws, introduction to Lagrange's Equations using Hamilton's Principle, illustrative examples",
         "duration": 4},
        {"unit": 3, "title": "Rigid Body Kinematics",
         "topics": "Degrees of Freedom, position, velocity and acceleration in Fixed, Rotating and Moving Reference Frames",
         "duration": 5},
        {"unit": 4, "title": "Particle Kinetics",
         "topics": "Pulleys and mechanical advantage, 3D printer head motion analysis",
         "duration": 4},
        {"unit": 5, "title": "Rigid Body Kinetics",
         "topics": "Equations of motion of general one and two degree of freedom dynamic systems using Newton's Laws, Rotating and Moving Coordinate Frames",
         "duration": 6},
        {"unit": 6, "title": "Work and Energy",
         "topics": "Work-Energy Principle, kinetic and potential energy of dynamic systems, power dissipated, infinitesimal work done by non-conservative forces",
         "duration": 4},
        {"unit": 7, "title": "Introduction to Advanced Topics",
         "topics": "Numerical simulations using ODE editors of computational software platforms",
         "duration": 4},
    ],
}
