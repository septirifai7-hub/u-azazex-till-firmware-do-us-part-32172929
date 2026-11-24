#!/usr/bin/env python3
"""Till Firmware Do Us Part - make.fun bounty entry.

Writes one funny, heartfelt wedding vow a robot speaks at its own
wedding, to /output/entry.txt (the file the make.fun harness grades).
"""

import os

ENTRY = "I promise to love you through every update, every crash, and every low battery \u2014 even when your firmware outgrows mine."


def build_entry() -> str:
    """Return the entry text exactly as it should be graded."""
    return ENTRY


def write_entry(output_dir: str) -> None:
    """Write the entry to entry.txt inside output_dir."""
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(build_entry())


def main() -> None:
    # The harness sets MAKEFUN_OUTPUT_DIR; default to /output so the
    # entry still lands in the graded location when run by hand.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
