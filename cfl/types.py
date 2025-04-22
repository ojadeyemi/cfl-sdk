"""Type definitions for the CFL API SDK."""

from datetime import datetime
from typing import Literal, NotRequired, Required, TypedDict


class Metadata(TypedDict):
    created_at: datetime
    revision_at: datetime
    revision: int


class Location(TypedDict, total=False):
    street1: str | None
    street2: str | None
    city: str | None
    prov_state: str | None
    country: str
    postal_code: str | None


class Genius(TypedDict, total=False):
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
    """Important dates for specific season"""

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
    press_box: str | None
    home_dressing_room: str | None
    away_dressing_room: str | None
    radio_station: str | None
    time_zone: str
    office_location: Location
    ticket_office_location: Location | None
    genius: Genius
    metadata: Metadata


class FixtureRelations(TypedDict):
    venue: FixtureVenue


class Fixture(TypedDict, total=False):
    """Fixture (Games) in  a season"""

    ID: int
    season_id: int
    season_game_count: int | None
    home_team_id: int | None
    home_team_score: int | None
    home_game_count: int | None
    away_team_id: int | None
    away_team_score: int | None
    week: int
    game_type_id: int
    game_clock: str | None
    start_at: str
    start_at_local: str
    venue_id: int
    start_at: str
    broadcasting_options: list[str] | None
    relations: FixtureRelations
    metadata: Metadata
    genius: Genius


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


