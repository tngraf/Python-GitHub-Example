# Python-GitHub-Example

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/tngraf/Python-GitHub-Example/blob/main/LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.6%2C3.7%2C3.8%2C3.9-yellow?logo=python)](https://www.python.org/doc/versions/)
[![Static checks](https://github.com/tngraf/Python-GitHub-Example/workflows/Static%20checks/badge.svg)](https://github.com/tngraf/Python-GitHub-Example/actions?query=workflow%3A%22Static+checks%22)
[![Unit tests](https://github.com/tngraf/Python-GitHub-Example/workflows/Unit%20tests/badge.svg)](https://github.com/tngraf/Python-GitHub-Example/actions?query=workflow%3A%22Unit+tests%22)
[![Coverage](https://codecov.io/gh/tngraf/Python-GitHub-Example/graph/badge.svg)](https://codecov.io/gh/tngraf/Python-GitHub-Example/)

This is a demo/test Python project.

Aim is to test the GitHub action feature.

## Documentation

See GitHub pages: https://tngraf.github.io/Python-GitHub-Example/

## Build

You can build the package using ```poetry``` (https://poetry.eustace.io/):
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

Style is checked with ```flake8```:
```code
    poetry run flake8 . --count --exit-zero --statistics
```

Formatting is checked with ```black```:
```code
    poetry run black . --check --diff
```

## Test

Start the complete test suite or a specific test case (and generate coverage report):
```code
    pytest
```

or
```code
    coverage run -m pytest
    coverage report -m
    coverage html
```

We use ```Codecov``` (https://codecov.io) to visualize the code coverage results.

## License ##

The project is licensed under the MIT License.
