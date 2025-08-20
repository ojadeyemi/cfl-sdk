"""CFL API SDK for Python.

A modern, lightweight client for interacting with the CFL API.
"""

from .client import CFLClient
from .constants import (
    DEFAULT_LIMIT,
    DEFAULT_PAGE,
    DEFAULT_TIMEOUT,
)
from .exceptions import (
    CFLAPIAuthenticationError,
    CFLAPIConnectionError,
    CFLAPIError,
    CFLAPINotFoundError,
    CFLAPIResponseError,
    CFLAPIServerError,
    CFLAPITimeoutError,
    CFLAPIValidationError,
)

__all__ = [
    "CFLClient",
    "DEFAULT_LIMIT",
    "DEFAULT_PAGE",
    "DEFAULT_TIMEOUT",
    "CFLAPIError",
    "CFLAPIConnectionError",
    "CFLAPITimeoutError",
    "CFLAPIResponseError",
    "CFLAPINotFoundError",
    "CFLAPIAuthenticationError",
    "CFLAPIValidationError",
    "CFLAPIServerError",
]

__version__ = "0.1.0"
