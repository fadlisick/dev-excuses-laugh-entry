"""Emit one developer excuse for the make.fun judge.

The program does a single job: drop the excuse line into the file the
harness grades, ``entry.txt`` inside the output directory the harness
points at. No network, no arguments, no extra output.
"""

import os
from pathlib import Path

# The excuse itself: one line, spoken the way a developer would say it
# out loud after production broke.
EXCUSE_LINE = "It passed every test because I wrote the tests after the code, to match the code, like a horoscope."


def resolve_outfile() -> Path:
    """Return the path the graded text must land on."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(out_dir) / "entry.txt"


def emit() -> None:
    """Write the excuse, exactly as-is, to the graded file."""
    outfile = resolve_outfile()
    if not outfile.parent.exists():
        outfile.parent.mkdir(parents=True, exist_ok=True)
    outfile.write_text(EXCUSE_LINE, encoding="utf-8")


if __name__ == "__main__":
    emit()