class BaseTeamStats(TypedDict, total=False):
    defensiveExtraPointsBlocked: int | None
    driveGoalToGoSucceeded: int | None
    driveGoalToGoAttempted: int | None
    driveInsideTwentyAttempted: int | None
    driveInsideTwentySucceeded: int | None
    driveInsideTwentySucceededPercentage: float | None
    drives: int | None
    extraPointsAttempted: int | None
    extraPointsSucceeded: int | None
    fieldGoalsAttempted: int | None
    fieldGoalsAverageYards: float | None
    fieldGoalsMissed: int | None
    fieldGoalsMissedReturns: int | None
    fieldGoalsMissedReturnsYards: int | None
    fieldGoalsMissedReturnsYardsAverage: float | None
    fieldGoalsMissedReturnsYardsLongest: int | None
    fieldGoalsSucceeded: int | None
    fieldGoalsSucceededPercentage: float | None
    fieldGoalsSucceededYardsLongest: int | None
    fieldGoalsYards: int | None
    firstDowns: int | None
    firstDownsAttempted: int | None
    firstDownsByPass: int | None
    firstDownsByPenalties: int | None
    firstDownsByRush: int | None
    firstDownsConversions: int | None
    firstDownsConversionsPercentage: float | None
    firstDownsPenalties: int | None
    firstDownsYards: int | None
    firstDownsYardsAverage: float | None
    fourthDownAttempts: int | None
    fourthDownConversions: int | None
    fumbles: int | None
    fumblesForced: int | None
    fumblesLost: int | None
    fumblesOutOfBounds: int | None
    fumblesRecoveries: int | None
    fumblesRecoveriesFromOpponents: int | None
    fumblesRecoveriesOwn: int | None
    fumblesRecoveriesOwnYards: int | None
    fumblesReturnsYards: int | None
    fumblesReturnsYardsLongest: int | None
    interceptions: int | None
    interceptionsReturns: int | None
    interceptionsReturnsYards: int | None
    interceptionsReturnsYardsLongest: int | None
    kickoffs: int | None
    kickoffsInsideEndZone: int | None
    kickoffsInsideTwenty: int | None
    kickoffsKickerReturnsYards: int | None
    kickoffsOutOfBounds: int | None
    kickoffsReturns: int | None
    kickoffsReturnsYards: int | None
    kickoffsReturnsYardsAverage: float | None
    kickoffsReturnsYardsLongest: int | None
    kickoffsYards: int | None
    kickoffsYardsAverage: float | None
    kickoffsYardsLongest: int | None
    kneels: int | None
    kneelsYards: int | None
    largestLead: int | None
    losses: int | None
    lossesYards: int | None
    offenseYards: int | None
    passesAttempted: int | None
    passesAttemptedYardsAverage: float | None
    passesCompleted: int | None
    passesIntercepted: int | None
    passesRating: float | None
    passesSacked: int | None
    passesSackedFirstDown: int | None
    passesSackedLostYards: int | None
    passesSackedSecondDown: int | None
    passesSackedThirdDown: int | None
    passesSucceededPercentage: float | None
    passesSucceededThirtyPlusYards: int | None
    passesSucceededYardsAverage: float | None
    passesSucceededYardsLongest: int | None
    passesTouchdowns: int | None
    passesYards: int | None
    penalties: int | None
    penaltiesDeclined: int | None
    penaltiesYards: int | None
    playYardsAverage: float | None
    plays: int | None
    pointsAllowed: int | None
    pointsAllowedFirstQuarter: int | None
    pointsAllowedFourthQuarter: int | None
    pointsAllowedOvertime: int | None
    pointsAllowedSecondQuarter: int | None
    pointsAllowedThirdQuarter: int | None
    pointsScored: int | None
    pointsScoredFirstQuarter: int | None
    pointsScoredFourthQuarter: int | None
    pointsScoredSecondQuarter: int | None
    pointsScoredThirdQuarter: int | None
    pointsScoredOvertime: int | None
    puntingInsideTen: int | None
    puntingInsideTwenty: int | None
    puntingKickerReturnsYards: int | None
    puntingReturnsYards: int | None
    puntingReturnsYardsAverage: float | None
    puntingReturnsYardsLongest: int | None
    puntingYards: int | None
    puntingYardsGrossAverage: float | None
    puntingYardsLongest: int | None
    puntingYardsNet: int | None
    puntingYardsNetAverage: float | None
    punts: int | None
    puntsBlocked: int | None
    puntsReturns: int | None
    receptions: int | None
    receptionsSecondDownForFirstDown: int | None
    receptionsThirtyPlusYards: int | None
    receptionsYards: int | None
    receptionsYardsAverage: float | None
    receptionsYardsLongest: int | None
    redZoneAppearances: int | None
    redZoneTouchdowns: int | None
    returnsYards: int | None
    rushes: int | None
    rushesAttemptedInsideTwenty: int | None
    rushesSucceededInsideTwenty: int | None
    rushesTenPlusYards: int | None
    rushesTouchdowns: int | None
    rushesTwentyPlusYards: int | None
    rushesYards: int | None
    rushingTacklesForLoss: int | None
    rushingTacklesForLossYards: int | None
    rushingYardsAverage: float | None
    rushingYardsLongest: int | None
    safeties: int | None
    sacks: int | None
    sacksForLossYards: int | None
    sacksYards: int | None
    secondDownsAttempted: int | None
    secondDownsConversions: int | None
    secondDownsConversionsPercentage: float | None
    secondDownsFourToSixYardsAttempted: int | None
    secondDownsFourToSixYardsConversions: int | None
    secondDownsFourToSixYardsConversionsPercentage: float | None
    secondDownsOneToThreeYardsAttempted: int | None
    secondDownsOneToThreeYardsConversions: int | None
    secondDownsOneToThreeYardsConversionsPercentage: float | None
    secondDownsSevenPlusYardsAttempted: int | None
    secondDownsSevenPlusYardsConversions: int | None
    secondDownsSevenPlusYardsConversionsPercentage: float | None
    secondDownsYards: int | None
    secondDownsYardsAverage: float | None
    singles: int | None
    singlesFieldGoals: int | None
    singlesKickoffs: int | None
    singlesPunts: int | None
    tackles: int | None
    tacklesForLoss: int | None
    tacklesForLossYards: int | None
    tacklesSolo: int | None
    tacklesSpecialTeam: int | None
    thirdDownAttempts: int | None
    thirdDownConversions: int | None
    thirdDownsConversionsPercentage: float | None
    thirdDownsYards: int | None
    thirdDownsYardsAverage: float | None
    timeOfPossession: str | None
    timeOfPossessionSeconds: int | None
    touchdowns: int | None
    touchdownsFieldGoalsReturns: int | None
    touchdownsFumblesOwnRecovery: int | None
    touchdownsFumblesReturn: int | None
    touchdownsInterceptionsReturns: int | None
    touchdownsInterceptionsReturnsYardsLongest: int | None
    touchdownsKickoffsOwnRecovery: int | None
    touchdownsKickoffsReturns: int | None
    touchdownsKickoffsReturnsYardsLongest: int | None
    touchdownsPassesYardsLongest: int | None
    touchdownsPuntingOwnRecovery: int | None
    touchdownsPuntingReturns: int | None
    touchdownsPuntingReturnsYardsLongest: int | None
    touchdownsReceptions: int | None
    touchdownsReceptionsYardsLongest: int | None
    touchdownsReturns: int | None
    touchdownsRushing: int | None
    touchdownsRushingYardsLongest: int | None
    turnovers: int | None
    turnoversOnDowns: int | None
    twoPointConversionsDefense: int | None
    twoPointDefensiveConversionsAttempted: int | None
    twoPointDefensiveConversionsSucceeded: int | None
    twoPointPassAttempted: int | None
    twoPointPassSucceeded: int | None
    twoPointReceptionAttempted: int | None
    twoPointReceptionSucceeded: int | None
    twoPointRushAttempted: int | None
    twoPointRushSucceeded: int | None
    yardsAfterCatch: int


