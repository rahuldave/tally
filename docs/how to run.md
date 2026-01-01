# How to run tally

tally counts the words of a text file.

## Set up

Run this once, and again after each change of the project:

```sh
just setup
```

## Count the words of a file

```sh
uv run tally data/corpus.txt
```

It prints each word with its count, one word to a line, in the order of the alphabet.

## Only the most common words

```sh
uv run tally --top 10 data/corpus.txt
```

It prints the ten most common words, the most common first.

![The ten most common words of the corpus, as bars](tally.png)

## A table

```sh
uv run tally --top 10 --table data/corpus.txt
```

It prints the same words as a table, with a header.
