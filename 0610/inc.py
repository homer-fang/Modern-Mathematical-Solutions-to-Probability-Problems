import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots(figsize=(14, 6))

ax.set_xlim(0, 16)
ax.set_ylim(0, 8)
ax.axis('off')

# =========================
# 1. Top row: current string
# =========================
top_bits = ['...', '1', '1', '0', '1', '1']
top_x = [1, 3, 4, 5, 6, 7]
top_y = 6

ax.text(0.8, 7.2, "Current string:", fontsize=16, fontweight='bold')

for x, bit in zip(top_x, top_bits):
    if bit == '...':
        ax.text(x, top_y, bit, fontsize=20, ha='center', va='center')
    else:
        rect = Rectangle(
            (x - 0.35, top_y - 0.35),
            0.7,
            0.7,
            fill=False,
            linewidth=1.5
        )
        ax.add_patch(rect)
        ax.text(x, top_y, bit, fontsize=18, ha='center', va='center')

ax.plot([6, 7], [5.35, 5.35], color='red', linewidth=3)
ax.text(6.5, 4.95, "suffix run of 1s", color='red', fontsize=14, ha='center')

ax.annotate(
    r"suffix length $L = 2$",
    xy=(7, 6),
    xytext=(9.0, 6.7),
    fontsize=14,
    color='blue',
    arrowprops=dict(arrowstyle='->', color='blue', lw=2)
)

# =========================
# 2. Bottom row: next bit succeeds
# =========================
bottom_bits = ['...', '1', '1', '0', '1', '1', '1']
bottom_x = [1, 3, 4, 5, 6, 7, 8]
bottom_y = 2.8

ax.text(0.8, 4.2, "Next bit succeeds:", fontsize=16, fontweight='bold')

for x, bit in zip(bottom_x, bottom_bits):
    if bit == '...':
        ax.text(x, bottom_y, bit, fontsize=20, ha='center', va='center')
    else:
        rect = Rectangle(
            (x - 0.35, bottom_y - 0.35),
            0.7,
            0.7,
            fill=False,
            linewidth=1.5
        )
        ax.add_patch(rect)
        ax.text(x, bottom_y, bit, fontsize=18, ha='center', va='center')

# Highlight the newly appended 1
highlight_rect = Rectangle(
    (8 - 0.35, bottom_y - 0.35),
    0.7,
    0.7,
    fill=False,
    linewidth=2.5,
    edgecolor='green'
)
ax.add_patch(highlight_rect)
ax.text(8, bottom_y, '1', fontsize=18, ha='center', va='center', color='green')

ax.plot([6, 8], [2.15, 2.15], color='red', linewidth=3)
ax.text(7, 1.7, "new suffix run of 1s", color='red', fontsize=14, ha='center')

ax.annotate(
    r"suffix length $L + 1 = 3$",
    xy=(8, bottom_y),
    xytext=(8.9, 3.25),
    fontsize=14,
    color='blue',
    arrowprops=dict(arrowstyle='->', color='blue', lw=2)
)

# =========================
# 3. Middle: transition label
# =========================
ax.annotate(
    "",
    xy=(8.0, 3.9),
    xytext=(8.0, 5.0),
    arrowprops=dict(arrowstyle='->', color='purple', lw=2)
)

ax.text(8.25, 4.35, r"bit $i$ succeeds", fontsize=14, color='purple', va='center')

# =========================
# 4. Right side: formulas
# =========================
formula_x = 11.3

# Vertical separator
ax.plot(
    [10.7, 10.7],
    [1.2, 6.7],
    color='gray',
    linestyle='--',
    linewidth=1,
    alpha=0.4
)

ax.text(formula_x, 5.8, "Old suffix contribution:", fontsize=14)
ax.text(formula_x + 0.2, 5.2, r"$L^3$", fontsize=18, color='darkred')

ax.text(formula_x, 4.2, "New suffix contribution:", fontsize=14)
ax.text(formula_x + 0.2, 3.6, r"$(L+1)^3$", fontsize=18, color='darkred')

ax.text(formula_x, 2.5, "Score increment:", fontsize=14, fontweight='bold')
ax.text(
    formula_x + 0.2,
    1.8,
    r"$(L+1)^3 - L^3 = 3L^2 + 3L + 1$",
    fontsize=18,
    color='darkgreen'
)

# =========================
# 5. Bottom summary
# =========================
summary_text = (
    r"Key point: we track the score increment, not $(L+1)^3$ directly."
    "\n"
    r"So we only need $E[L]$ and $E[L^2]$, not the third moment $E[L^3]$."
)

ax.text(
    1.0,
    0.5,
    summary_text,
    fontsize=14,
    color='black',
    bbox=dict(
        boxstyle='round,pad=0.4',
        edgecolor='gray',
        facecolor='#f5f5f5'
    )
)

plt.tight_layout()
plt.show()