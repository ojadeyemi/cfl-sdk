"""Smoke test: every public CFLClient method returns data against the live API."""

import pytest

from cfl import CFLClient

from .conftest import SEASON, SEASON_ID


def _dict(value) -> bool:
    return isinstance(value, dict) and bool(value)


def _list(value) -> bool:
    return isinstance(value, list) and bool(value)


# name -> (call, predicate the result must satisfy)
CASES = {
    "get_teams": (lambda c: c.get_teams(), _list),
    "get_team": (lambda c: c.get_team(1), _dict),
    "get_team_roster": (lambda c: c.get_team_roster(1), _dict),
    "get_venues": (lambda c: c.get_venues(), _list),
    "get_venue": (lambda c: c.get_venue(1), _dict),
    "get_players": (lambda c: c.get_players(position="QB", limit=5), _list),
    "get_player": (lambda c: c.get_player(183186), _dict),
    "search_players": (lambda c: c.search_players("mitchell"), _list),
    "get_player_positions": (lambda c: c.get_player_positions(), _list),
    "get_seasons": (lambda c: c.get_seasons(limit=5), _list),
    "get_season": (lambda c: c.get_season(SEASON_ID), _dict),
    "get_fixtures": (lambda c: c.get_fixtures(season_id=SEASON_ID, limit=5), _list),
    "get_fixture": (lambda c: c.get_fixture(6555), _dict),
    "get_rosters": (lambda c: c.get_rosters(), _list),
    "get_roster": (lambda c: c.get_roster(1), _dict),
    "get_rosters_summary": (lambda c: c.get_rosters_summary(), _list),
    "get_roster_players": (lambda c: c.get_roster_players(limit=5), _list),
    "get_roster_player": (lambda c: c.get_roster_player(26733), _dict),
    "get_roster_player_states": (lambda c: c.get_roster_player_states(), _list),
    "get_ledger": (lambda c: c.get_ledger(SEASON), _list),
    "get_colleges": (lambda c: c.get_colleges(limit=5), _list),
    "get_college": (lambda c: c.get_college(295), _dict),
    "get_team_stats": (lambda c: c.get_team_stats(season_id=SEASON_ID), _list),
    "get_player_stats": (
        lambda c: c.get_player_stats(season_id=SEASON_ID, limit=5),
        _list,
    ),
    "get_player_pims": (lambda c: c.get_player_pims(168507), _dict),
    "get_standings": (lambda c: c.get_standings(SEASON), _dict),
    "get_leaderboards": (lambda c: c.get_leaderboards(SEASON), _dict),
}


@pytest.mark.parametrize("name", list(CASES))
def test_method_returns_data(client: CFLClient, name: str):
    call, predicate = CASES[name]
    assert predicate(call(client))