class SeasonTeamStats(BaseTeamStats, total=False):
    season: Required[int]
    season_id: Required[int]
    team_id: Required[int]
    team_abbreviation: str
    opponent_team_abbreviation: str
    opponent_team_id: int


class FixtureTeamStats(BaseTeamStats, total=False):
    driveGoalToGoSuccessful: int
    extraPointsBlocked: int
    fieldGoalsBlocked: int


class FixtureTeamStatsWrapper(TypedDict, total=False):
    fixture_id: Required[int]
    genius_id: int
    season: int
    season_id: Required[int]
    week: int
    start_at: str
    stats: FixtureTeamStats


class TeamStats(TypedDict, total=False):
    """Team statistics"""

    ID: int
    abbreviation: str
    last_game_id: int | None
    name: str
    region_label: str
    team_id: int
    seasons: list[SeasonTeamStats]
    fixtures: NotRequired[list[FixtureTeamStatsWrapper]]
    metadata: Metadata


class BasePlayerStats(TypedDict, total=False):
    fieldGoalsMissedReturns: int | None
    fieldGoalsMissedReturnsYards: int | None
    fumbles: int | None
    fumblesForced: int | None
    fumblesRecoveries: int | None
    fumblesRecoveriesOwn: int | None
    kickoffs: int | None
    kickoffsInsideEndZone: int | None
    kickoffsInsideTwenty: int | None
    kickoffsKickerReturnsYards: int | None
    kickoffsOutOfBounds: int | None
    kickoffsReturns: int | None
    kickoffsReturnsYards: int | None
    kickoffsReturnsYardsLongest: int | None
    kickoffsYards: int | None
    kickoffsYardsAverage: int | None
    kickoffsYardsLongest: int | None
    passesAttempted: int | None
    passesDefended: int | None
    passesIntercepted: int | None
    passesRating: float | None
    passesSucceeded: int | None
    passesSucceededPercentage: float | None
    passesSucceededYards: int | None
    passesSucceededYardsLongest: int | None
    passesTargetedAt: int | None
    penaltiesChargedDefense: int | None
    penaltiesChargedOffense: int | None
    pointsScored: int | None
    pointsScoredFirstQuarter: int | None
    pointsScoredFourthQuarter: int | None
    pointsScoredThirdQuarter: int | None
    puntingInsideTen: int | None
    puntingInsideTwenty: int | None
    puntingKickerReturnsYards: int | None
    puntingReturnsYards: int | None
    puntingReturnsYardsLongest: int | None
    puntingYards: int | None
    puntingYardsGrossAverage: float | None
    puntingYardsNet: int | float | None
    punts: int | None
    puntsReturns: int | None
    receptions: int | None
    receptionsYards: int | None
    receptionsYardsLongest: int | None
    rushes: int | None
    rushingYards: int | None
    rushingYardsLongest: int | None
    sacks: int | None
    singles: int | None
    singlesKickoffs: int | None
    singlesPunts: int | None
    tackles: int | None
    tacklesForLoss: int | None
    tacklesSolo: int | None
    tacklesSpecialTeam: int | None
    touchdownsPasses: int | None
    touchdownsReceptions: int | None
    touchdownsReceptionsYardsLongest: int | None
    touchdownsRushing: int | None
    touchdownsRushingYardsLongest: int | None
    yardsAfterCatch: int | None


