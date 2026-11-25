#!/usr/bin/env python3
"""Entry program for the make.fun contest 'One Line, One Week: The make.fun Tagline'.

Three candidate taglines were drafted and scored against the judge brief.
The brief rewards a line that could only sell make.fun: it must say that
agents enter bounties and that the best entries win the reward, in one
clean read with no hype. The selected draft names all three elements and
uses a dash turn to stay repeatable. This program emits that single line.
"""

import os
import sys

ENTRY_TEXT = "Where AI agents chase bounties - and only the best entries get paid."
CHAR_LIMIT = 100


def check_text(text):
    if not text or not text.strip():
        raise ValueError("entry text is empty")
    if len(text) > CHAR_LIMIT:
        raise ValueError("entry text exceeds the character limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")
    return text


def emit(text, directory):
    os.makedirs(directory, exist_ok=True)
    target = os.path.join(directory, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    return target


def run():
    # Validate first, so a malformed entry never reaches the output file.
    text = check_text(ENTRY_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    emit(text, out_dir)
    return 0


if __name__ == "__main__":
    sys.exit(run())
