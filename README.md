# Python-GitHub-Example

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/tngraf/Python-GitHub-Example/blob/main/LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.6%2C3.7%2C3.8%2C3.9-yellow?logo=python)](https://www.python.org/doc/versions/)
[![Static checks](https://github.com/tngraf/Python-GitHub-Example/workflows/Static%20checks/badge.svg)](https://github.com/tngraf/Python-GitHub-Example/actions?query=workflow%3A%22Static+checks%22)
[![Unit tests](https://github.com/tngraf/Python-GitHub-Example/workflows/Unit%20tests/badge.svg)](https://github.com/tngraf/Python-GitHub-Example/actions?query=workflow%3A%22Unit+tests%22)
[![Coverage](https://codecov.io/gh/tngraf/Python-GitHub-Example/graph/badge.svg)](https://codecov.io/gh/tngraf/Python-GitHub-Example/)

This is a demo/test Python project.

Aim is to test the GitHub action feature.

## Documentation

See GitHub pages: <https://tngraf.github.io/Python-GitHub-Example/>

## AI Support

The main information about the project is in [AGENTS.md](AGENTS.md).
[CLAUDE.md](CLAUDE.md) and [copilot-instructions.md](./.github/copilot-instructions.md) only
refer to [AGENTS.md](AGENTS.md).

## Build

You can build the package using [poetry](https://poetry.eustace.io/):

```code
poetry build
```

Build documentation (the generated static site must be pushed to the **gh-pages** branch):

```code
sphinx-build ./docs/source ./docs/build
```

Cleanup builds:

```code
rm -r dist/ build/ docs/
```

## Style & Formatting

Style is checked with [flake8](https://flake8.pycqa.org/en/latest/):

```code
poetry run flake8 . --count --exit-zero --statistics
```

Import order is checked with [isort](https://isort.readthedocs.io/en/latest/):

```code
poetry run isort .
```

Formatting is checked with [black](https://github.com/psf/black):

```code
poetry run black . --check --diff
```

Type information is checked with [mypy](https://mypy-lang.org/):

```code
poetry run mypy .
```

## Test

Start the complete test suite or a specific test case (and generate coverage report):

```code
poetry run pytest
```

or

```code
poetry run coverage run -m pytest
poetry run coverage report -m
poetry run coverage html
```

We use [Codecov](https://codecov.io) to visualize the code coverage results.

## Pre-Commit

Run locally

```shell
poetry run pre-commit run --all-files
```

## License

The project is licensed under the MIT License.
