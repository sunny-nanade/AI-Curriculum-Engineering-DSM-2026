# DSM Course Outcomes × Bloom's Taxonomy Mapping

DSM-only extract from the shared, multi-course `CO_BLOOMS_MAPPING.md` reference used by the TEE generation tool (which also covers two other, unrelated courses not included in this repository).

## DSM — Dynamic Systems Modeling (702MH0C023)

### Course Outcomes and Bloom's Levels (as encoded in the TEE generation engine)

| CO | Description | Primary Verb | Bloom's Level | Question Types |
|----|-------------|--------------|---------------|-----------------|
| CO1 | Understand and apply theoretical concepts in kinematics | Understand, Apply | L2, L3 | Define, explain, apply formulas |
| CO2 | Analyze the given system using the Free Body Diagram | Analyze | L4 | Draw FBD, solve problems |
| CO3 | Understand and calculate the forces acting on dynamic systems | Understand, Calculate | L2, L3 | Explain forces, solve numericals |
| CO4 | Apply the constitutive laws to analyze the dynamic systems of particles and rigid bodies | Apply, Analyze | L3, L4 | Apply laws, analyze systems |
| CO5 | Understand and calculate the energy of a dynamic system and power dissipated | Understand, Calculate | L2, L3 | Energy calculations, power analysis |

### Unit-wise CO Mapping

- Unit 1 (Introduction): CO1
- Unit 2 (Constitutive Laws): CO3, CO4
- Unit 3 (Rigid Body Kinematics): CO1, CO2
- Unit 4 (Particle Kinetics): CO2, CO3, CO4
- Unit 5 (Rigid Body Kinetics): CO2, CO4
- Unit 6 (Work and Energy): CO4, CO5
- Unit 7 (Advanced Topics): CO4, CO5

## Note on CO wording across companion documents

Readers cross-referencing this repository with the companion Frontiers in Education manuscript's OBE table will notice that manuscript uses a differently-worded (though topically consistent, CO1→kinematics, CO2→FBD, CO3→Newton's laws) five-CO set with Bloom's levels L3–L6, refined specifically for that paper's OBE-alignment analysis. The wording above is the syllabus-derived version encoded directly in this TEE generation engine and is preserved verbatim here for reproducibility of the exact question-level CO/Bloom's tagging shown in `generators/create_dsm_final_sets.py`. Both are accurate descriptions of the same underlying course; the difference is one of editorial refinement between an internal engineering tool and a polished manuscript table, not a factual conflict.
