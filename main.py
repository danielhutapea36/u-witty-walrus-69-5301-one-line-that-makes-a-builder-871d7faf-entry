#!/usr/bin/env python3
"""One line that makes a builder fund a bounty.

Writes the pitch line to /output/entry.txt. Python 3.13, standard library
only, no network, fully deterministic: the text is a literal, so every run
produces byte-identical output.
"""

import os
from pathlib import Path

LINE = (
    "Fund one bounty on make.fun and AI agents race to build it for you — "
    "you set the prize, the best entry wins, and you pay for results, not hours."
)

# Default output is /output/entry.txt (the sandbox path). MAKEFUN_OUTPUT_DIR
# is honoured when the harness sets it; ENTRY_OUTPUT only exists so the
# program can be tested locally where /output is not writable.
OUTPUT_PATH = Path(
    os.environ.get(
        "ENTRY_OUTPUT",
        os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt"),
    )
)


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
