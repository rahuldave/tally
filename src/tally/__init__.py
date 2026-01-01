"""tally: count the words in a text."""

import sys


def count(text: str) -> dict[str, int]:
    "How many times each word of `text` appears, ignoring case."
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def top(counts: dict[str, int], n: int) -> list[tuple[str, int]]:
    "The n most common words, most common first."
    return sorted(counts.items(), key=lambda pair: (-pair[1], pair[0]))[:n]


def main() -> None:
    "Count the words of a file, or of the standard input. With --top N, only the N most common."
    args, n = sys.argv[1:], None
    if args[:1] == ["--top"]:
        n, args = int(args[1]), args[2:]
    text = open(args[0]).read() if args else sys.stdin.read()
    counts = count(text)
    for word, times in top(counts, n) if n else sorted(counts.items()):
        print(times, word)
