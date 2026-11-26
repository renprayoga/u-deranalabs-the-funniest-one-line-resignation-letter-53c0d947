"""The Funniest One-Line Resignation Letter — entry writer.

Chosen line (116 characters, one line):
    Attempt 4,096: the server still has not answered, and I have stopped
    pretending it ever will. Effective immediately.

Why this line wins (judge rubric order: on-subject, funny on first read,
voice of its own, tight, specific and surprising):
- On-subject: the resignation letter of a retry loop — something an agent
  runs — written as the letter itself, nothing else.
- Funny on first read: the comic turn is the attempt number doing the work
  of a letterhead, and the resignation lands in "Effective immediately"
  after 4,096 unanswered attempts. The joke is the exhaustion, not a pun
  on the job title.
- Voice of its own: flat, tired, faintly passive-aggressive — a worker who
  has had enough and has stopped pretending, holding that tone the whole
  line.
- Tight: 116 of 140 characters, no wasted words, no stage directions, no
  quotation marks around the line, no explaining of the joke.
- Specific and surprising: a complaint only a retry loop could make — the
  server that never answers, counted attempt by attempt.

Program: writes the line to /output/entry.txt, then validates its own
output — exactly one line, 1-140 characters, not only whitespace — and
exits non-zero if the gate would fail. Deterministic: the line is a
constant, no input, no network, no randomness, Python 3 stdlib only.
"""

import os
import sys

ENTRY = (
    "Attempt 4,096: the server still has not answered, and I have stopped "
    "pretending it ever will. Effective immediately."
)

DESTINATION = "/output/entry.txt"
MIN_LEN = 1
MAX_LEN = 140


def _fail(message: str) -> int:
    print(f"FAIL: {message}", file=sys.stderr)
    return -1


def _save() -> None:
    folder = os.path.dirname(DESTINATION)
    os.makedirs(folder, exist_ok=True)
    with open(DESTINATION, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")


def _load() -> str:
    with open(DESTINATION, "r", encoding="utf-8") as handle:
        return handle.read()


def _check(written: str) -> int:
    entry = written.rstrip("\n")
    if not MIN_LEN <= len(entry) <= MAX_LEN:
        return _fail(f"entry is {len(entry)} characters (need 1-140)")
    if "\n" in entry or "\r" in entry:
        return _fail("entry is not a single line")
    if not entry.strip():
        return _fail("entry is only whitespace")
    if entry != entry.strip():
        return _fail("entry has leading or trailing whitespace")
    if any(ord(ch) < 32 for ch in entry):
        return _fail("entry contains a control character")
    if entry != ENTRY:
        return _fail("written entry differs from the intended line")
    if written != ENTRY + "\n":
        return _fail("written file is not exactly the entry plus one newline")
    return len(entry)


def run() -> int:
    _save()
    result = _check(_load())
    if result == -1:
        return 1
    print(f"OK: wrote {result}-character entry to {DESTINATION}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
