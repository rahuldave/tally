"""tally: count the words in a text."""

import sys


def count(text: str) -> dict[str, int]:
    "How many times each word of `text` appears, ignoring case."
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def main() -> None:
    text = open(sys.argv[1]).read() if len(sys.argv) > 1 else sys.stdin.read()
    for word, n in sorted(count(text).items()):
        print(n, word)
