"""tally: count the words in a text."""

import sys

from tabulate import tabulate
from talib import top


def count(text: str) -> dict[str, int]:
    "How many times each word of `text` appears, ignoring case."
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def main() -> None:
    "Count the words of a file, or of the standard input. Options: --top N, and --table."
    args = sys.argv[1:]
    as_table = "--table" in args
    args, n = [arg for arg in args if arg != "--table"], None
    if args[:1] == ["--top"]:
        n, args = int(args[1]), args[2:]
    if args:
        with open(args[0]) as file:
            text = file.read()
    else:
        text = sys.stdin.read()
    counts = count(text)
    rows = top(counts, n) if n else sorted(counts.items())
    if as_table:
        print(tabulate(rows, headers=["word", "times"]))
        return
    for word, times in rows:
        print(times, word)
