#!/bin/bash
# ------------------------------------------------
# Run quality checks
#
# SPDX-FileCopyrightText: (c) 2020-2026 T. Graf
# SPDX-License-Identifier: MIT
# ------------------------------------------------

echo "flake8 ..."
poetry run flake8

echo "markdownlint ..."
# --disable MD041 forces NO error for the social image in Readme.md
npx -q markdownlint-cli *.md --disable MD041

echo "isort ..."
poetry run isort .

echo "mypy ..."
poetry run mypy .

echo "codespell ..."
poetry run codespell .

echo "Done."

# ------------------------------------------------
# ------------------------------------------------

