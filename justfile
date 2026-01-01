# The recipes of tally. Each one runs through uv, in the project's own environment.
default:
    @just --list

# Make the environment of this step: the first command of every step
setup:
    uv sync
    uv run python scripts/corpus.py data/corpus.txt
    test -f build/top.txt || just report

# Count the words of a file
run file:
    uv run tally {{ file }}

# Run the tests
test:
    uv run python -m unittest discover -s tests -q

# Write the ten most common words of the corpus to build/top.txt
report:
    mkdir -p build
    uv run tally --top 10 data/corpus.txt > build/top.txt
