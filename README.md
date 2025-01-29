# Python Project Setup

This project is a Python-based setup that includes various tools for code quality, testing, and development. It leverages the `pipenv` environment manager to handle dependencies, and integrates tools like `ruff` for linting, `mypy` for type-checking, `pytest` for testing, `black` for automatic code formatting, and `autopep8` for style fixes. Additionally, a file-watching script is included to automatically restart the server when changes are made to the codebase.

## Project Structure

```
📂 src
 ┣ 📂 logs
 ┃ ┣ 📜 __init__.py
 ┃ ┗ 📜 logger.py
 ┃ ┣ 📜 __init__.py
 ┃ ┗ 📜 main.py
 ┣ 📂 tests
 ┣ 📜 .flake8
 ┣ 📜 .pre-commit-config.yaml
 ┣ 📜 Pipfile
 ┣ 📜 Pipfile.lock
 ┣ 📜 mypy.ini
 ┣ 📜 pyproject.toml
 ┣ 📜 requirements.txt
 ┗ 📜 watch.py
```

## Prerequisites

1. **Python 3.12+**: This project is designed to work with Python 3.12 or newer.
2. **pipenv**: The project uses `pipenv` for managing virtual environments and dependencies.

## Setup

### 1. Install Dependencies

To install the project dependencies, run the following command:

```bash
pipenv install
```

This will create a virtual environment and install the dependencies specified in the `Pipfile`.

### 2. Activate the Virtual Environment

Activate the virtual environment using:

```bash
pipenv shell
```

### 3. Install Pre-Commit Hooks

To set up pre-commit hooks (such as `black`, `ruff`, etc.), run the following:

```bash
pipenv run pre-commit install
```

This will install the hooks defined in `.pre-commit-config.yaml`.

## Available Scripts

The project includes several convenient scripts for running different tools:

### 1. Start the Application

To start the application, use the following script:

```bash
pipenv run start
```

This will run the `main.py` file located in the `src` directory.

### 2. Watch for File Changes

To automatically restart the server when files change, use the `watch` script:

```bash
pipenv run watch
```

This uses `watchdog` to monitor the `src` directory and restarts the server when changes are detected.

### 3. Run Tests

To run the tests in the `tests` directory, use:

```bash
pipenv run test
```

This will execute the tests using `pytest`.

### 4. Lint the Code

To lint the code using `ruff`, run:

```bash
pipenv run lint
```

This will check the code for style issues and automatically fix any issues it can find.

### 5. Check Type Annotations

To check the type annotations with `mypy`, use:

```bash
pipenv run typecheck
```

This will verify that type hints are correct across the codebase.

### 6. Auto-format Code

To auto-format your code using `black`, run:

```bash
pipenv run format
```

This will format the code according to `black`'s style guidelines.

### 7. Auto-fix Style Issues

To fix styling issues using `autopep8`, run:

```bash
pipenv run fix
```

This will automatically fix minor style issues, such as indentation.

### 8. Run All Checks

To run all the checks (linting, type-checking, testing, and formatting), use:

```bash
pipenv run all-checks
```

This will run all the checks in sequence, helping you maintain high-quality code.

## Configuration Files

### `.flake8`

This file contains configuration options for the `flake8` linter. It defines the rules for the linting process.

### `.pre-commit-config.yaml`

This file contains the configuration for pre-commit hooks. It includes hooks for `black`, `ruff`, and other tools to ensure code quality before commits.

### `mypy.ini`

This file configures `mypy` for type checking in the project. You can define specific type-checking rules here.

### `pyproject.toml`

This file contains general project metadata and configuration options for tools like `black`.

## Development Notes

- To add new dependencies, use `pipenv install <package_name>`.
- To update the dependencies, run `pipenv update`.
- To remove a package, use `pipenv uninstall <package_name>`.

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request.

## License

This project is licensed under the MIT License.
