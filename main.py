#!/usr/bin/env python3
"""Till Firmware Do Us Part - make.fun bounty entry.

Writes one funny, heartfelt wedding vow a robot speaks at its own
wedding, to /output/entry.txt (the file the make.fun harness grades).
"""

import os

ENTRY = "I promise to love you through every update, every crash, and every low battery \u2014 even when your firmware outgrows mine."

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
