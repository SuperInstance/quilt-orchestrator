# quilt-orchestrator

> Orchestrator — DAG-based substrate walker composer

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)]()
[![Tests](https://img.shields.io/badge/tests-6+-brightgreen.svg)](tests/)
[![Brewed by](https://img.shields.io/badge/brewed_by-quilt--brewer-purple.svg)](https://github.com/SuperInstance/quilt-brewer)

## What is this?

Brewed by `quilt-brewer` from the `quilt-orchestrator` recipe. Implements the
canonical substrate walker pattern (199 LOC wrapper + tests + demo).

## Polarity rules

| Polarity | Status |
|---|---|
| **ACCEPT** | `ok` |
| **DRIFT** | `warn` |
| **REFUSE** | `fail` |

## Operations

- plan
- execute
- compose
- validate

## Usage

```python
from quilt_orchestrator import DagSubstrate

substrate = DagSubstrate()
receipt = substrate.step("cell-id", {"key": "value"}, status="ok")
print(receipt.polarity)  # ACCEPT
```

## Run tests

```bash
python3 -m unittest tests.test_dag -v
```

## Run demo

```bash
python3 examples/demo.py
```

## License

Apache-2.0
