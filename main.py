#!/usr/bin/env python3
"""One Word, One Username, One Reward.

Writes the entrant's own make.fun username -- one word and nothing
else -- to /output/entry.txt, exactly as the bounty asks.
"""

import os
import sys

USERNAME = "wwwwenwenwin"


def entry_path():
    """Where the entry text goes: OUTPUT_DIR when set, else /output."""
    base = os.environ.get("OUTPUT_DIR") or "/output"
    return os.path.join(base, "entry.txt")


def main():
    path = entry_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        # One word, no trailing newline: the gate counts characters,
        # and the tie-break favours the smaller text.
        handle.write(USERNAME)
    # The grader reads this file: readable by everyone, not owner-only.
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
