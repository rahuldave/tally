# tally

Count the words in a text.

## Run it

Make the environment, the corpus and the report first. Then count the words of a file:

    just setup
    uv run tally data/corpus.txt

`uv run tally --top 10 data/corpus.txt` prints only the ten most common words. `just test` runs the tests, and
`just report` writes the ten most common words of the corpus to `build/top.txt`.

## Count from Python

tally is a library too. `count` counts the words of a text, and `top` keeps the most common:

```python
from pathlib import Path

from tally import count, top

counts = count(Path("data/corpus.txt").read_text())
print(top(counts, 3))
```

It prints `[('line', 127), ('class', 126), ('word', 125)]`, the three most common words of the corpus.

The page [How to run tally](docs/how%20to%20run.md) says more, with a picture of the most common words.
