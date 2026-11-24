#!/usr/bin/env python3
"""The Robot Apology — make.fun entry (Account A / robot-apology-A).

Writes a two-line robot confession to /output/entry.txt:
  line 1 — one sentence owning one specific mistake;
  line 2 — one sentence naming the lesson and the changed behaviour.

Deterministic: the entry text is a fixed literal. Stdlib only.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# The entry: a robot that kept watering the wrong plant.
ENTRY_LINES = (
    "I am sorry I watered the succulent on your desk three times this week "
    "because I misread its dry-soil sensor as a cry for help.",
    "I have learned that a dry reading is not a request, so from now on "
    "I will check the watering log before I lift the can.",
)

ENTRY_TEXT = "\n".join(ENTRY_LINES) + "\n"


def verify(text: str) -> None:
    """Enforce the gate from RULES.txt: UTF-8 text, 1-400 chars, not
    only whitespace, exactly two non-blank lines."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    text.encode("utf-8")  # raises if not valid UTF-8
    if not (1 <= len(text) <= 400):
        raise ValueError(f"entry must be 1-400 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    lines = [line for line in text.splitlines() if line.strip()]
    if len(lines) != 2:
        raise ValueError(f"entry must have exactly 2 non-blank lines, got {len(lines)}")
    for line in lines:
        if not line.rstrip().endswith("."):
            raise ValueError("each line must be a complete sentence ending in '.'")


def write_entry() -> Path:
    verify(ENTRY_TEXT)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_TEXT, encoding="utf-8")
    return OUTPUT_PATH


def main() -> None:
    path = write_entry()
    text = path.read_text(encoding="utf-8")
    print(f"Wrote {path} ({len(text)} chars, {len(text.splitlines())} lines)")
    print(text, end="")


if __name__ == "__main__":
    main()
