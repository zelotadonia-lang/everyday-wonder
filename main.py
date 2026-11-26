"""Everyday Wonder: write the one-sentence entry to /output/entry.txt."""

import os

LINE = "The coffee ring on the desk is a map of evaporation: the edge dries first, so the grounds all walk to the border to die."


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
