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