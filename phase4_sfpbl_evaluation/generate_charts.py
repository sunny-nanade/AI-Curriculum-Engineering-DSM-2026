"""
Generate charts for the RRSPBL/JEET Research Paper on SF-PBL.
All values are independently recomputed from the ground-truth source data
(Evaluation_Rubric_Sheets.xlsx via recompute_rubric.py; DSM_Survey_Raw_PrePost.csv),
excluding the one student absent for the entire exhibition day (N=53, consistent
with the consenting survey cohort used throughout the paper).
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

OUT = os.path.dirname(os.path.abspath(__file__)) + "/"

# ─── CHART 1: Domain Performance Bar Chart ──────────────────────────────────
domains = ['Manufacturing', 'Industrial\nAutomation', 'Communication', 'HR & Behavioural\nScience', 'Mathematics', 'IP &\nInnovation']
means   = [13.94, 17.09, 13.26, 13.02, 12.77, 12.53]
maxes   = [16,    20,    16,    16,    16,    16]
sds     = [1.23,  2.18,  2.13,  2.28,  2.67,  2.68]
pcts    = [m/mx*100 for m, mx in zip(means, maxes)]

fig, ax = plt.subplots(figsize=(8, 4.5))
colors = ['#2ecc71' if p >= 85 else '#f39c12' if p >= 79 else '#e74c3c' for p in pcts]
bars = ax.bar(domains, pcts, color=colors, edgecolor='black', linewidth=0.5, width=0.6)
yerrs = [s/mx*100 for s, mx in zip(sds, maxes)]
ax.errorbar(domains, pcts, yerr=yerrs,
            fmt='none', color='black', capsize=4, linewidth=1.5, capthick=1.5)

ax.set_ylabel('Score as % of Maximum', fontsize=11)
ax.set_title('Fig. 1: Expert Panel Domain Scores — 17 Teams (N=53 students)', fontsize=11, fontweight='bold')
ax.set_ylim(50, 105)
ax.axhline(y=np.mean(pcts), color='navy', linestyle='--', linewidth=1, label=f'Overall Mean = {np.mean(pcts):.1f}%')
ax.legend(fontsize=9)
ax.tick_params(axis='x', labelsize=9)
ax.tick_params(axis='y', labelsize=9)
ax.set_ylabel('Score (% of Domain Maximum)', fontsize=10)

for bar, pct, mean, mx, yerr in zip(bars, pcts, means, maxes, yerrs):
    ax.text(bar.get_x() + bar.get_width()/2., pct + yerr + 1.0,
            f'{mean:.1f}/{mx}\n({pct:.1f}%)', ha='center', va='bottom', fontsize=7.5, fontweight='bold',
            bbox=dict(facecolor='white', alpha=0.75, edgecolor='none', pad=1))

legend_patches = [
    mpatches.Patch(color='#2ecc71', label='≥85% (Strong)'),
    mpatches.Patch(color='#f39c12', label='79–84% (Moderate)'),
    mpatches.Patch(color='#e74c3c', label='<79% (Needs development)')
]
ax.legend(handles=legend_patches + [plt.Line2D([0],[0], color='navy', linestyle='--', label=f'Overall Mean = {np.mean(pcts):.1f}%')], fontsize=8, loc='lower right')

plt.tight_layout()
plt.savefig(OUT + 'chart1_domain_scores.png', dpi=150, bbox_inches='tight')
print("Chart 1 saved.")
plt.close()


# ─── CHART 2: Pre/Post Survey (Knowledge Gain + Self-Efficacy) ─────────────
fig, axes = plt.subplots(1, 2, figsize=(8, 3.8))

# Left: Knowledge Gain
categories = ['Pre-Test', 'Post-Test']
scores = [1.96, 3.28]
colors_kg = ['#95a5a6', '#2980b9']
bars2 = axes[0].bar(categories, scores, color=colors_kg, edgecolor='black', linewidth=0.5, width=0.4)
axes[0].set_ylim(0, 5)
axes[0].set_ylabel('Mean Score (out of 5)', fontsize=10)
axes[0].set_title('Knowledge Gain (MCQ)\nN=53 Students', fontsize=10, fontweight='bold')
for bar, score in zip(bars2, scores):
    axes[0].text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.05,
                f'{score:.2f}', ha='center', va='bottom', fontsize=10, fontweight='bold')
axes[0].annotate('', xy=(1, 3.28), xytext=(0, 1.96),
                arrowprops=dict(arrowstyle='->', color='green', lw=2))
axes[0].text(0.5, 2.6, 'g = 0.43\n(Medium Gain)', ha='center', fontsize=9, color='green', fontweight='bold')

# Right: Self-Efficacy
categories_se = ['Pre-Exhibition', 'Post-Exhibition']
scores_se = [2.92, 3.80]
colors_se = ['#95a5a6', '#27ae60']
bars3 = axes[1].bar(categories_se, scores_se, color=colors_se, edgecolor='black', linewidth=0.5, width=0.4)
axes[1].set_ylim(0, 5)
axes[1].set_ylabel('Mean Score (1–5 scale)', fontsize=10)
axes[1].set_title('Self-Efficacy Score\nN=53 Students', fontsize=10, fontweight='bold')
for bar, score in zip(bars3, scores_se):
    axes[1].text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.05,
                f'{score:.2f}', ha='center', va='bottom', fontsize=10, fontweight='bold')
axes[1].annotate('', xy=(1, 3.80), xytext=(0, 2.92),
                arrowprops=dict(arrowstyle='->', color='green', lw=2))
axes[1].text(0.5, 3.35, '+30%', ha='center', fontsize=9, color='green', fontweight='bold')

fig.suptitle('Fig. 2: Pre/Post Survey Results — Student Knowledge Gain & Self-Efficacy', fontsize=10, fontweight='bold')
plt.tight_layout()
plt.savefig(OUT + 'chart2_survey_results.png', dpi=150, bbox_inches='tight')
print("Chart 2 saved.")
plt.close()


# ─── CHART 3: Team Score Distribution ────────────────────────────────────────
team_scores = [82.3, 81.3, 84.3, 60.5, 89.5, 54.0, 83.3, 90.0, 88.2, 85.0, 85.0, 75.3, 90.8, 85.5, 90.2, 87.7, 80.0]
team_labels = [f'G{i:02d}' for i in range(1, 18)]

fig, ax = plt.subplots(figsize=(9, 3.8))
colors_t = ['#e74c3c' if s < 70 else '#f39c12' if s < 82 else '#27ae60' for s in team_scores]
bars4 = ax.bar(team_labels, team_scores, color=colors_t, edgecolor='black', linewidth=0.5, width=0.7)
ax.axhline(y=np.mean(team_scores), color='navy', linestyle='--', linewidth=1.5, label=f'Mean = {np.mean(team_scores):.1f}')
ax.set_ylim(40, 100)
ax.set_ylabel('Total Score (/100)', fontsize=10)
ax.set_title('Fig. 3: Total Expert Panel Scores by Team — 17 Teams', fontsize=10, fontweight='bold')
ax.legend(fontsize=9)
ax.tick_params(axis='x', labelsize=8)
for bar, score in zip(bars4, team_scores):
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.3,
            f'{score}', ha='center', va='bottom', fontsize=7, fontweight='bold')

legend_patches = [
    mpatches.Patch(color='#e74c3c', label='<70 (Low)'),
    mpatches.Patch(color='#f39c12', label='70–81 (Moderate)'),
    mpatches.Patch(color='#27ae60', label='≥82 (High)')
]
ax.legend(handles=legend_patches + [plt.Line2D([0],[0], color='navy', linestyle='--', label=f'Mean = {np.mean(team_scores):.1f}')], fontsize=8)

plt.tight_layout()
plt.savefig(OUT + 'chart3_team_scores.png', dpi=150, bbox_inches='tight')
print("Chart 3 saved.")
plt.close()

print("All charts generated successfully.")
