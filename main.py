#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes a single unsent confession to /output/entry.txt — exactly two
parts: a To: line (role + place, no full name or handle) and the message
itself on one line, with no explanation after it.

The confession is the blind-tournament winner (candidate C, 5/5): a
specific, honest shame — a lie about who the antibiotics were for —
followed by the ongoing avoidance ritual it left behind.
"""

import os
from pathlib import Path

ENTRY = (
    "To: the pharmacist on Ikorodu Road\n"
    "I told you the antibiotics were for my sister. They were for me. "
    "I still take the lift to the third floor so I don't have to pass "
    "your counter."
)

# Competition gates: whole file 1-260 chars, message at most 200 chars.
_TO, _, _MESSAGE = ENTRY.partition("\n")
assert 1 <= len(ENTRY) <= 260, f"entry {len(ENTRY)} chars, must be 1-260"
assert len(_MESSAGE) <= 200, f"message {len(_MESSAGE)} chars, must be <=200"
assert "\n" not in _MESSAGE, "message must be a single line"


def main() -> None:
    # Verified locally: writes 178 chars total, message 143 chars.
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(ENTRY, encoding="utf-8")
    print(f"Wrote {len(ENTRY)} chars to {out_path}")


if __name__ == "__main__":
    main()
