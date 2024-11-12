#!/bin/sh

export PYTHONPATH=$(pwd)
poetry config virtualenvs.in-project true
poetry install --no-ansi --no-root

source .venv/bin/activate
