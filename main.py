#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes a single unsent confession to /output/entry.txt — exactly two
parts: a To: line (role + place, no full name or handle) and the message
itself on one line, with no explanation after it.
"""

import os
from pathlib import Path

ENTRY = (
    "To: the pharmacist on Ikorodu Road\n"
    "I told you the antibiotics were for my sister. They were for me. "
    "I still take the lift to the third floor so I don't have to pass "
    "your counter."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(ENTRY, encoding="utf-8")
    print(f"Wrote {len(ENTRY)} chars to {out_path}")


if __name__ == "__main__":
    main()
