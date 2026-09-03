"""Constants for the CFL API SDK."""

# Base URLs
BASE_API_URL = "https://echo.pims.cfl.ca/api"
STATS_API_URL = "https://api.stats.cfl.ca"

# API Endpoints (relative to BASE_API_URL)
TEAMS_ENDPOINT = "/teams"
TEAM_ENDPOINT = "/teams/{team_id}"
TEAM_ROSTER_ENDPOINT = "/teams/{team_id}/roster"
VENUES_ENDPOINT = "/venues"
VENUE_ENDPOINT = "/venues/{venue_id}"
PLAYERS_ENDPOINT = "/players"
PLAYER_ENDPOINT = "/players/{player_id}"
PLAYER_LOOKUP_ENDPOINT = "/players/lookup/{pattern}"
PLAYER_POSITIONS_ENDPOINT = "/players/positions"
SEASONS_ENDPOINT = "/seasons"
SEASON_ENDPOINT = "/seasons/{season_id}"
FIXTURES_ENDPOINT = "/fixtures"
FIXTURE_ENDPOINT = "/fixtures/{fixture_id}"
SEASON_FIXTURES_ENDPOINT = "/seasons/{season_id}/fixtures"
ROSTERS_ENDPOINT = "/rosters"
ROSTER_ENDPOINT = "/rosters/{roster_id}"
ROSTERS_SUMMARY_ENDPOINT = "/rosters/summary"
ROSTER_PLAYERS_ENDPOINT = "/rosterplayers"
ROSTER_PLAYER_ENDPOINT = "/rosterplayers/{rosterplayer_id}"
ROSTER_PLAYER_STATES_ENDPOINT = "/rosterplayers/states"
COLLEGES_ENDPOINT = "/colleges"
COLLEGE_ENDPOINT = "/colleges/{college_id}"
LEDGER_ENDPOINT = "/ledger/{year}"
TEAM_STATS_ENDPOINT = "/stats/teamrecords"
TEAM_STAT_ENDPOINT = "/stats/teamrecords/{team_stats_id}"
PLAYER_STATS_ENDPOINT = "/stats/playerrecords"
PLAYER_STAT_ENDPOINT = "/stats/playerrecords/{player_stats_id}"
PLAYER_PIMS_ENDPOINT = "/stats/playerrecords/pims_player/{player_id}"
STANDINGS_ENDPOINT = "/standings/{year}"

# API Endpoints (relative to STATS_API_URL)
LEADERS_ENDPOINT = "/stats/leaders/{year}"

# Request Configuration
DEFAULT_TIMEOUT = 30

# API Parameters
DEFAULT_SEASON = 2026
DEFAULT_LIMIT = 100
DEFAULT_PAGE = 1
MIN_SEASON = 2016
MAX_SEASON = 2026

# League leaders: number of players returned per stat category
DEFAULT_LEADERS_COUNT = 3
MAX_LEADERS_COUNT = 25
