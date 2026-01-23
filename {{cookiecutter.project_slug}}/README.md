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
bazel run src/package:main
```

### Testing the project

Run all tests (test files should have the `_test.py` suffix):

```bash
bazel test //...
```

### Adding Dependencies

1. Add your dependency to `requirements.in`:
   ```
   numpy==2.4.1
   rich>=13.0.0
   ```

2. Install dependencies:
   ```bash
   ./install
   ```

3. Import your dependency in source code:
   ```python
   import rich
   ```

4. Update BUILD files:
   ```bash
   ./update
   ```