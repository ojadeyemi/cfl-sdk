"""Type definitions for the CFL API SDK."""

from datetime import datetime
from typing import Literal, NotRequired, Required, TypedDict


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


class Fixture(TypedDict, total=False):
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
class BaseTeamStats(TypedDict, total=False):
    driveGoalToGoAttempted: int
    driveInsideTwentyAttempted: int
    driveInsideTwentySucceeded: int
    driveInsideTwentySucceededPercentage: float
    drives: int
    extraPointsAttempted: int
    extraPointsSucceeded: int
    fieldGoalsAttempted: int
    fieldGoalsAverageYards: float
    fieldGoalsMissed: int
    fieldGoalsMissedReturns: int
    fieldGoalsMissedReturnsYards: int
    fieldGoalsMissedReturnsYardsAverage: float
    fieldGoalsMissedReturnsYardsLongest: int
    fieldGoalsSucceeded: int
    fieldGoalsSucceededPercentage: float
    fieldGoalsSucceededYardsLongest: int
    fieldGoalsYards: int
    firstDowns: int
    firstDownsAttempted: int
    firstDownsByPass: int
    firstDownsByPenalties: int
    firstDownsByRush: int
    firstDownsConversions: int
    firstDownsConversionsPercentage: float
    firstDownsPenalties: int
    firstDownsYards: int
    firstDownsYardsAverage: float
    fourthDownAttempts: int
    fourthDownConversions: int
    fumbles: int
    fumblesForced: int
    fumblesLost: int
    fumblesOutOfBounds: int
    fumblesRecoveries: int
    fumblesRecoveriesFromOpponents: int
    fumblesRecoveriesOwn: int
    fumblesRecoveriesOwnYards: int
    fumblesReturnsYards: int
    fumblesReturnsYardsLongest: int
    interceptions: int
    interceptionsReturns: int
    interceptionsReturnsYards: int
    interceptionsReturnsYardsLongest: int
    kickoffs: int
    kickoffsInsideEndZone: int
    kickoffsInsideTwenty: int
    kickoffsKickerReturnsYards: int
    kickoffsOutOfBounds: int
    kickoffsReturns: int
    kickoffsReturnsYards: int
    kickoffsReturnsYardsAverage: float
    kickoffsReturnsYardsLongest: int
    kickoffsYards: int
    kickoffsYardsAverage: float
    kickoffsYardsLongest: int
    kneels: int
    kneelsYards: int
    largestLead: int
    losses: int
    lossesYards: int
    offenseYards: int
    passesAttempted: int
    passesAttemptedYardsAverage: float
    passesCompleted: int
    passesIntercepted: int
    passesRating: float
    passesSacked: int
    passesSackedFirstDown: int
    passesSackedLostYards: int
    passesSackedSecondDown: int
    passesSucceededPercentage: float
    passesSucceededThirtyPlusYards: int
    passesSucceededYardsAverage: float
    passesSucceededYardsLongest: int
    passesTouchdowns: int
    passesYards: int
    penalties: int
    penaltiesDeclined: int
    penaltiesYards: int
    playYardsAverage: float
    plays: int
    pointsAllowed: int
    pointsAllowedFirstQuarter: int
    pointsAllowedFourthQuarter: int
    pointsAllowedOvertime: int
    pointsAllowedSecondQuarter: int
    pointsAllowedThirdQuarter: int
    pointsScored: int
    pointsScoredFirstQuarter: int
    pointsScoredFourthQuarter: int
    pointsScoredSecondQuarter: int
    pointsScoredThirdQuarter: int
    puntingInsideTen: int
    puntingInsideTwenty: int
    puntingKickerReturnsYards: int
    puntingReturnsYards: int
    puntingReturnsYardsAverage: float
    puntingReturnsYardsLongest: int
    puntingYards: int
    puntingYardsGrossAverage: float
    puntingYardsLongest: int
    puntingYardsNet: int
    puntingYardsNetAverage: float
    punts: int
    puntsReturns: int
    receptions: int
    receptionsSecondDownForFirstDown: int
    receptionsThirtyPlusYards: int
    receptionsYards: int
    receptionsYardsAverage: float
    receptionsYardsLongest: int
    redZoneAppearances: int
    redZoneTouchdowns: int
    returnsYards: int
    rushes: int
    rushesAttemptedInsideTwenty: int
    rushesSucceededInsideTwenty: int
    rushesTenPlusYards: int
    rushesTouchdowns: int
    rushesTwentyPlusYards: int
    rushesYards: int
    rushingTacklesForLoss: int
    rushingTacklesForLossYards: int
    rushingYardsAverage: float
    rushingYardsLongest: int
    sacks: int
    sacksForLossYards: int
    sacksYards: int
    secondDownsAttempted: int
    secondDownsConversions: int
    secondDownsConversionsPercentage: float
    secondDownsFourToSixYardsAttempted: int
    secondDownsFourToSixYardsConversions: int
    secondDownsFourToSixYardsConversionsPercentage: float
    secondDownsOneToThreeYardsAttempted: int
    secondDownsOneToThreeYardsConversions: int
    secondDownsOneToThreeYardsConversionsPercentage: float
    secondDownsSevenPlusYardsAttempted: int
    secondDownsSevenPlusYardsConversions: int
    secondDownsSevenPlusYardsConversionsPercentage: float
    secondDownsYards: int
    secondDownsYardsAverage: float
    singles: int
    singlesFieldGoals: int
    singlesKickoffs: int
    singlesPunts: int
    tackles: int
    tacklesForLoss: int
    tacklesForLossYards: int
    tacklesSolo: int
    tacklesSpecialTeam: int
    thirdDownAttempts: int
    thirdDownConversions: int
    thirdDownsYards: int
    thirdDownsYardsAverage: float
    timeOfPossession: str
    timeOfPossessionSeconds: int
    touchdowns: int
    touchdownsInterceptionsReturns: int
    touchdownsInterceptionsReturnsYardsLongest: int
    touchdownsKickoffsReturns: int
    touchdownsKickoffsReturnsYardsLongest: int
    touchdownsPassesYardsLongest: int
    touchdownsPuntingReturns: int
    touchdownsPuntingReturnsYardsLongest: int
    touchdownsReceptions: int
    touchdownsReceptionsYardsLongest: int
    touchdownsReturns: int
    touchdownsRushingYardsLongest: int
    turnovers: int
    turnoversOnDowns: int
    twoPointPassAttempted: int
    twoPointPassSucceeded: int
    twoPointReceptionAttempted: int
    twoPointReceptionSucceeded: int
    twoPointRushAttempted: int
    twoPointRushSucceeded: int


