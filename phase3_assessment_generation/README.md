# Phase 3 — Algorithmic Assessment Generation

This folder contains the deterministic assessment-generation engine described in Section 3.4 ("Phase 3") of the manuscript, including the Lagrangian-derivation-grounded Simple Pendulum generator discussed in detail in the paper (Listing 1).

## Scripts

- `generate_m2_question_papers_v2.py` — Generates 4 parameterised sets of the Mid-Semester II question paper (syllabus scope: Units 3–5) plus 4 full model-answer-key sets, as Word (`.docx`) documents. Each set uses distinct numerical parameters drawn from validated, dimensionally-consistent ranges, so that no two sets are identical while remaining equivalent in difficulty and syllabus coverage.
- `generate_m3_question_papers_v2.py` — Equivalent generator for the Mid-Semester III (re-examination) question papers.

Both scripts are self-contained (`python generate_m2_question_papers_v2.py`) and write their output to a local `question_papers_m2/` or `question_papers_m3/` folder; `sample_generated_assessments/` below shows the actual output already produced for this course offering.

## `sample_generated_assessments/`

Real, already-generated output from the two scripts above:

- `M2/` — 4 M2 question-paper sets + 4 model-answer-key sets (`.docx`), plus combined PDFs.
- `M3/` — 2 M3 re-examination question-paper sets + solutions (`.docx` and `.pdf`).

These are genuine assessment instruments used in the DSM course (Jan–Apr 2026 offering); no student responses or grades are included, only the instructor-facing question papers and model solutions.
