"""Type definitions for the CFL API SDK."""

from datetime import datetime
from typing import NotRequired, TypedDict


class Metadata(TypedDict):
    created_at: datetime
    revision_at: datetime
    revision: int


class Location(TypedDict, total=False):
    street1: str | None
    street2: NotRequired[str | None]
    city: str | None
    prov_state: str | None
    country: str
    postal_code: str | None


class Genius(TypedDict):
    id: int
    error: str | None
    messages: list
    last_update: datetime


class Team(TypedDict):
    ID: int
    name: str
    region_label: str
    abbreviation: str
    team_zone: str
    time_zone: str
    primary_color: str
    accent_color: str
    text_color: str
    team_order: int
    logo_svg: str
    office_location: Location | None
    clubname: str
    default_venue_id: int
    genius: Genius
    metadata: Metadata


class Venue(TypedDict):
    """Type hint for venue info"""

    ID: int
    name: str
    capacity: int
    grey_cup_capacity: int | None
    time_zone: str
    office_location: Location | None
    metadata: Metadata


class Season(TypedDict):
    ID: int
    year: int
    preseason_weeks: list[str]
    season_weeks: list[str]
    semi_final_weeks: list[str]
    final_weeks: list[str]
    start_date: str
    end_date: str | None
    grey_cup_final_week: str | None
    metadata: Metadata


class FixtureVenue(TypedDict, total=False):
    ID: int
    name: str
    capacity: int
    grey_cup_capacity: int
    media_entrance_gate: str | None
    press_box: str
    home_dressing_room: str
    away_dressing_room: str
    radio_station: str
    time_zone: str
    office_location: Location
    ticket_office_location: Location | None
    genius: Genius
    metadata: Metadata


class FixtureRelations(TypedDict):
    venue: FixtureVenue


class Fixture(TypedDict):
    """Fixture (Games) in  a season"""

    ID: int
    season_id: int
    season_game_count: int | None
    home_team_id: int | None
    home_game_count: int | None
    away_team_id: int | None
    week: int
    game_type_id: int
    start_at_local: str
    venue_id: int
    start_at: str
    relations: FixtureRelations
    metadata: Metadata


class RosterPlayer(TypedDict):
    ID: int
    player_id: int
    firstname: str
    lastname: str
    jersey_no: int | None
    birthdate: str
    height_ft: int | None
    height_in: int | None
    weight_lbs: int | None
    college_id: int | None
    college: str
    position: str
    return_from_injury_date: str | None
    return_to_practice_date: str | None
    state: str
    available_roster: bool
    no_set: bool
    team_id: list[int]
    teams: list[str]
    files: list
    metadata: Metadata


class Roster(TypedDict):
    """Type hint for player roster for a specific team"""

    ID: int
    team_id: int
    name: str
    rosterplayers: list[RosterPlayer]
    metadata: Metadata


class LedgerTransaction(TypedDict):
    """Type hint for ledger transactions"""

    transaction_id: int
    description: str
    accepted_at: str
    distributed_at: str
    firstname: str
    lastname: str
    position: str
    nationality: str
    college: str
    team_abbr: str | None
    action: str
    is_distributed: bool
    player_id: int
    resource_type: str
    state_change: str
    previous_state: str


# Stats types
class SeasonTeamStats(TypedDict):
    season_id: int
    season: int
    team_id: int
    team_abbreviation: str
    opponent_team_id: int
    opponent_team_abbreviation: str
    drives: int
    firstDowns: int
    passesAttempted: int
    passesCompleted: int
    passesYards: int
    passesTouchdowns: int
    rushes: int
    rushesYards: int
    rushesTouchdowns: int
    penalties: int
    penaltiesYards: int
    turnovers: int
    fumblesLost: int
    interceptions: int
    thirdDownConversions: int
    thirdDownAttempts: int
    fourthDownConversions: int
    fourthDownAttempts: int
    redZoneAppearances: int
    redZoneTouchdowns: int
    sacks: int
    sacksYards: int
    pointsScored: int
    timeOfPossession: str


class FixtureTeamStats(TypedDict):
    driveGoalToGoAttempted: int
    driveGoalToGoSuccessful: int
    firstDowns: int
    firstDownsByRush: int
    firstDownsByPass: int
    passesAttempted: int
    passesCompleted: int
    passesYards: int
    passesTouchdowns: int
    rushes: int
    rushesYards: int
    rushesTouchdowns: int
    penalties: int
    penaltiesYards: int
    turnovers: int
    fumblesLost: int
    interceptions: int
    thirdDownConversions: int
    thirdDownAttempts: int
    fourthDownConversions: int
    fourthDownAttempts: int
    redZoneAppearances: int
    redZoneTouchdowns: int
    sacks: int
    sacksYards: int
    pointsScored: int
    timeOfPossession: str


class FixtureTeamStatsWrapper(TypedDict):
    fixture_id: int
    genius_id: int
    season: int
    season_id: int
    week: int
    start_at: str
    stats: FixtureTeamStats


class TeamStats(TypedDict):
    ID: int
    seasons: list[SeasonTeamStats]
    fixtures: list[FixtureTeamStatsWrapper]


# Player stats types
class SeasonPlayerStats(TypedDict):
    season_id: int
    season: int
    hasParticipated: int
    team_id: int
    team_abbreviation: str
    opponent_team_id: int
    opponent_team_abbreviation: str
    penaltiesChargedDefense: int
    tackles: int
    tacklesSpecialTeam: int
    wasStarter: int
    tacklesSolo: int


class FixturePlayerStats(TypedDict):
    hasParticipated: bool
    wasStarter: bool


class FixturePlayerStatsWrapper(TypedDict):
    fixture_id: int
    genius_id: int
    season: int
    season_id: int
    week: int
    start_at: str
    stats: FixturePlayerStats
    team_id: int
    team_abbreviation: str
    opponent_team_id: int
    opponent_team_abbreviation: str


class PlayerStats(TypedDict, total=False):
    ID: int
    seasons: list[SeasonPlayerStats]
    fixtures: list[FixturePlayerStatsWrapper]
    last_game_id: int
    player_id: int
    rosterplayer_id: int
    firstname: str
    lastname: str
    team_id: int
    team: str
    position: str
    metadata: Metadata


class ErrorResponse(TypedDict):
    error: str
    message: str
    status_code: int


class StandingsStats(TypedDict):
    RK: str
    TEAM: str
    GP: str
    W: str
    L: str
    T: str
    PTS: str
    F: str
    A: str
    HOME: str
    AWAY: str
    DIV: str


class Standings(TypedDict):
    """Type hint for standings"""

    WEST_DIVISION: list[StandingsStats]
    EAST_DIVISION: list[StandingsStats]
