"""Tests for CFLClient.get_standings (echo.pims.cfl.ca/api/standings)."""

import pytest

from cfl import CFLClient

from .conftest import SEASON

INT_FIELDS = (
    "team_id",
    "place",
    "games_played",
    "wins",
    "losses",
    "ties",
    "points",
    "points_for",
    "points_against",
    "home_wins",
    "away_losses",
    "division_wins",
    "season",
)


def test_returns_all_three_divisions(client: CFLClient):
    standings = client.get_standings(SEASON)

    assert set(standings) == {"week", "east", "west", "unified"}
    assert isinstance(standings["week"], int)
    assert standings["east"] and standings["west"] and standings["unified"]
    # unified is the two divisions combined
    assert len(standings["unified"]) == len(standings["east"]) + len(standings["west"])


def test_rows_are_typed_numbers_not_scrape_strings(client: CFLClient):
    row = client.get_standings(SEASON)["unified"][0]

    for field in INT_FIELDS:
        assert isinstance(row[field], int), field
    assert isinstance(row["winning_percentage"], float)
    assert isinstance(row["abbreviation"], str)
    assert row["season"] == SEASON


def test_rows_are_ordered_by_place(client: CFLClient):
    places = [row["place"] for row in client.get_standings(SEASON)["unified"]]
    assert places == sorted(places)


def test_historic_season_supported(client: CFLClient):
    # ``unified`` only exists from ~2020 on; older seasons still have east/west.
    standings = client.get_standings(2016)
    assert standings["east"] and standings["west"]


@pytest.mark.parametrize("year", [2015, 2027])
def test_out_of_range_year_raises(client: CFLClient, year: int):
    with pytest.raises(ValueError):
        client.get_standings(year)
