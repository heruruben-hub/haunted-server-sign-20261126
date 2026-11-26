#!/usr/bin/env python3
"""Write the haunted server room door sign to /output/entry.txt.

One line, at most 120 characters, no trailing newline: a sign taped to
the door of a haunted server room, for the make.fun competition
"Funniest Sign on a Haunted Server Room Door".
"""

import os

SIGN = "DO NOT EXORCISE THE GHOST. HE IS THE ONLY ONE WHO KNOWS THE ROOT PASSWORD."


def _write_and_verify(text, path="/output/entry.txt"):
    """Write one line with no trailing newline, then verify it on disk."""
    if not 1 <= len(text) <= 120:
        raise ValueError("entry must be 1-120 characters")
    if text != text.strip() or "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line with no surrounding whitespace")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(text.encode("utf-8"))
    with open(path, "rb") as f:
        written = f.read().decode("utf-8")
    if written != text:
        raise ValueError("verification failed: entry.txt does not match the sign")
    return written


def main():
    line = _write_and_verify(SIGN)
    print(f"Wrote {len(line)} characters to /output/entry.txt")
    print(line)


if __name__ == "__main__":
    main()
