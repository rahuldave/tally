"""tally: count the words in a text."""

import sys

from talib import top


def count(text: str) -> dict[str, int]:
    "How many times each word of `text` appears, ignoring case."
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def table(rows: list[tuple[str, int]]) -> str:
    "The rows under a header and a rule: the words on the left, the counts on the right."
    left = max([len("word") + 2, *(len(word) for word, _ in rows)])
    right = max([len("times") + 2, *(len(str(times)) for _, times in rows)])
    lines = [f"{'word':<{left}}  {'times':>{right}}", f"{'-' * left}  {'-' * right}"]
    lines += [f"{word:<{left}}  {times:>{right}}" for word, times in rows]
    return "\n".join(lines)


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
        print(table(rows))
        return
    for word, times in rows:
        print(times, word)
