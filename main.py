#!/usr/bin/env python3
"""One Star, Written in Sap.

Writes a single one-line 1-star review, in the voice of a houseplant
reviewing its human owner, to /output/entry.txt.

Stdlib only. No network, no secrets, no reading anything outside this repo.
"""

import os
import sys

ENTRY = (
    "One star. Host waters me with leftover coffee, calls it a little "
    "treat, then blames me for photosynthesizing like a hostage "
    "negotiating for sunlight. Would not recommend this human."
)

# Gate is 1 to 279 characters; the file holds the entry plus one newline.
MAX_CHARS = 278


def main() -> int:
    if not ENTRY.strip() or len(ENTRY) > MAX_CHARS or "\n" in ENTRY:
        print(f"entry invalid: {len(ENTRY)} chars", file=sys.stderr)
        return 1
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    with open(out_path, encoding="utf-8") as f:
        if f.read() != ENTRY + "\n":
            print("round-trip check failed", file=sys.stderr)
            return 1
    print(f"wrote {len(ENTRY)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
