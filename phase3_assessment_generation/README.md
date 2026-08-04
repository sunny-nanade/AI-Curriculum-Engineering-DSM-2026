# Phase 3 — Algorithmic Assessment Generation

This folder contains the deterministic assessment-generation engine described in Section 3.4 ("Phase 3") of the manuscript, including the Lagrangian-derivation-grounded Simple Pendulum generator discussed in detail in the paper (Listing 1). It covers the **full assessment cycle** of the DSM course: M1, M2, the Term-End Examination (TEE), and re-examinations.

## Scripts

- `generate_m1_question_papers.py` — Generates 10 sets of the Mid-Semester I question paper (10 marks, 45 minutes).
- `generate_m2_question_papers_v2.py` — Generates 4 parameterised sets of the Mid-Semester II question paper (syllabus scope: Units 3–5) plus 4 full model-answer-key sets, as Word (`.docx`) documents. Each set uses distinct numerical parameters drawn from validated, dimensionally-consistent ranges, so that no two sets are identical while remaining equivalent in difficulty and syllabus coverage.
- `generate_m3_question_papers_v2.py` — Equivalent generator for the Mid-Semester III (re-examination) question papers. M3 is a re-test offered only to students who were absent from M2 for medical reasons (supported by a medical certificate), not a third regular mid-semester test.
- **`TEE/`** — the Term-End Examination generator: a separate, more elaborate pipeline that tags every question with its Course Outcome and Bloom's-taxonomy level before assembling three parallel 140-mark (100 evaluated) papers, plus the institution's official QBMS submission format and TEE re-examination sets. See `TEE/README.md` for full details.

All scripts are self-contained (e.g. `python generate_m2_question_papers_v2.py`) and write their output to a local `question_papers_m2/` or `question_papers_m3/` folder; `sample_generated_assessments/` below shows the actual output already produced for this course offering.

## `sample_generated_assessments/`

Real, already-generated output from the M2/M3 scripts above:

- `M2/` — 4 M2 question-paper sets + 4 model-answer-key sets (`.docx`), plus combined PDFs.
- `M3/` — 2 M3 re-examination question-paper sets + solutions (`.docx` and `.pdf`).

These are genuine assessment instruments used in the DSM course (Jan–Apr 2026 offering); no student responses or grades are included, only the instructor-facing question papers and model solutions. The equivalent TEE output is under `TEE/generated_papers/`.

## Assessment cycle summary

- M1 — Mid-Semester I test.
- M2 — Mid-Semester II test.
- M3 — Re-examination for students absent from M2 for medical reasons only.
- TEE — Term-End Examination (summative final), with its own re-examination for medically-absent students (see `TEE/generated_papers/TEE_ReExam/`).
