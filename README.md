# Bazel Python Boilerplate

This repository provides a ready-to-use setup for Python projects with:

- **Bazel** for build automation and dependency management
- **Gazelle** for automatic BUILD file generation

## Quick Start

### Prerequisites

1. Install Bazelisk (manages Bazel versions automatically):

#### macOs
```bash
brew install bazelisk
```

#### Windows
```bash
# Using winget
winget install Bazel.Bazelisk

# Or using Chocolatey
choco install bazelisk

# Or using Scoop
scoop install bazelisk
```

#### Linux
```bash
mise use -g bazelisk@latest
```

2. Install CookieCutter:
```bash
pip install cookiecutter
```

### Creating a New Project

1. Generate your project from the template:
```bash
cookiecutter gh:miguelmendozajr/bazel-python-boilerplate
```

2. You'll be prompted for:
   - `project_name`: Your project directory name
   - `python_version`: Python version to use

### Project Structure

```
project/
├── .bazelversion          # Bazel version specification
├── .gitignore
├── BUILD.bazel            # Root build file
├── MODULE.bazel           # Bazel module definition
├── gazelle_python.yaml    # Gazelle configuration
├── requirements.in        # Python dependencies (pip-tools)
├── requirements.txt       # Locked dependencies
├── install                # Script for downloading and integrating dependencies
├── intellisense           # VS Code IntelliSense generator
├── update                 # BUILD files updater
├── .github/
│   └── workflows/
│       └── ci.yml        # GitHub Actions CI/CD
└── src/
    └── package/
        ├── BUILD.bazel
        ├── __init__.py
        ├── main.py       # Entry point
        └── tests/
            ├── BUILD.bazel
            ├── __init__.py
            └── main_test.py
```

### Running a target
```bash
bazel run src/package:main
```

### Testing targets

Run all tests (test files should have the `_test.py` suffix):

```bash
bazel test //...
```

### Adding Dependencies

Before adding a dependency, check if it's already in `requirements.txt` or `requirements.in`. If it exists, skip step 1.

1. Add your dependency to `requirements.in`:
   ```
   numpy==2.4.1
   rich>=13.0.0
   ```

2. Import your dependency in source code:
   ```python
   import rich
   ```

3. Update BUILD files:
   ```bash
   ./update
   ```