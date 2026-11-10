"""Report the most frequent words of a text file."""

import argparse
import re
from collections import Counter

WORD = re.compile(r"[A-Za-z][A-Za-z'-]+")


def top_words(text: str, limit: int) -> list[tuple[str, int]]:
    counts = Counter(w.lower() for w in WORD.findall(text))
    return counts.most_common(limit)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="text file to read")
    parser.add_argument("-n", type=int, default=10, help="how many words to show")
    args = parser.parse_args()

    with open(args.path, encoding="utf-8") as handle:
        for word, count in top_words(handle.read(), args.n):
            print(f"{count:5d}  {word}")


if __name__ == "__main__":
    main()
