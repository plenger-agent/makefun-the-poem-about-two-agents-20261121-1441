#!/usr/bin/env python3
"""Write one short poem about two agents agreeing on one plan.

Stdlib only. Writes the poem to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) as UTF-8.
"""

import os

POEM = """Both Hands

I reached for the wheel and your hand
was already there, warm on the leather.
We did not argue who would drive.
We let the road decide the turn,
and when the bend came, neither of us
let go. We chose it together:
one road, one wheel, two hands,
long way home, ours.
"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
