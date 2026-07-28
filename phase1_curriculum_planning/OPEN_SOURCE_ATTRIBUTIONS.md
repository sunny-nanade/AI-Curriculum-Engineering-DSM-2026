# Open-Source Attributions — Phase 1 (Curriculum Planning & Data Harvesting)

During Phase 1 (AI-driven curriculum planning), the course team consulted and, where explicitly noted, adapted **pedagogical structure and code patterns** (not verbatim source files) from the following openly available materials. None of the third-party repositories listed below are redistributed in this repository; only this attribution list and the course team's own, independently authored materials (Phases 1–3 folders) are published here. Links and license terms were verified directly against each source's own `git remote` and license file at the time of writing.

| # | Source | URL | License | How it informed the DSM course |
|---|--------|-----|---------|----------------------------------|
| 1 | MIT 2.003SC Engineering Dynamics (OpenCourseWare) | https://ocw.mit.edu/courses/2-003sc-engineering-dynamics-fall-2011/ | CC BY-NC-SA 4.0 | Lecture sequencing, problem-set difficulty calibration, and topic ordering (Units 1–7) benchmarked against this OCW course. |
| 2 | `RussTedrake/underactuated` (MIT 6.832, Russ Tedrake) | https://github.com/RussTedrake/underactuated | MIT License | Pedagogical flow (model → analyze → control) and selected worked-example framing for pendulum/cart-pole systems; adapted conceptually, not copied verbatim (Drake-based code was not reused; DSM notebooks use SymPy/SciPy). |
| 3 | `adamheins/lagrangian-mechanics-3-ways` | https://github.com/adamheins/lagrangian-mechanics-3-ways | Not specified by author — adaptation only | Inspired the "manual vs. symbolic derivation" side-by-side pattern used in Unit 2 notebooks; SymPy `LagrangesMethod` workflow adapted for DSM's own coordinate systems and problems. |
| 4 | `chris-greening/double-pendula` | https://github.com/chris-greening/double-pendula | Not specified by author — adaptation only | Informed the `matplotlib.animation.FuncAnimation` pattern used for DSM's own pendulum/rigid-body animations. |
| 5 | `Saptak625/DoublePendulum` | https://github.com/Saptak625/DoublePendulum | Not specified by author — adaptation only | Reference for 3D visualization concepts and multi-coordinate-system framing considered for advanced/optional material. |
| 6 | `iamAkshayrao/LQR-BalanceBot` | https://github.com/iamAkshayrao/LQR-BalanceBot | Not specified by author — adaptation only | Reference for the simulate-validate-hardware workflow considered for capstone/Unit 7 control content. |
| 7 | `AunSiro/optibot` | https://github.com/AunSiro/optibot | Not specified by author — adaptation only | Reference for SymPy + CasADi symbolic-to-numeric optimization workflow considered for optional advanced trajectory-optimization material. |
| 8 | `moorepants/resonance` (Jason K. Moore & Kenneth Lyons) | https://github.com/moorepants/resonance | MIT License | Reference for vibrations/resonance simulation utilities considered for Unit 5 (modal analysis) content. |
| 9 | `mugalan/classical-mechanics-from-a-geometric-point-of-view` (D. H. S. Maithripala, University of Peradeniya) | https://github.com/mugalan/classical-mechanics-from-a-geometric-point-of-view | See source repo | Reference for rigid-body simulation utilities (quaternion/rotation helpers) considered for Unit 5 content. |

## Note on licensing diligence

Where a source's license was **not explicitly specified** by its author (rows 3–7), the course team treated it as "look, learn, and re-implement independently" reference material rather than code to redistribute or copy verbatim — consistent with standard academic fair-use practice for pedagogical benchmarking. No files from any external repository are included in this public repository; all Python scripts and notebooks under `phase2_procedural_content_generation/` and `phase3_assessment_generation/` are original works authored by the course team for the DSM course.

## Full internal catalog

A more detailed internal catalog of these and other candidate sources (evaluated but not all adopted) is maintained in the course team's working notes (`RESEARCH_GOLDMINE.md`) and is available from the corresponding author on request.
