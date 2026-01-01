"""tally: count the words in a text."""


def count(text):
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def main() -> None:
    print("tally: nothing to count yet")
