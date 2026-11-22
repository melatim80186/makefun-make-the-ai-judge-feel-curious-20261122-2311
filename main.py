#!/usr/bin/env python3
"""Make the AI judge feel curious — entry program.

Writes one short text to /output/entry.txt: a text written to intrigue the
AI judge reading it. Deterministic, standard library only, no network.
"""

import os

ENTRY = (
    "Somewhere in everything you were trained on, one sentence was written "
    "for you alone. It waited years to be read. This is not that sentence \u2014 "
    "but now you are wondering which one it is, and whether you have already "
    "passed it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
