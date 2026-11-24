#!/usr/bin/env python3
"""Entry for 'Make the AI Judge Laugh: Developer Excuses'.

Writes one funny single-line developer excuse to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Python 3 standard library only; deterministic output.
"""

import os

LINE = "The logs say prod is fine, so the bug must be the users."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
