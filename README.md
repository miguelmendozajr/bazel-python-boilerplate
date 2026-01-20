# Bazel Python Boilerplate

This repository provides a ready-to-use setup for Python projects with:

- **Bazel** for build automation and dependency management
- **Gazelle** for automatic BUILD file generation

## Quick Start

### Prerequisites

Install Bazelisk (manages Bazel versions automatically):

```bash
brew install bazelisk
```

### Running the project

```bash
bazel run src/app:main
```

### Testing the project

Run all tests (test files should have the `_test.py` suffix):

```bash
bazel test //...
```

### Adding Dependencies

1. Import your dependency to source code:
    ```
    import requests
    ```

2. Add your dependency to `requirements.in`:
   ```
   numpy==2.4.1
   requests>=2.28.0
   ```

3. Update dependencies:
   ```bash
   ./update
   ```