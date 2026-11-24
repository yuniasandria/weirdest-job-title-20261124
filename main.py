# SPDX-License-Identifier: MIT
"""Weirdest Job Title entry.

Writes a single job title to /output/entry.txt: a real-sounding corporate
title with one hilariously specific twist, 32 characters, nothing else.
"""

import os

TITLE = "Chief Penguin Relocation Officer"


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
