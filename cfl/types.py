"""Type definitions for the CFL API SDK."""

from datetime import datetime
from typing import TypedDict


# Common types
class Metadata(TypedDict):
    created_at: datetime
    revision_at: datetime
    revision: int


class Location(TypedDict):
    street1: str
    street2: str | None
    city: str
    prov_state: str
    prov_state_text: str | None
    country: str
    country_text: str | None
    postal_code: str


class Genius(TypedDict):
    ID: int
    error: str | None
    messages: list
    last_update: datetime


# Team types
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
    office_location: Location
    clubname: str
    default_venue_id: int
    genius: Genius
    metadata: Metadata


class Venue(TypedDict):
    ID: int
    name: str
    capacity: int
    grey_cup_capacity: int
    time_zone: str
    office_location: Location
    metadata: Metadata


class Season(TypedDict):
    ID: int
    year: int
    preseason_weeks: list[str]
    season_weeks: list[str]
    semi_final_weeks: list[str]
    final_weeks: list[str]
    start_date: str
    end_date: str
    grey_cup_final_week: str
    metadata: Metadata


# Fixture types
class FixtureVenue(TypedDict):
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
    ID: int
    season_id: int
    season_game_count: int
    home_team_id: int
    home_game_count: int
    away_team_id: int
    week: int
    game_type_id: int
    start_at_local: str
    venue_id: int
    start_at: str
    relations: FixtureRelations
    metadata: Metadata


# Roster types
class RosterPlayer(TypedDict):
    ID: int
    player_id: int
    firstname: str
    lastname: str
    jersey_no: int
    birthdate: str
    height_ft: int
    height_in: int
    weight_lbs: int
    college_id: int
    college: str
    position: str
    return_from_injury_date: str | None
    return_to_practice_date: str | None
    state: str
    available_roster: bool
    no_set: bool
    team_id: list[int]
    teams: list[str]
    files: list[dict]
    metadata: Metadata


class Roster(TypedDict):
    ID: int
    team_id: int
    name: str
    rosterplayers: list[RosterPlayer]
    metadata: Metadata


# Ledger types
class LedgerTransaction(TypedDict):
    transaction_id: int
    description: str
    accepted_at: str
    distributed_at: str
    firstname: str
    lastname: str
    position: str
    nationality: str
    college: str
    team_abbr: str
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
    penaltiesChargedDefense: int
    tackles: int
    tacklesSolo: int
    tacklesSpecialTeam: int
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


class PlayerStats(TypedDict):
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
    WEST_DIVISION: list[StandingsStats]
    EAST_DIVISION: list[StandingsStats]