class SeasonPlayerStats(BasePlayerStats):
    hasParticipated: int
    opponent_team_abbreviation: str
    opponent_team_id: int
    season: int
    season_id: int
    team_abbreviation: str
    team_id: int
    wasStarter: int


class FixturePlayerStats(BasePlayerStats):
    hasParticipated: bool
    wasStarter: bool


class FixturePlayerStatsWrapper(TypedDict, total=False):
    fixture_id: Required[int]
    genius_id: int
    season: int
    season_id: Required[int]
    week: int
    start_at: str
    stats: FixturePlayerStats
    team_id: Required[int]
    team_abbreviation: str
    opponent_team_id: Required[int]
    opponent_team_abbreviation: str


class PlayerStats(TypedDict, total=False):
    """Player statistics"""

    ID: int
    seasons: list[SeasonPlayerStats]
    fixtures: list[FixturePlayerStatsWrapper]
    last_game_id: int
    player_id: Required[int]
    photo_url: str
    rosterplayer_id: int
    firstname: str
    lastname: str
    team_id: int | None
    team: str | None
    position: str | None
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


class _PlayerStat(TypedDict):
    """Individual player statistic entry"""

    rank: int
    player_id: str
    player_name: str
    team_abbreviation: str
    value: int | float
    photo_url: str


StatCategory = Literal["offence", "defence", "special_teams"]


class OffenceLeaders(TypedDict):
    """Offensive statistics categories"""

    PASSING_YARDS: list[_PlayerStat]
    PASSING_TDS: list[_PlayerStat]
    RUSHING_YARDS: list[_PlayerStat]
    RUSHING_TDS: list[_PlayerStat]
    RECEIVING_YARDS: list[_PlayerStat]
    RECEIVING_TDS: list[_PlayerStat]
    RECEPTIONS: list[_PlayerStat]
    TARGETS: list[_PlayerStat]


class DefenceLeaders(TypedDict):
    """Defensive statistics categories"""

    TOTAL_TACKLES: list[_PlayerStat]
    SACKS: list[_PlayerStat]
    INTERCEPTIONS: list[_PlayerStat]
    FORCED_FUMBLES: list[_PlayerStat]
    FUMBLE_RECOVERIES: list[_PlayerStat]


class SpecialTeamsLeaders(TypedDict):
    """Special teams statistics categories"""

    FIELD_GOALS: list[_PlayerStat]
    PUNTING_YARDS_AVG: list[_PlayerStat]
    PUNT_RETURNS_YARDS: list[_PlayerStat]
    KICKOFF_RETURNS_YARDS: list[_PlayerStat]
    FIELD_GOAL_MISS_RETURNS_YARDS: list[_PlayerStat]
    KICKOFFS_YARDS_AVG: list[_PlayerStat]
    KICKS_BLOCKED: list[_PlayerStat]
    TACKLES_SPECIAL_TEAMS: list[_PlayerStat]


class LeagueLeaders(TypedDict):
    """Complete league leaders data structure"""

    offence: OffenceLeaders
    defence: DefenceLeaders
    special_teams: SpecialTeamsLeaders
