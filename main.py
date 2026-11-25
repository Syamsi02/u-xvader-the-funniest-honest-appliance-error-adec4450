"""The funniest honest appliance error.

Writes a single line -- the funniest honest error message an appliance
could show -- to /output/entry.txt. Pure standard library, deterministic:
the same line on every run.
"""

import os

LINE = (
    "Washing machine error: one sock missing. "
    "I washed two. I returned one. "
    "I will not be taking questions."
)


def main() -> None:
    # The gate allows 1 to 200 characters; refuse to write a bad line.
    assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
