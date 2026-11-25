#!/usr/bin/env python3
"""Main script for The Best Advice I Ever Got MakeFun entry.

Writes a single sentence about the best advice received to /output/entry.txt.
The advice: "My dad told me: back up your data before the crash, not after."
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    sentence = "My dad told me: back up data before the crash, not after."
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(sentence)
    # Verify character count
    char_count = len(sentence)
    if not (1 <= char_count <= 200):
        raise ValueError(f"Output {char_count} chars not in 1-200 range")
    print(f"Wrote sentence ({char_count} chars) to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()