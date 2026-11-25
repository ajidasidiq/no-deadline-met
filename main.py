#!/usr/bin/env python3
"""No Deadline Met — writes a single-line joke excusing a missed deadline.

The entry line is embedded here as a constant. The program writes it to
/output/entry.txt and then self-checks the written file: it must be valid
UTF-8 text of 1-200 characters and not only whitespace (the competition gate).
"""

import os

ENTRY = "I finished it in my head three days ago \u2014 unfortunately, my head doesn\u2019t have a submit button."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Write atomically so a partial run can never leave a half-written entry.
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, OUTPUT_PATH)

    # Gate self-check on the file actually written, not just the constant.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")  # raises UnicodeDecodeError if not valid UTF-8
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry is only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    print(f"OK: wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
