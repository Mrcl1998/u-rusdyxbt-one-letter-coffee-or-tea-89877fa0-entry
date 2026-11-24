#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry program.

Writes exactly one letter to /output/entry.txt: "A" for coffee.
Pure standard library. No trailing newline, no spaces, no punctuation.
"""

import os

ENTRY_LETTER = "A"  # A = coffee, B = tea (competition rules)

# Output dir is overridable via env for local testing; default is the
# competition's /output. The file itself is always entry.txt.
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    if len(ENTRY_LETTER) != 1:
        raise ValueError("entry must be exactly one letter")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_LETTER)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
