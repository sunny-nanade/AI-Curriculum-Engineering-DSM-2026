# Term-End Examination (TEE) Generation — DSM

This folder extends `phase3_assessment_generation/` with the **Term-End Examination** (the course's summative final exam, 100 marks evaluated out of a 140-mark paper), complementing the M1/M2 mid-semester generators in the parent folder. It was added from a separate internal tool (originally built to serve three courses; only the DSM-relevant parts are included here, per repository scope).

## Contents

- **`engine/`** — the shared, course-agnostic generation framework: `qp_generator.py` (core `QuestionPaper` class, structural validation), `create_qp_templates.py`, `blooms_taxonomy_verbs.py` (Bloom's Taxonomy L1–L6 reference and verb-matching).
- **`course_syllabus_summary_DSM.py`** — DSM-only course/syllabus data (course code corrected to 702MH0C023; see in-file note).
- **`DSM_CO_BLOOMS_MAPPING.md`** — DSM-only Course Outcome × Bloom's-level mapping.
- **`generators/`** — real, working generator scripts:
  - `generate_question_papers.py` — **M1** generator (10 marks, 45 min).
  - `create_dsm_exam_docs.py`, `create_dsm_final_sets.py` — **TEE** generator (140-mark paper, 100 evaluated; Q1 compulsory 4×5 marks + Q2–Q7 six 20-mark questions, solve any 4). Each question is tagged with Unit, Course Outcome, Bloom's level, difficulty, and question type in an explicit synoptic table (`MASTER_ROWS` in `create_dsm_final_sets.py`), then rendered into three parallel, non-identical sets.
  - `create_dsm_answer_booklets.py` — full worked-solution generator for the TEE sets.
  - `create_dsm_reexam_sets.py`, `create_dsm_reexam_answers.py` — Re-Examination generator for students who were absent from the Term-End Examination for medical reasons only (not a general repeat/failure retest).
- **`generated_papers/`** — real generated output:
  - `TEE_Final/` — the 3 final TEE question-paper sets + 3 model-answer sets + student answer-sheet template + topic-mapping reference.
  - `TEE_QBMS_Submission_Format/` — the same TEE content reformatted into the institution's official Question Bank Management System (QBMS) submission format (Sets A/B/C, each with a question paper and a synoptic/CO-Bloom's mapping table), as actually submitted for institutional records.
  - `TEE_ReExam/` — the 2 re-examination sets + answers, plus draft/header-format working files.
- **`DSM_syllabus_extracted.txt`** — plain-text extraction of the official DSM syllabus (source: the institution's own AY 2025–26 Semester IV syllabus document), used to seed the CO/unit data above.

## Relevance to the manuscript

Every question in the Term-End Examination is tagged with its Course Outcome and Bloom's-taxonomy level before the paper is assembled (see `MASTER_ROWS` in `create_dsm_final_sets.py`), and three non-identical, difficulty-matched sets are generated from the same tagged question bank. This supports the manuscript's Phase 3 description of assessment generation across the full assessment cycle (M1, M2, and the Term-End Examination), not only the mid-semester tests.

## Data privacy

All files in this folder are institutional question papers, model-answer keys, and syllabus/CO reference documents. None contain student names, roll numbers, or individual results.
