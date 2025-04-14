"""Constants for the CFL API SDK."""

import random

BASE_API_URL = "https://echo.pims.cfl.ca/api"
BASE_WEB_URL = "https://www.cfl.ca"

# Endpoints
TEAMS_ENDPOINT = "/teams"
TEAM_ENDPOINT = "/teams/{team_id}"
VENUES_ENDPOINT = "/venues"
VENUE_ENDPOINT = "/venues/{venue_id}"
SEASONS_ENDPOINT = "/seasons"
SEASON_ENDPOINT = "/seasons/{season_id}"
FIXTURES_ENDPOINT = "/fixtures"
SEASON_FIXTURES_ENDPOINT = "/seasons/{season_id}/fixtures"
ROSTERS_ENDPOINT = "/rosters"
ROSTER_ENDPOINT = "/rosters/{roster_id}"
LEDGER_ENDPOINT = "/ledger/{year}"
TEAM_STATS_ENDPOINT = "/stats/teams"
TEAM_STAT_ENDPOINT = "/stats/teams/{team_stats_id}"
PLAYER_STATS_ENDPOINT = "/stats/players"
PLAYER_STAT_ENDPOINT = "/stats/players/{player_stats_id}"
PLAYER_PIMS_ENDPOINT = "/stats/players/pims_player/{player_id}"
LEADERBOARD_URL = f"{BASE_WEB_URL}/league-leaders"

# Default parameters
DEFAULT_SEASON = 2024
DEFAULT_LIMIT = 50
DEFAULT_PAGE = 1
DEFAULT_TIMEOUT = 10

MAX_PLAYERS = 5
MIN_SEASON = 2023
MAX_SEASON = 2025


DEFAULT_HEADERS = {
    "Referer": "https://www.cfl.ca/",
    "Accept": "application/json, text/javascript, */*; q=0.01",
}

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
]


def get_random_user_agent() -> str:
    return random.choice(USER_AGENTS)
