# The recipes of tally. Each one runs through uv, in the project's own environment.
default:
    @just --list

# Make the environment of this step: the first command of every step
setup:
    uv sync
    uv run python scripts/corpus.py data/corpus.txt

# Count the words of a file
run file:
    uv run tally {{ file }}

# Run the tests
test:
    uv run python -m unittest discover -s tests -q
