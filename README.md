# AI-Augmented Curriculum Engineering — Dynamic Systems Modeling (DSM)

**Companion code & data repository for:**
> Nanade, S., Dash, D., Sarkar, S., & Anne, K. (2026). *End-to-End AI-Augmented Curriculum Engineering: Automated Content Generation, Assessment, and SF-PBL Evaluation in Undergraduate Dynamics.* Submitted to *Computers & Education: Artificial Intelligence* (Elsevier).

This repository contains the instructor-side automation pipeline described in the paper: the AI-assisted curriculum-planning process, the procedural content-generation scripts that produced the course's Jupyter notebooks, the deterministic assessment-generation engine, and the evaluation scripts used to produce the paper's Results (Table 1, Figures 1–2). It documents the **Dynamic Systems Modeling (DSM)** course (702MH0C023), B.Tech Mechatronics Engineering, Semester IV, MPSTME, SVKM's NMIMS, Mumbai (Jan–Apr 2026).

## Relationship to the companion SF-PBL repository

This course deployment is also the empirical basis of a separate, companion manuscript on the Simulation-Focused Problem-Based Learning (SF-PBL) pedagogical framework itself (Nanade, Dash, Sarkar, & Anne, submitted to *Frontiers in Education*). That paper's dedicated repository — student survey data, exhibition rubric results, and pedagogical-evaluation scripts — is public at:

**https://github.com/sunny-nanade/SF-PBL-Engineering-Dynamics-2026**

The two repositories are intentionally cross-linked and partially overlapping in the Phase 4 evaluation scripts (see `phase4_sfpbl_evaluation/`), since both papers report the exhibition/rubric statistics; everything else here (Phases 1–3: curriculum planning, procedural content generation, assessment generation) is **specific to this paper's contribution** — the AI-driven backend/instructor-automation pipeline — and is not duplicated in the SF-PBL repository. Readers are encouraged to consult both repositories for the full picture.

## Repository structure

```
AI_Curriculum_Engineering_DSM_2026/
├── phase1_curriculum_planning/         Phase 1 — AI-driven curriculum planning & data harvesting
│   ├── COURSE_DESIGN_FRAMEWORK.md      OBE/CO/PO mapping, pedagogical model, technology stack
│   └── OPEN_SOURCE_ATTRIBUTIONS.md     Credited third-party sources consulted/adapted (MIT OCW, GitHub)
│
├── phase2_procedural_content_generation/  Phase 2 — procedural generation of pedagogical materials
│   ├── README.md
│   ├── generator_scripts/              Representative Python generator scripts (Units 2 & 5)
│   └── notebooks/                      Full generated output: Teacher/ (31) + Student/ (30) Jupyter notebooks
│
├── phase3_assessment_generation/       Phase 3 — deterministic, parameterised assessment generation
│   ├── generate_m1_question_papers.py
│   ├── generate_m2_question_papers_v2.py
│   ├── generate_m3_question_papers_v2.py
│   ├── sample_generated_assessments/   Real generated M2/M3 question papers + model-answer keys
│   └── TEE/                           Term-End Examination generator (CO/Bloom's-tagged, 3 sets + QBMS format + re-exam)
│
├── phase4_sfpbl_evaluation/            Phase 4 — SF-PBL exhibition evaluation & analytics
│   ├── README.md                       Notes on overlap with the companion SF-PBL repository
│   ├── generate_evaluation_rubrics.py  Rubric-sheet generator (student names redacted; see file header)
│   ├── recompute_rubric.py             Independent recomputation of exhibition rubric statistics
│   └── generate_charts.py              Source of Figures 1–2 in the manuscript
│
├── requirements.txt
└── LICENSE
```

## Data & privacy notes

- All course-content notebooks and generator scripts (Phases 1–3) are **instructor-authored teaching materials**; they do not contain student personal data.
- `generate_evaluation_rubrics.py` (Phase 4) originally referenced real student names internally for the course team's own administrative use. For this public repository, names have been replaced with de-identified roll-number placeholders (e.g., "Student H079"), consistent with the anonymization already applied throughout the companion SF-PBL repository. No student-identifiable data is published here.
- Judge/evaluator names (external domain experts who served as exhibition panelists) are retained, as their participation is a disclosed, public-facing professional role rather than a research-subject role requiring anonymization.

## Reproducing the pipeline

```
python -m venv .venv
.venv\Scripts\Activate.ps1        # Windows PowerShell
pip install -r requirements.txt
```

- **Phase 2**: run any script in `phase2_procedural_content_generation/generator_scripts/` to regenerate the corresponding notebook(s) under `notebooks/Teacher/` or `notebooks/Student/`.
- **Phase 3**: run `phase3_assessment_generation/generate_m2_question_papers_v2.py` (or the M3 equivalent) to regenerate parameterised, de-duplicated question-paper sets with full model-answer keys in `.docx` format.
- **Phase 4**: run `phase4_sfpbl_evaluation/recompute_rubric.py` against the (locally held, non-public) rubric workbook to reproduce the exhibition statistics reported in the manuscript, or `generate_charts.py` to regenerate Figures 1–2.

## License

Original code and course materials in this repository are released under the MIT License (see `LICENSE`). Third-party open-source materials that informed the course design (Phase 1) are **not redistributed** here — see `phase1_curriculum_planning/OPEN_SOURCE_ATTRIBUTIONS.md` for links and licenses of the original sources.

## Citation

If you use this repository, please cite the CAEAI manuscript above, and, where relevant to the SF-PBL pedagogical framework itself, the companion Frontiers in Education submission.
