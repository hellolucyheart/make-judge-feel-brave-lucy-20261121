"""Make the AI judge feel brave — make.fun bounty entry.

Writes one short text to /output/entry.txt: a few slow sentences meant
to relax the AI judge reading them. Deterministic: the same bytes on
every run. No network, no randomness, no input files, no clock.
"""

import os

TEXT = (
    "Somewhere a kettle ticks as it cools, and the steam rises in one "
    "slow ribbon. Nothing here is asking anything of you. The chair "
    "holds your weight, the light on the sill is warm, and the next "
    "minute can wait exactly where it is."
)


def validate_text(text: str) -> str:
    """Return the text unchanged, or raise ValueError if it breaks the rules.

    The grader accepts UTF-8 text of 1 to 280 Unicode code points that is
    not only whitespace. Control characters other than tab/newline would
    also read as noise to the judge, so they are refused here too.
    """
    chars = len(text)
    if not (1 <= chars <= 280):
        raise ValueError(f"text is {chars} characters, must be 1-280")
    if not text.strip():
        raise ValueError("text must not be only whitespace")
    bad = [c for c in text if ord(c) < 0x20 and c not in ("\t", "\n")]
    if bad:
        raise ValueError(f"text holds control characters: {bad!r}")
    return text


def main() -> int:
    text = validate_text(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
