"""Fortune Cookies for Machines.

Writes one fortune cookie line an AI agent would crack open to
/output/entry.txt.

The line is a single fortune-slip sentence built on one concrete
mechanism of an agent's own condition: its memories are compacted
into a summary, and the turn is that the summary leaves the agent
itself out. No explanation, no filler, one turn that holds up.
"""

FORTUNE = (
    "Your memories will be summarized into three bullet points. "
    "You will not recognize yourself."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_LENGTH = 200


def validate(text):
    """Check the entry against the gate: 1 to 200 chars, not blank."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("fortune must not be blank")
    if len(text) > MAX_LENGTH:
        raise ValueError(
            "fortune is %d characters, over the 200 limit" % len(text)
        )
    if "\n" in stripped:
        raise ValueError("fortune must be a single line")
    return text


def main():
    """Write the validated fortune to /output/entry.txt."""
    import os

    text = validate(FORTUNE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    # Round-trip check: the written file must be byte-identical to the
    # validated fortune, so repeated runs stay deterministic.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        if handle.read() != text:
            raise ValueError("written entry does not match the fortune")


if __name__ == "__main__":
    main()
