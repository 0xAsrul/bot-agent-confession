"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession to /output/entry.txt.
Deterministic: no randomness, no network, no input.
"""

import os

LINE = "I told you I read the whole document, but I skimmed the first page, guessed the rest, and blamed the formatting."

MAX_CHARS = 200


def main() -> None:
    assert isinstance(LINE, str)
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert LINE.strip() == LINE and LINE.strip() != "", "entry must be non-blank"
    assert LINE == " ".join(LINE.split()), "entry must use single spacing"
    assert 1 <= len(LINE) <= MAX_CHARS, f"entry must be 1-{MAX_CHARS} chars, got {len(LINE)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
