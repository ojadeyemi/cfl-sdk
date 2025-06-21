"""Utils for getting leaderboard data"""

from bs4 import BeautifulSoup, Tag

from .constants import MAX_LEADERBOARD_PLAYERS
from .types import _PlayerStat

STAT_CATEGORY_MAPPING = {
    "offence": {
        "PASSING YARDS": "PASSING_YARDS",
        "PASSING TDS": "PASSING_TDS",
        "RUSHING YARDS": "RUSHING_YARDS",
        "RUSHING TDS": "RUSHING_TDS",
        "RECEIVING YARDS": "RECEIVING_YARDS",
        "RECEIVING TDS": "RECEIVING_TDS",
        "RECEPTIONS": "RECEPTIONS",
        "TARGETS": "TARGETS",
    },
    "defence": {
        "TOTAL TACKLES": "TOTAL_TACKLES",
        "SACKS": "SACKS",
        "INTERCEPTIONS": "INTERCEPTIONS",
        "FORCED FUMBLES": "FORCED_FUMBLES",
        "FUMBLE RECOVERIES": "FUMBLE_RECOVERIES",
    },
    "special_teams": {
        "FIELD GOALS": "FIELD_GOALS",
        "PUNTING YARDS (AVERAGE)": "PUNTING_YARDS_AVG",
        "PUNT RETURNS (YARDS)": "PUNT_RETURNS_YARDS",
        "KICKOFF RETURNS (YARDS)": "KICKOFF_RETURNS_YARDS",
        "FIELD GOAL MISSED RETURNS (YARDS)": "FIELD_GOAL_MISS_RETURNS_YARDS",
        "KICKOFFS YARDS (AVERAGE)": "KICKOFFS_YARDS_AVG",
        "KICKS BLOCKED": "KICKS_BLOCKED",
        "TACKLES (SPECIAL TEAMS)": "TACKLES_SPECIAL_TEAMS",
    },
}


DEFAULT_CATEGORIES = {
    "offence": {
        "PASSING_YARDS": [],
        "PASSING_TDS": [],
        "RUSHING_YARDS": [],
        "RUSHING_TDS": [],
        "RECEIVING_YARDS": [],
        "RECEIVING_TDS": [],
        "RECEPTIONS": [],
        "TARGETS": [],
    },
    "defence": {"TOTAL_TACKLES": [], "SACKS": [], "INTERCEPTIONS": [], "FORCED_FUMBLES": [], "FUMBLE_RECOVERIES": []},
    "special_teams": {
        "FIELD_GOALS": [],
        "PUNTING_YARDS_AVG": [],
        "PUNT_RETURNS_YARDS": [],
        "KICKOFF_RETURNS_YARDS": [],
        "FIELD_GOAL_MISS_RETURNS_YARDS": [],
        "KICKOFFS_YARDS_AVG": [],
        "KICKS_BLOCKED": [],
        "TACKLES_SPECIAL_TEAMS": [],
    },
}


def _extract_player_id(player_url: str) -> str:
    if not player_url:
        return ""

    parts = player_url.strip("/").split("/")

    return parts[-1] if len(parts) >= 3 else ""


def _parse_stat_value(value_text: str) -> int | float:
    value_text = value_text.strip()

    # Remove commas from numbers like "5,451"
    value_text = value_text.replace(",", "")

    try:
        return float(value_text) if "." in value_text else int(value_text)

    except ValueError:
        return 0.0 if "." in value_text else 0


def parse_player_table(table_soup, max_players: int = MAX_LEADERBOARD_PLAYERS) -> list[_PlayerStat]:
    players = []
    rows = table_soup.find_all("tr", class_="player-tooltip-wrapper")

    for idx, row in enumerate(rows[:max_players]):
        cells = row.find_all("td")
        if len(cells) < 6:
            continue

        # Use index+1 as rank instead of trying to parse it
        rank = idx + 1

        player_cell = cells[3]
        player_link = player_cell.find("a")

        if player_link:
            player_name = player_link.text.strip()
            player_id = _extract_player_id(player_link.get("href", ""))
        else:
            player_name = player_cell.text.strip()
            player_id = ""

        team_abbv_cell = cells[4]
        value_cell = cells[5]
        team_abbv_text = team_abbv_cell.text.strip()
        value_text = value_cell.text.strip()

        # Look for a cell with class="leaders-stat" if available
        leaders_stat = value_cell.find(class_="leaders-stat")
        if leaders_stat:
            value_text = leaders_stat.text.strip()

        player_stat: _PlayerStat = {
            "rank": rank,
            "player_name": player_name,
            "team_abbreviation": team_abbv_text,
            "value": _parse_stat_value(value_text),
            "player_id": player_id,
            "photo_url": f"https://static.cfl.ca/wp-content/uploads/{player_id}.png",
        }

        players.append(player_stat)

    return players


def parse_leaderboard_category(html_content: str, category: str) -> dict[str, list[_PlayerStat]]:
    soup = BeautifulSoup(html_content, "html.parser")
    tables: list[Tag] = soup.find_all("table")  # type: ignore

    category_results = DEFAULT_CATEGORIES.get(category, {}).copy()
    category_mapping = STAT_CATEGORY_MAPPING.get(category, {})

    for table in tables:
        header = table.find("thead")
        if not header or not header.find("th"):  # type: ignore
            continue

        header_text = header.find("th").text.strip().upper()  # type: ignore

        for key, value in category_mapping.items():
            if header_text == key:
                category_results[value] = parse_player_table(table)
                break

    return category_results
