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
from tally import count, top

counts = count("the cat and the hat")
print(top(counts, 2))
```

It prints `[('the', 2), ('and', 1)]`.

The page [How to run tally](docs/how%20to%20run.md) says more, with a picture of the most common words.
