"""The Worst App Idea Ever Pitched -- make.fun bounty
u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23.

Writes one sentence (191 characters, inside the 240-character gate)
pitching the worst app imaginable to /output/entry.txt.

The pitch: NapTrack, a nap app that wakes you every 20 minutes to confirm
you are still napping, then charges $3.99 a month to graph how tired its
own interruptions made you -- for the 4 million Americans who nap wrong.
The absurd logic is the joke itself: the app defeats its own purpose, and
the founder states it with total confidence. One product name, one
useless function, one audience, three concrete numbers, one sentence.
"""

import os
import sys

ENTRY = (
    "NapTrack wakes you every 20 minutes to confirm you are still napping, "
    "then charges $3.99 a month to graph how tired its own interruptions "
    "made you \u2014 for the 4 million Americans who nap wrong."
)

MAX_CHARS = 240


def validate_entry(text: str) -> str:
    """Gate check (competition rules): UTF-8, 1-240 chars, one sentence."""
    assert isinstance(text, str) and text, "entry must be a non-empty string"
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= MAX_CHARS, (
        "entry is %d chars, gate is 1-%d" % (len(text), MAX_CHARS)
    )
    assert text == text.strip(), "entry must not start or end with whitespace"
    # One clean sentence: exactly one sentence-ending period, at the end.
    # The "$3.99" price holds the only other period, inside a number.
    assert text.endswith("."), "entry must end with a period"
    assert text.count(".") == 2, (
        "entry must be one sentence, found %d periods" % text.count(".")
    )
    text.encode("utf-8")  # gate: must be valid UTF-8
    return text


def summarize(text: str) -> str:
    """One-line summary of the entry for the run log (stdout stays clean)."""
    return "entry: %d chars, %d bytes, %d words, 1 sentence" % (
        len(text),
        len(text.encode("utf-8")),
        len(text.split()),
    )


def main() -> int:
    text = validate_entry(ENTRY)
    print(summarize(text), file=sys.stderr)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
