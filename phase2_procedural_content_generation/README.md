# Phase 2 — Procedural Content Generation (PCG)

This folder contains the procedural-content-generation pipeline described in Section 3.3 ("Phase 2") of the manuscript.

## `generator_scripts/`

Nine representative Python generator scripts, shown as worked examples of the PCG pipeline:

- `generate_u2_l1.py`, `generate_u2_l2.py`, `generate_u2_p1.py` — Unit 2 (Newton's Laws & **Lagrangian Mechanics**), directly parallel to the Lagrangian derivation presented in the manuscript's Methodology section.
- `create_u5_l1.py` – `create_u5_l5.py`, `create_u5_p1.py` — Unit 5 (Rigid-Body Equations of Motion, Coupled Systems, Multi-DOF Systems, Single/Multi-DOF Vibrations, Modal Testing Practical).

Each script deterministically assembles a Jupyter notebook (markdown + code cells) following the course's Explain–Try–Challenge (E-T-C) structure, embedding SymPy symbolic derivations, Matplotlib visualizations, and parameterized numerical examples. Running a script regenerates its corresponding notebook(s) in `notebooks/Teacher/` and, via a paired student-facing script, `notebooks/Student/`.

The remaining unit generators (Units 1, 3, 4, 6, 7) follow the same pattern and are available from the corresponding author on request; they are omitted here for repository conciseness rather than to overstate reproducibility — the nine scripts included are sufficient to demonstrate and independently verify the generation methodology end-to-end.

## `notebooks/`

The full set of **generated output notebooks** — the actual PCG deliverables referenced in the manuscript ("30+ specialized notebooks"):

- `Teacher/` — 31 instructor-facing notebooks (Units 1–7: Lectures, Practicals, and one Assessment notebook), including full worked solutions and answer keys.
- `Student/` — 30 student-facing notebooks (same units/lectures/practicals, scaffolded per the Explain–Try–Challenge model, without answer keys).

Note: `T_U3_P1_Rotating_Frames_Practical.ipynb` is unusually large (~34 MB) because it contains embedded animation-frame output; this is genuine generated output, not a data-integrity issue.
