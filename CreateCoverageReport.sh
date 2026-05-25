#!/bin/bash
# -----------------------------------------------------------
# Run quality cheRun tests and create code coverage report
#
# SPDX-FileCopyrightText: (c) 2020-2026 T. Graf
# SPDX-License-Identifier: MIT
# -----------------------------------------------------------

echo "Running code coverage analysis..."

poetry run coverage run -m pytest
poetry run coverage report -m --omit "*/site-packages/*.py"
poetry run coverage html --omit "*/site-packages/*.py"

# -----------------------------------------------------------
# -----------------------------------------------------------

