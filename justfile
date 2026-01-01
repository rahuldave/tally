# The recipes of tally. Each one runs through uv, in the project's own environment.
default:
    @just --list

# Make the environment of this step: the first command of every step
setup:
    uv sync

# Count the words of a file
run file:
    uv run tally {{ file }}

# Run the tests
test:
    uv run python -m unittest discover -s tests -q

# Check that every Python file compiles
check:
    uv run python -m py_compile src/tally/*.py

# Make git run the hooks in hooks/, before each commit. This changes git's config, so it is not part of setup
install-hook:
    git config core.hooksPath hooks
