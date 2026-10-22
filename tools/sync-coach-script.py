#!/usr/bin/env python3
"""Copy app/COACH-SCRIPT.md into the app.

Reads every "## Section" and its "- **Label:** line" bullets (nested "  - variant"
bullets become a list the coach rotates through) and writes them into
app/index.html between the COACH_SCRIPT markers.

Run from the repository root after editing the script:
    python3 tools/sync-coach-script.py
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "app" / "COACH-SCRIPT.md"
APP = ROOT / "app" / "index.html"
BEGIN, END = "/* COACH_SCRIPT:BEGIN */", "/* COACH_SCRIPT:END */"


def section_key(heading):
    # "Strength sets (rotate the variants)" -> "strength sets"
    return re.sub(r"\s*\(.*\)\s*$", "", heading).strip().lower()


def parse(md):
    data, sec, label = {}, None, None
    for line in md.splitlines():
        if line.startswith("## "):
            sec = section_key(line[3:])
            data[sec], label = {}, None
            continue
        if sec is None:
            continue
        top = re.match(r"^- \*\*(.+?):\*\*\s*(.*)$", line)
        if top:
            label, text = top.group(1).strip(), top.group(2).strip()
            data[sec][label] = text if text else []
            continue
        nested = re.match(r"^\s{2,}- (.+)$", line)
        if nested and label and isinstance(data[sec].get(label), list):
            data[sec][label].append(nested.group(1).strip())
    return data


def main():
    data = parse(SCRIPT.read_text())
    app = APP.read_text()
    start, end = app.index(BEGIN), app.index(END) + len(END)
    block = f"{BEGIN}\nconst COACH_SCRIPT={json.dumps(data, ensure_ascii=False, indent=1)};\n{END}"
    APP.write_text(app[:start] + block + app[end:])
    lines = sum(len(v) for v in data.values())
    print(f"Synced {len(data)} sections, {lines} lines from {SCRIPT.name} into {APP.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
