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
