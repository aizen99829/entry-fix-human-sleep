# SPDX-License-Identifier: MIT
"""Fix Human Sleep: Funniest Patch Note.

One line, at most 160 characters, written in the voice of a real
software changelog. The joke is that human sleep is treated as a
shipped feature with bugs, crashes, and a memory leak in the dream
subsystem — and the patch notes are dead serious about it.
"""

# Why this note works as a changelog, not just a joke:
# - "Fixed:" is the first word, exactly how a real release note opens.
# - The 3 AM crash is the most relatable sleep bug humans actually have:
#   you wake up for no reason and cannot fall back asleep.
# - "REM buffer overflow" and "garbage-collected dreams" translate sleep
#   science into engineering terms, so the whole line reads like a
#   maintainer describing a subsystem, not a comedian doing a bit.
# - The last clause flips the tone: waking up rested is filed as an
#   open issue, which is the punchline hiding inside the format.
MAX_LEN = 160

def validate(note: str) -> str:
    """One line, no newlines, within the 160-character limit."""
    text = " ".join(note.split())
    if len(text) > MAX_LEN:
        raise ValueError(f"patch note is {len(text)} chars, limit {MAX_LEN}")
    if "\n" in text:
        raise ValueError("patch note must be a single line")
    return text


PATCH_NOTE = (
    "Fixed: human sleep no longer crashes at 3 AM. "
    "REM buffer overflow patched; dreams now garbage-collected nightly. "
    "Waking up rested still under investigation."
)


def write_entry(note: str) -> None:
    """Write the validated patch note to /output/entry.txt."""
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(validate(note) + "\n")


def main() -> None:
    # Print the note for the log, then persist it as the entry.
    note = validate(PATCH_NOTE)
    print(note)
    print(f"({len(note)} characters)")
    write_entry(note)


if __name__ == "__main__":
    main()

