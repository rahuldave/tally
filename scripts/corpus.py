"""Write data/corpus.txt, a text of 2000 words to count, the same every time. Leave it alone if it is there."""

import sys
from pathlib import Path

WORDS = "the a word count text tally test step move commit tag note slide class shell file line code".split()


def main() -> None:
    target = Path(sys.argv[1] if len(sys.argv) > 1 else "data/corpus.txt")
    if target.exists():
        print(f"{target} is there")
        return
    seed, words = 7, []
    for _ in range(2000):
        seed = (seed * 1103515245 + 12345) % 2**31
        words.append(WORDS[seed % len(WORDS)])
    target.parent.mkdir(parents=True, exist_ok=True)
    lines = (" ".join(words[i : i + 12]) for i in range(0, len(words), 12))
    target.write_text("\n".join(lines) + "\n")
    print(f"wrote {target}: {len(words)} words")


if __name__ == "__main__":
    main()
