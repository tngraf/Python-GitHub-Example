# AGENTS.md

This is a demo/test Python project.

## General

- Use `poetry` to manage the project.
- Use `requests` for HTTP communication.
- Use `pytest` for unit testing.
- Use `responses` for mocking HTTP requests.

## Code Style

- use `flake8`
- use `isort`
- use type hints
- use `requests` for HTTP communication

## Naming Conventions

- Follow PEP 8 naming conventions
- Use ALL_CAPS for constants

## Running Tests

Run all tests via

```shell
poetry run pytest
```

## Code Coverage

Run all tests via

```shell
poetry run pytest
```

## Code Style Checks

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

## Code Quality

- Use meaningful variable and function names that clearly describe their purpose
- Include helpful comments for complex logic
- Add error handling for user inputs and API calls
- Use type hints throughout the codebase for better IDE support
- Include docstrings for all public methods

## PR instructions

- Title format: [<project_name>] Title
