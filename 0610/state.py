import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

OUTPUT = "state_dependency_graph.png"

fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(0, 16)
ax.set_ylim(0, 10)
ax.axis("off")

# -------------------------
# Helper functions
# -------------------------
def draw_node(x, y, text, radius=0.75, fc="#eef4ff", ec="#1f4e79",
              textsize=14, weight="normal"):
    circle = Circle((x, y), radius=radius, facecolor=fc, edgecolor=ec, linewidth=2)
    ax.add_patch(circle)
    ax.text(x, y, text, ha="center", va="center", fontsize=textsize, fontweight=weight)

def draw_arrow(x1, y1, x2, y2, text=None, text_offset=(0, 0),
               color="black", lw=1.8, style="-|>", rad=0.0, textsize=12):
    arrow = FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle=style,
        mutation_scale=15,
        linewidth=lw,
        color=color,
        connectionstyle=f"arc3,rad={rad}"
    )
    ax.add_patch(arrow)
    if text is not None:
        mx = (x1 + x2) / 2 + text_offset[0]
        my = (y1 + y2) / 2 + text_offset[1]
        ax.text(mx, my, text, fontsize=textsize, color=color,
                ha="center", va="center")

# -------------------------
# Title
# -------------------------
ax.text(
    8, 9.4,
    "Recurrence State Dependency Graph",
    ha="center", va="center",
    fontsize=22, fontweight="bold"
)

# -------------------------
# Column labels
# -------------------------
ax.text(3, 8.4, "Step i - 1", fontsize=18, fontweight="bold", ha="center", color="#1f4e79")
ax.text(8, 8.4, "Input", fontsize=18, fontweight="bold", ha="center", color="#7a3db8")
ax.text(13, 8.4, "Step i", fontsize=18, fontweight="bold", ha="center", color="#2e7d32")

# -------------------------
# Left side nodes: step i-1
# -------------------------
draw_node(3, 6.8, "E1[i-1]", fc="#eaf2fb", ec="#1f4e79", weight="bold")
draw_node(3, 5.0, "E2[i-1]", fc="#eaf2fb", ec="#1f4e79", weight="bold")
draw_node(3, 3.2, "ans[i-1]", fc="#eaf2fb", ec="#1f4e79", weight="bold")

# meanings
ax.text(1.2, 6.8, r"$= E[L_{i-1}]$", fontsize=14, color="#1f4e79", ha="left", va="center")
ax.text(1.0, 5.0, r"$= E[L_{i-1}^2]$", fontsize=14, color="#1f4e79", ha="left", va="center")
ax.text(0.95, 3.2, r"$= E[S_{i-1}]$", fontsize=14, color="#1f4e79", ha="left", va="center")

# -------------------------
# Middle input node
# -------------------------
draw_node(8, 5.0, "p_i", radius=0.7, fc="#f3e8ff", ec="#7a3db8", textsize=16, weight="bold")

# -------------------------
# Right side nodes: step i
# -------------------------
draw_node(13, 6.8, "E1[i]", fc="#edf7ed", ec="#2e7d32", weight="bold")
draw_node(13, 5.0, "E2[i]", fc="#edf7ed", ec="#2e7d32", weight="bold")
draw_node(13, 3.2, "ans[i]", fc="#edf7ed", ec="#2e7d32", weight="bold")

# -------------------------
# Dependency arrows
# -------------------------

# E1[i] depends on E1[i-1] and p_i
draw_arrow(3.8, 6.8, 12.2, 6.8, text=r"$E1[i] = p_i(E1[i-1] + 1)$",
           text_offset=(0, 0.45), color="#2e7d32", lw=2.0, textsize=12)
draw_arrow(8.55, 5.55, 12.55, 6.25, color="#7a3db8", lw=1.8, rad=0.08)

# E2[i] depends on E2[i-1], E1[i-1], and p_i
draw_arrow(3.8, 5.0, 12.2, 5.0, text=r"$E2[i] = p_i(E2[i-1] + 2E1[i-1] + 1)$",
           text_offset=(0, 0.45), color="#2e7d32", lw=2.0, textsize=12)
draw_arrow(3.75, 6.45, 12.25, 5.35, color="#2e7d32", lw=1.5, rad=-0.05)
draw_arrow(8.7, 5.0, 12.25, 5.0, color="#7a3db8", lw=1.8)

# ans[i] depends on ans[i-1], E1[i-1], E2[i-1], and p_i
draw_arrow(3.8, 3.2, 12.2, 3.2, text=r"$ans[i] = ans[i-1] + p_i(3E2[i-1] + 3E1[i-1] + 1)$",
           text_offset=(0, -0.52), color="#2e7d32", lw=2.0, textsize=11)
draw_arrow(3.75, 6.35, 12.25, 3.65, color="#2e7d32", lw=1.4, rad=-0.08)
draw_arrow(3.75, 4.85, 12.25, 3.45, color="#2e7d32", lw=1.4, rad=-0.04)
draw_arrow(8.55, 4.45, 12.55, 3.75, color="#7a3db8", lw=1.8, rad=-0.06)

# -------------------------
# Legend / explanation
# -------------------------
ax.text(
    8, 1.2,
    "Directed edges indicate dependency: each state at step i is computed only from step i - 1 and the current input p_i.",
    fontsize=13.5,
    ha="center",
    va="center",
    bbox=dict(boxstyle="round,pad=0.4", facecolor="#f7f7f7", edgecolor="gray")
)

# -------------------------
# Save figure
# -------------------------
plt.tight_layout()
plt.savefig(OUTPUT, dpi=180, bbox_inches="tight")
print(f"Saved: {OUTPUT}")