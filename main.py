#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry program.

Writes exactly one letter to /output/entry.txt: "A" for coffee.
Pure standard library. No trailing newline, no spaces, no punctuation.
"""

import os

ENTRY_LETTER = "A"  # A = coffee, B = tea (competition rules)

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_LETTER)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
