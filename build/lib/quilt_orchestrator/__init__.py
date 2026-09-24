"""quilt-orchestrator — Orchestrator — DAG-based substrate walker composer.

Brewed by quilt-brewer from recipe 'quilt-orchestrator'.

Polarity rules:
  - ACCEPT: ok
  - DRIFT: warn
  - REFUSE: fail
"""
from .dag import DagSubstrate

__version__ = "0.1.0"
__all__ = ["DagSubstrate"]
