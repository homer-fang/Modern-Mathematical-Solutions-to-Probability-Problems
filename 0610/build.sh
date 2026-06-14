#!/usr/bin/env bash
# Build 0610 assets: figures (PNG), Word (DOCX), and PDF from 0610.md
set -eu

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

MD="0610.md"
DOCX="0610.docx"
PDF="0610.pdf"
INC_IMAGE="inc_output.png"
STATE_IMAGE="state_dependency_graph.png"
CJK_FONT="${CJK_FONT:-AR PL UMing CN}"

need() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "Error: '$1' not found. Please install it first." >&2
    exit 1
  fi
}

need python3
need pandoc
need xelatex

if ! python3 -c "import matplotlib" 2>/dev/null; then
  echo "Installing matplotlib..."
  python3 -m pip install matplotlib -q
fi

echo "==> [1/4] Generating figure: $INC_IMAGE"
MPLBACKEND=Agg python3 << 'PY'
import matplotlib
matplotlib.use("Agg")
from pathlib import Path

code = Path("inc.py").read_text(encoding="utf-8")
code = code.replace(
    "plt.show()",
    "plt.savefig('inc_output.png', dpi=150, bbox_inches='tight'); print('Saved inc_output.png')",
)
exec(compile(code, "inc.py", "exec"), {"__name__": "__main__"})
PY

echo "==> [2/4] Generating figure: $STATE_IMAGE"
python3 state.py

echo "==> [3/4] Generating DOCX: $DOCX"
pandoc "$MD" -o "$DOCX"

echo "==> [4/4] Generating PDF: $PDF"
pandoc "$MD" -o "$PDF" \
  --pdf-engine=xelatex \
  -V "CJKmainfont=${CJK_FONT}"

echo ""
echo "All done:"
ls -lh "$INC_IMAGE" "$STATE_IMAGE" "$DOCX" "$PDF"
