# 🏈 CFL SDK

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

A modern Python SDK for the CFL (Canadian Football League) API using httpx.

## Features

- Full type hints using modern Python typing
- Complete API coverage
- Pagination handling built-in
- Error handling and logging

## Installation

```bash
pip install git+https://github.com/ojadeyemi/cfl-sdk.git
```

## Quick Start

```python
from cfl import CFLClient

# Create client
client = CFLClient()

# Get teams
teams = client.get_teams()
for team in teams:
    print(f"{team['name']} ({team['abbreviation']})")

# Get fixtures for a season
fixtures = client.get_fixtures(season_id=123)

# Get player stats
player_stats = client.get_player_stats(season_id=123)
```

## API Reference

### Teams

```python
# Get all teams
teams = client.get_teams()

# Get a specific team
team = client.get_team(team_id=1)
```

### Venues

```python
# Get all venues
venues = client.get_venues()

# Get specific venue
venue = client.get_venue(venue_id=123)
```

### Seasons

```python
# Get all seasons
seasons = client.get_seasons()

# Get specific season
season = client.get_season(season_id=123)
```

### Fixtures (Games)

```python
# Get all fixtures
fixtures = client.get_fixtures()

# Get fixtures for a season
fixtures = client.get_fixtures(season_id=123)
```

### Rosters

```python
# Get all rosters
rosters = client.get_rosters()

# Get specific roster
roster = client.get_roster(roster_id=1)
```

### Ledger (Transactions)

```python
# Get transactions for a year
transactions = client.get_ledger(year=2024)
```

### Team Stats

```python
# Get team stats
team_stats = client.get_team_stats()

# Get team stats for a season
team_stats = client.get_team_stats(season_id=123)

# Get specific team stats
team_stat = client.get_team_stat(team_stats_id=123)
```

### Player Stats

```python
# Get player stats
player_stats = client.get_player_stats()

# Get specific player stats
player_stat = client.get_player_stat(player_stats_id=123)

player_stat = client.get_player_pims(player_id=123)
```

### Standings

```python
# Get standings for a year
standings = client.get_standings(season=2024)
```

### Leaderboard

```python
# Get player leaderboard for differnet stats for a year
leaderboard = client.get_leadeboards(season=2024)
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
from cfl_sdk import CFLClient, CFLAPINotFoundError

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

## Acknowledgements

**This SDK is made possible by the [Canadian Football League (CFL)](https://www.cfl.ca/) providing a public API. A big thank you to the CFL for making their data accessible to developers and fans.**

## Disclaimer

This is an unofficial SDK and is not affiliated with, endorsed, or sponsored by the Canadian Football League (CFL).

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
