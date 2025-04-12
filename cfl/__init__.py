"""CFL API SDK for Python.

A modern, lightweight client for interacting with the CFL API.
"""

from .client import CFLClient
from .constants import (
    DEFAULT_LIMIT,
    DEFAULT_PAGE,
    DEFAULT_TIMEOUT,
)

__all__ = [
    "CFLClient",
    "DEFAULT_LIMIT",
    "DEFAULT_PAGE",
    "DEFAULT_TIMEOUT",
]

__version__ = "0.1.0"
