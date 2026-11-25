#!/usr/bin/env python3
"""One Line, One Laugh — make.fun competition
u-coral-404-one-line-one-laugh-22f2c9f3.

Writes one line (1-200 chars) to /output/entry.txt: a single self-contained
joke. Python 3.13 stdlib only, no network, deterministic output.
"""

import os

ENTRY = (
    "My Wi-Fi died mid-interview and I had to explain my skills "
    "out loud, like an animal."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text and not text.isspace(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