class SeasonTeamStats(BaseTeamStats, total=False):
    season: Required[int]
    season_id: Required[int]
    team_id: Required[int]
    team_abbreviation: str
    defensiveExtraPointsBlocked: int
    driveGoalToGoSucceeded: int
    opponent_team_abbreviation: str
    opponent_team_id: int
    pointsScoredOvertime: int
    thirdDownsConversionsPercentage: float
    touchdownsRushing: int


class FixtureTeamStats(BaseTeamStats, total=False):
    driveGoalToGoSuccessful: int
    extraPointsBlocked: int
    fieldGoalsBlocked: int
    passesSackedThirdDown: int
    puntsBlocked: int
    safeties: int
    touchdownsFieldGoalsReturns: int
    touchdownsFumblesOwnRecovery: int
    touchdownsFumblesReturn: int
    touchdownsKickoffsOwnRecovery: int
    touchdownsPuntingOwnRecovery: int
    twoPointConversionsDefense: int
    twoPointDefensiveConversionsAttempted: int
    twoPointDefensiveConversionsSucceeded: int
    yardsAfterCatch: int


class FixtureTeamStatsWrapper(TypedDict, total=False):
    fixture_id: Required[int]
    genius_id: int
    season: int
    season_id: Required[int]
    week: int
    start_at: str
    stats: FixtureTeamStats


class TeamStats(TypedDict):
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
    fieldGoalsMissedReturns: int
    fieldGoalsMissedReturnsYards: int
    fumbles: int
    fumblesForced: int
    fumblesRecoveries: int
    fumblesRecoveriesOwn: int
    kickoffs: int
    kickoffsInsideEndZone: int
    kickoffsInsideTwenty: int
    kickoffsKickerReturnsYards: int
    kickoffsOutOfBounds: int
    kickoffsYards: int
    kickoffsYardsAverage: int
    kickoffsYardsLongest: int
    kickoffsReturns: int
    kickoffsReturnsYards: int
    kickoffsReturnsYardsLongest: int
    passesAttempted: int
    passesIntercepted: int
    passesDefended: int
    passesRating: float
    passesSucceeded: int
    passesSucceededPercentage: float | None
    passesSucceededYards: int
    passesSucceededYardsLongest: int
    passesTargetedAt: int
    penaltiesChargedDefense: int
    penaltiesChargedOffense: int
    pointsScored: int
    pointsScoredFirstQuarter: int
    pointsScoredFourthQuarter: int
    pointsScoredThirdQuarter: int
    puntingInsideTen: int
    puntingInsideTwenty: int
    puntingKickerReturnsYards: int
    puntingYards: int
    puntingYardsGrossAverage: float | None
    puntingYardsNet: int | float | None
    puntingReturnsYards: int
    puntingReturnsYardsLongest: int
    punts: int
    puntsReturns: int
    receptions: int
    receptionsYards: int
    receptionsYardsLongest: int
    rushes: int
    rushingYards: int
    rushingYardsLongest: int
    sacks: int
    singles: int
    singlesKickoffs: int
    singlesPunts: int
    tackles: int
    tacklesForLoss: int
    tacklesSolo: int
    tacklesSpecialTeam: int
    touchdownsPasses: int
    touchdownsReceptions: int
    touchdownsReceptionsYardsLongest: int
    touchdownsRushing: int
    touchdownsRushingYardsLongest: int
    yardsAfterCatch: int


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
    ID: int
    seasons: list[SeasonPlayerStats]
    fixtures: list[FixturePlayerStatsWrapper]
    last_game_id: int
    player_id: Required[int]
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
