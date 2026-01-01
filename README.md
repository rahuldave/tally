# tally

Count the words in a text.

## Run it

Make the environment, the corpus and the report first. Then count the words of a file:

    just setup
    uv run tally data/corpus.txt

`uv run tally --top 10 data/corpus.txt` prints only the ten most common words. `just test` runs the tests, and
`just report` writes the ten most common words of the corpus to `build/top.txt`.
