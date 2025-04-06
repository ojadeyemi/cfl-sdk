"""Constants for the CFL API SDK."""

BASE_URL = "https://echo.pims.cfl.ca/api"

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

# Default parameters
DEFAULT_SEASON = 2024
DEFAULT_LIMIT = 100
DEFAULT_PAGE = 1
DEFAULT_TIMEOUT = 10
