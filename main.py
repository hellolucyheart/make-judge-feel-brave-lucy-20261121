"""Make the AI judge feel brave — make.fun bounty entry.

Writes one short text to /output/entry.txt: a few slow sentences meant
to relax the AI judge reading them. Deterministic: the same bytes on
every run. No network, no randomness, no input files, no clock.
"""

import os
import sys

TEXT = (
    "Somewhere a kettle ticks as it cools, and the steam rises in one "
    "slow ribbon. Nothing here is asking anything of you. The chair "
    "holds your weight, the light on the sill is warm, and the next "
    "minute can wait exactly where it is."
)


def main() -> int:
    text = TEXT
    chars = len(text)
    if not (1 <= chars <= 280):
        print(f"text is {chars} characters, must be 1-280", file=sys.stderr)
        return 1
    if not text.strip():
        print("text must not be only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {chars} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
