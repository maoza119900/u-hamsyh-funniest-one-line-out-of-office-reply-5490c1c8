#!/usr/bin/env python3
"""Funniest one-line out-of-office reply.

Prints the reply to stdout and writes it to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output), as the bounty requires: one line of UTF-8 text.
"""

import os

REPLY = "I'm away — please direct all urgent matters to my houseplant. It has firm boundaries and no Wi-Fi."

# Gate: entry.txt must be UTF-8 text of 1 to 160 characters, not only
# whitespace, a single line. Check it here so a bad edit fails loudly.
assert 1 <= len(REPLY) <= 160, "reply must be 1-160 characters"
assert "\n" not in REPLY and REPLY.strip(), "reply must be one non-blank line"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(REPLY)
    print(REPLY)


if __name__ == "__main__":
    main()
