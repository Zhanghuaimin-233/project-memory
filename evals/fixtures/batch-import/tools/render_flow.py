"""Render the fixture's editable three-step source without external packages."""
import html
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
data = json.loads((root / "docs/flow.json").read_text(encoding="utf-8"))
if len(data["steps"]) != 3:
    raise ValueError("This fixture renderer expects three steps")
parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="920" height="200" viewBox="0 0 920 200">',
         '<rect width="920" height="200" fill="#f5f5f0"/>',
         '<g font-family="sans-serif" fill="#183028">',
         f'<text x="30" y="35" font-size="23">{html.escape(data["title"])}</text>']
for index, label in enumerate(data["steps"]):
    x = 30 + 310 * index
    parts.append(f'<rect x="{x}" y="70" width="240" height="70" rx="8" fill="#d8e7dc"/>')
    parts.append(f'<text x="{x + 120}" y="113" text-anchor="middle" font-size="18">{html.escape(label)}</text>')
    if index < 2:
        parts.append(f'<text x="{x + 285}" y="113" text-anchor="middle" font-size="25">→</text>')
parts.append('</g></svg>')
(root / "docs/flow.svg").write_text('\n'.join(parts) + '\n', encoding="utf-8")
