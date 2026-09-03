"""Shared fixtures.

These tests hit the live CFL API, so they need network access.
"""

import pytest

from cfl import CFLClient

SEASON = 2026
SEASON_ID = 75  # 2026


def pytest_collection_modifyitems(items):
    """Every test here talks to the live API; tag them all as ``network``."""
    for item in items:
        item.add_marker("network")


@pytest.fixture(scope="session")
def client():
    with CFLClient() as cfl:
        yield cfl
