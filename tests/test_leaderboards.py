"""Tests for CFLClient.get_leaderboards (api.stats.cfl.ca/stats/leaders)."""

import pytest

from cfl import CFLClient

from .conftest import SEASON

GROUPS = ("offence", "defence", "special_teams")
LEADER_FIELDS = {
    "statValue",
    "player_id",
    "firstname",
    "lastname",
    "position",
    "team_id",
    "image_url",
}


def test_grouped_into_offence_defence_special_teams(client: CFLClient):
    leaders = client.get_leaderboards(SEASON)

    assert set(leaders) == {"availableSeasons", *GROUPS}
    for group in GROUPS:
        assert leaders[group], group
        for category in leaders[group]:
            assert set(category) == {"category", "leaders"}


def test_leader_entries_are_shaped_and_typed(client: CFLClient):
    entry = client.get_leaderboards(SEASON)["offence"][0]["leaders"][0]

    assert set(entry) == LEADER_FIELDS
    assert isinstance(entry["player_id"], int)
    assert isinstance(entry["team_id"], int)
    assert isinstance(entry["statValue"], (int, float))
    assert entry["image_url"].startswith("https://")


def test_count_controls_players_per_category(client: CFLClient):
    leaders = client.get_leaderboards(SEASON, count=5)
    assert all(len(cat["leaders"]) <= 5 for group in GROUPS for cat in leaders[group])


def test_count_is_capped_at_25(client: CFLClient):
    leaders = client.get_leaderboards(2024, count=999)
    assert all(len(cat["leaders"]) <= 25 for group in GROUPS for cat in leaders[group])


@pytest.mark.parametrize("season", [2015, 2027])
def test_out_of_range_season_raises(client: CFLClient, season: int):
    with pytest.raises(ValueError):
        client.get_leaderboards(season)
