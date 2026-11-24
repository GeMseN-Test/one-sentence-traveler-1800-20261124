#!/usr/bin/env python3
"""One sentence for a traveler from 1800.

Writes a single 196-character sentence to /output/entry.txt. The sentence
explains the modern internet using only things a person from 1800 already
knows -- a library, a post office, a letter, the sea -- and no word coined
after their time. One comparison carries the whole sentence: a library and
a post office in one, with no walls and no waiting. Deterministic: the same
sentence, every run.
"""

import os

SENTENCE = (
    "It is a library and a post office in one, with no walls and no waiting: "
    "any book or letter in the world lies upon your table the moment it is "
    "written, and a voice from across the sea answers back."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")
    print(f"wrote {len(SENTENCE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
