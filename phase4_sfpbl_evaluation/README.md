# Phase 4 — SF-PBL Exhibition Evaluation & Analytics

This folder contains the scripts that directly produced the statistics and figures reported in this manuscript's Results and Discussion sections (Table 1, Figure 1 `chart1_domain_scores.png`, Figure 2 `chart2_survey_results.png`).

## Overlap disclosure

These three scripts are **intentionally also part of** the companion SF-PBL repository (https://github.com/sunny-nanade/SF-PBL-Engineering-Dynamics-2026), since both papers report outcomes from the same exhibition/evaluation event. They are included here as well, rather than only linked, so that this paper's specific figures and table are independently reproducible directly from this repository without requiring the reader to cross-reference the companion repository. All other repository content here (Phases 1–3) is exclusive to this paper.

## Scripts

- `generate_evaluation_rubrics.py` — Generates the six-judge, four-criteria-per-domain evaluation rubric workbook used at the exhibition (17 teams, 6 domains, 100 points total). **Student names have been redacted** in this copy and replaced with de-identified roll-number placeholders (e.g., `"Student H079"`); see the in-file note at the top of the `GROUPS` list. The original, name-bearing workbook is retained internally by the course team for administrative purposes only and is not published.
- `recompute_rubric.py` — Independently re-extracts and recomputes exhibition rubric statistics directly from the (locally held) Excel workbook, applying the corrected N=53 accounting (excluding the one registered-but-absent student) described in the manuscript.
- `generate_charts.py` — Generates the two chart images used as Figures 1–2 in the manuscript, from the verified summary statistics.

## Data availability

The underlying anonymized survey and rubric datasets (`DSM_Survey_Raw_PrePost.csv` and related files) are published in the companion SF-PBL repository rather than duplicated here, to maintain a single authoritative source for that shared dataset. See this manuscript's Data Availability statement for full details.
