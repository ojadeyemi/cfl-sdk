# 🏈 CFL SDK

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

A modern Python SDK for the **[Canadian Football League](https://www.cfl.ca/)** API using httpx.

[Features](#features) · [Installation](#installation) · [Quick Start](#quick-start) · [API Reference](#api-reference) · [Built with CFL SDK](#built-with-cfl-sdk) · [Contributing](#contributing)


---

## Features

- Full type hints using modern Python typing
- Comprehensive API coverage (most endpoints supported)
- Error handling and logging

## Installation

```bash
pip install cfl-sdk
```

### With Poetry

```bash
poetry add cfl-sdk
```

## Quick Start

```python
from cfl import CFLClient

client = CFLClient()

# Get all teams
teams = client.get_teams()
for team in teams:
    print(f"{team['name']} ({team['abbreviation']})")

# Get fixtures for a season
fixtures = client.get_fixtures(season_id=35)  # 2026 season

# Get players filtered by position
qbs = client.get_players(position="QB", limit=20)
```

## API Reference

[Teams](#teams) · [Venues](#venues) · [Players](#players) · [Seasons](#seasons) · [Fixtures](#fixtures-games) · [Rosters](#rosters) · [Roster Players](#roster-players) · [Colleges](#colleges) · [Ledger](#ledger-transactions) · [Team Stats](#team-stats) · [Player Stats](#player-stats) · [Standings](#standings) · [Leaderboard](#leaderboard)

---

### Teams

```python
# Get all teams
teams = client.get_teams()

# Get a specific team
team = client.get_team(team_id=1)

# Get a team's full current roster
roster = client.get_team_roster(team_id=1)
```

### Venues

```python
# Get all venues
venues = client.get_venues()

# Get specific venue
venue = client.get_venue(venue_id=1)
```

### Players

```python
# Get players (filterable)
players = client.get_players(limit=50)
players = client.get_players(position="QB")
players = client.get_players(college_id=295)
players = client.get_players(sort_by="lastname", sort_order="asc", page=2, limit=25)

# Get a specific player
player = client.get_player(player_id=183186)

# Embed college details in the response
player = client.get_player(player_id=183186, with_college=True)
# player["relations"]["college"] -> college object

# Search players by name pattern
results = client.search_players("mitchell")  # returns [{ID, name}, ...]

# Get all position definitions
positions = client.get_player_positions()
```

### Seasons

```python
# Get all seasons (with optional pagination)
seasons = client.get_seasons(page=1, limit=50)

# Get specific season
season = client.get_season(season_id=35)  # 2026 season
```

### Fixtures (Games)

```python
# Get fixtures (with optional filters and pagination)
fixtures = client.get_fixtures(limit=50)
fixtures = client.get_fixtures(season_id=35)  # 2026 season
fixtures = client.get_fixtures(home_team_id=1)
fixtures = client.get_fixtures(away_team_id=1)
fixtures = client.get_fixtures(venue_id=1)

# Get a specific fixture
fixture = client.get_fixture(fixture_id=6555)

# Embed related objects
fixture = client.get_fixture(fixture_id=6555, with_venue=True)
fixture = client.get_fixture(fixture_id=6555, with_season=True)
# fixture["relations"]["venue"] -> venue object
```

### Rosters

```python
# Get all rosters
rosters = client.get_rosters()

# Get specific roster
roster = client.get_roster(roster_id=1)

# Get per-team roster state and nationality counts
summary = client.get_rosters_summary()
```

### Roster Players

```python
# Get all roster player entries
roster_players = client.get_roster_players(limit=50)

# Filter to a specific player's entry
entries = client.get_roster_players(player_id=183186)

# Embed full player object
entries = client.get_roster_players(with_player=True, limit=25)
# entries[0]["relations"]["player"] -> full player object

# Get a specific roster player entry
rp = client.get_roster_player(rosterplayer_id=26733)
rp = client.get_roster_player(rosterplayer_id=26733, with_player=True)

# Get all valid roster states
states = client.get_roster_player_states()
```

### Colleges

```python
# Get all colleges
colleges = client.get_colleges(limit=50)

# Filter by name
colleges = client.get_colleges(name="laval")

# Sort and paginate
colleges = client.get_colleges(sort_by="name", sort_order="asc", page=1, limit=25)

# Get a specific college
college = client.get_college(college_id=295)
```

### Ledger (Transactions)

```python
# Get transactions for a year
transactions = client.get_ledger(year=2026)
```

### Team Stats

```python
# Get team stats
team_stats = client.get_team_stats()

# Get team stats for a season
team_stats = client.get_team_stats(season_id=35)  # 2026 season

# Get specific team stats
team_stat = client.get_team_stat(team_stats_id=122345)
```

### Player Stats

```python
# Get player stats (with optional pagination and season filter)
player_stats = client.get_player_stats(season_id=35, page=1, limit=50)

# Get specific player stats
player_stat = client.get_player_stat(player_stats_id=1629968)

# Get player stats with photo URL
player_stat = client.get_player_pims(player_id=168507)
```

### Standings

```python
# Get standings for a year (2023-2026 supported)
standings = client.get_standings(year=2026)
```

### Leaderboard

```python
# Get player leaderboard for different stats for a year (2023-2026 supported)
leaderboard = client.get_leaderboards(season=2024)
```

## Error Handling

The SDK provides specific error types:

- `CFLAPIConnectionError`: For connection issues
- `CFLAPITimeoutError`: For request timeouts
- `CFLAPINotFoundError`: For 404 responses
- `CFLAPIAuthenticationError`: For auth issues
- `CFLAPIValidationError`: For invalid requests
- `CFLAPIServerError`: For server errors

```python
from cfl import CFLClient, CFLAPINotFoundError

client = CFLClient()

try:
    team = client.get_team(team_id=999999)
except CFLAPINotFoundError:
    print("Team not found")
```

## Using with Context Manager

```python
with CFLClient() as client:
    teams = client.get_teams()
    # Client will be closed automatically
```

## Acknowledgements & Disclaimer

Thank you to the **[Canadian Football League (CFL)](https://www.cfl.ca/)** for providing a public API.

This is an unofficial SDK and is not affiliated with, endorsed, or sponsored by the Canadian Football League (CFL).

## Built with CFL SDK

Using this SDK in a project? Open a PR to add it here!

| Project | Description |
|---------|-------------|
| *Your project here* | [Open a PR](https://github.com/ojadeyemi/cfl-sdk/pulls) to add yours |

## Contributing

Contributions are welcome! Please feel free to submit a pull request or [open an issue](https://github.com/ojadeyemi/cfl-sdk/issues) for any bugs or feature requests.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.
