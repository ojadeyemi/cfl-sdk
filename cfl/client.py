# type: ignore
# TODO cast data to right type before returning
"""CFL API Client for accessing CFL data."""

import asyncio
import json
from urllib.parse import urljoin

import httpx
from bs4 import BeautifulSoup

from .constants import (
    BASE_API_URL,
    BASE_WEB_URL,
    DEFAULT_HEADERS,
    DEFAULT_LIMIT,
    DEFAULT_PAGE,
    DEFAULT_SEASON,
    DEFAULT_TIMEOUT,
    DEFENCE,
    FIXTURES_ENDPOINT,
    LEADERBOARD_URL,
    LEDGER_ENDPOINT,
    MAX_SEASON,
    MIN_SEASON,
    OFFENCE,
    PLAYER_PIMS_ENDPOINT,
    PLAYER_STAT_ENDPOINT,
    PLAYER_STATS_ENDPOINT,
    ROSTER_ENDPOINT,
    ROSTERS_ENDPOINT,
    SEASON_ENDPOINT,
    SEASON_FIXTURES_ENDPOINT,
    SEASONS_ENDPOINT,
    SPECIAL_TEAMS,
    TEAM_ENDPOINT,
    TEAM_STAT_ENDPOINT,
    TEAM_STATS_ENDPOINT,
    TEAMS_ENDPOINT,
    VENUE_ENDPOINT,
    VENUES_ENDPOINT,
    get_random_user_agent,
)
from .exceptions import (
    CFLAPIAuthenticationError,
    CFLAPIConnectionError,
    CFLAPINotFoundError,
    CFLAPIServerError,
    CFLAPITimeoutError,
    CFLAPIValidationError,
)
from .leaderboard import parse_leaderboard_category
from .logger import logger
from .types import (
    Fixture,
    LeagueLeaders,
    LedgerTransaction,
    PlayerStats,
    Roster,
    Season,
    Standings,
    Team,
    TeamStats,
    Venue,
)


class CFLClient:
    """Client for interacting with the CFL API."""

    def __init__(
        self,
        base_url: str = BASE_API_URL,
        timeout: int = DEFAULT_TIMEOUT,
    ):
        """Initialize CFL API client.

        Args:
            base_url: API base URL
            timeout: Request timeout in seconds
        """

        self.base_url = base_url
        self.timeout = timeout
        self.headers = {**DEFAULT_HEADERS, "User-Agent": get_random_user_agent()}
        self.client = httpx.Client(timeout=timeout)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        """Close HTTP client."""
        self.client.close()
        logger.debug("Closed HTTP client")

    def _url(self, endpoint: str) -> str:
        """Build full URL from endpoint.

        Args:
            endpoint: API endpoint path

        Returns:
            Complete URL
        """

        return urljoin(self.base_url, f"/api/{endpoint.lstrip('/')}")

    def _handle_response(self, response: httpx.Response) -> dict:
        """Process API response and handle errors.

        Args:
            response: HTTP response

        Returns:
            Response JSON data

        Raises:
            CFLAPIResponseError: For API errors
        """
        logger.debug(f"Response status: {response.status_code}")

        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            status_code = e.response.status_code

            try:
                error_data = e.response.json()
                message = error_data.get("message", str(e))
            except (ValueError, KeyError):
                message = str(e)

            if status_code == 404:
                raise CFLAPINotFoundError(message) from e
            elif status_code in (401, 403):
                raise CFLAPIAuthenticationError(status_code, message) from e
            elif status_code == 400:
                raise CFLAPIValidationError(message) from e
            elif status_code >= 500:
                raise CFLAPIServerError(status_code, message) from e
            else:
                raise CFLAPIValidationError(message) from e

        try:
            return response.json()

        except json.JSONDecodeError:
            logger.warning("Failed to decode JSON response")

            return {}

    def _request(
        self,
        method: str,
        endpoint: str,
        params: dict | None = None,
        json_data: dict | None = None,
    ) -> dict:
        """Send HTTP request to the API.

        Args:
            method: HTTP method
            endpoint: API endpoint
            params: Query parameters
            json_data: JSON request body

        Returns:
            Response JSON data

        Raises:
            CFLAPIConnectionError: For connection failures
            CFLAPITimeoutError: For request timeouts
        """
        url = self._url(endpoint)
        logger.debug(f"{method} {url}")

        try:
            response = self.client.request(
                method=method,
                url=url,
                params=params,
                json=json_data,
            )

            return self._handle_response(response)

        except httpx.ConnectError as e:
            logger.error(f"Connection error: {e}")
            raise CFLAPIConnectionError(f"Failed to connect: {e}") from e

        except httpx.TimeoutException as e:
            logger.error(f"Request timed out: {e}")
            raise CFLAPITimeoutError(f"Request timed out: {e}") from e

        except Exception as e:
            logger.error(f"Request failed: {e}")
            raise

    def _get(
        self,
        endpoint: str,
        params: dict | None = None,
    ) -> dict:
        """Send GET request to API.

        Args:
            endpoint: API endpoint
            params: Query parameters

        Returns:
            Response JSON data
        """

        return self._request("GET", endpoint, params=params)

    def _paginated_get(
        self,
        endpoint: str,
        params: dict | None = None,
        limit: int = DEFAULT_LIMIT,
        page: int = DEFAULT_PAGE,
    ) -> list[dict]:
        """Get one page from a paginated endpoint.

        Args:
            endpoint: API endpoint
            params: Additional query parameters
            limit: Items per page
            page: Page number

        Returns:
            List of items from the requested page
        """
        params = params or {}
        params["limit"] = limit
        params["page"] = page

        response = self._get(endpoint, params)
        return response

    def get_teams(
        self,
    ) -> list[Team]:
        """Get all CFL teams.

        Args:
            page: Page number
            limit: Items per page

        Returns:
            List of teams
        """
        teams = self._get(
            TEAMS_ENDPOINT,
        )
        return teams

    def get_team(self, team_id: int) -> Team:
        """Get team details by ID.

        Args:
            team_id: Team ID

        Returns:
            Team details
        """
        endpoint = TEAM_ENDPOINT.format(team_id=team_id)

        return self._get(endpoint)

    def get_venues(
        self,
    ) -> list[Venue]:
        """Get all CFL venues.

        Args:
            page: Page number
            limit: Items per page

        Returns:
            List of venues
        """
        venues = self._paginated_get(
            VENUES_ENDPOINT,
        )

        return venues

    def get_venue(self, venue_id: int) -> Venue:
        """Get venue details by ID.

        Args:
            venue_id: Venue ID

        Returns:
            Venue details
        """
        endpoint = VENUE_ENDPOINT.format(venue_id=venue_id)

        return self._get(endpoint)

    def get_seasons(self, page: int = DEFAULT_PAGE, limit: int = DEFAULT_LIMIT) -> list[Season]:
        """Get all seasons.

        Args:
            page: Page number
            limit: Items per page

        Returns:
            List of seasons
        """
        seasons = self._paginated_get(
            SEASONS_ENDPOINT,
            params={"page": page, "limit": limit},
        )

        return seasons

    def get_season(self, season_id: int) -> Season:
        """Get season details by ID.

        Args:
            season_id: Season ID

        Returns:
            Season details
        """
        endpoint = SEASON_ENDPOINT.format(season_id=season_id)

        return self._get(endpoint)

    def get_fixtures(
        self,
        season_id: int | None = None,
        page: int = DEFAULT_PAGE,
        limit: int = DEFAULT_LIMIT,
    ) -> list[Fixture]:
        """Get all fixtures (games).

        Args:
            season_id: Optional season filter
            page: Page number
            limit: Items per page

        Returns:
            List of fixtures
        """
        params = {"page": page, "limit": limit}
        if season_id:
            endpoint = SEASON_FIXTURES_ENDPOINT.format(season_id=season_id)
        else:
            endpoint = FIXTURES_ENDPOINT

        fixtures = self._paginated_get(
            endpoint,
            params=params,
        )

        return fixtures

    def get_rosters(
        self,
    ) -> list[Roster]:
        """Get all rosters.

        Args:
            team_id: Optional team filter
            page: Page number
            limit: Items per page

        Returns:
            List of rosters
        """

        rosters = self._get(
            ROSTERS_ENDPOINT,
        )

        return rosters

    def get_roster(self, roster_id: int) -> Roster:
        """Get roster details by ID.

        Args:
            roster_id: Roster ID

        Returns:
            Roster details
        """
        endpoint = ROSTER_ENDPOINT.format(roster_id=roster_id)

        return self._get(endpoint)

    def get_ledger(
        self,
        year: int,
    ) -> list[LedgerTransaction]:
        """Get player transactions.

        Args:
            year: Year to fetch (e.g., 2024)
            page: Page number
            limit: Items per page

        Returns:
            List of transactions
        """
        endpoint = LEDGER_ENDPOINT.format(year=year)
        transactions = self._get(
            endpoint,
        )

        return transactions

    def get_team_stats(
        self,
        season_id: int | None = None,
    ) -> list[TeamStats]:
        """Get team statistics.

        Args:
            season_id: Optional season filter
            page: Page number
            limit: Items per page

        Returns:
            List of team statistics
        """
        params = {}
        if season_id:
            params["season_id"] = season_id

        stats = self._get(
            TEAM_STATS_ENDPOINT,
            params=params,
        )

        return stats

    def get_team_stat(self, team_stats_id: int, season_id: int | None = None) -> TeamStats:
        """Get team stats by ID.

        Args:
            team_stats_id: Team stats ID

        Returns:
            Team statistics
        """
        endpoint = TEAM_STAT_ENDPOINT.format(team_stats_id=team_stats_id)
        params = {}
        if season_id:
            params["season_id"] = season_id

        return self._get(endpoint, params=params)

    def get_player_stats(
        self,
        season_id: int | None = None,
        page: int = DEFAULT_PAGE,
        limit: int = DEFAULT_LIMIT,
    ) -> list[PlayerStats]:
        """Get culumnating player statistics.

        Args:
            team_id: Optional team filter
            page: Page number
            limit: Items per page

        Returns:
            List of player statistics
        """
        params = {"page": page, "limit": limit}

        if season_id:
            params["season_id"] = season_id

        stats = self._paginated_get(
            PLAYER_STATS_ENDPOINT,
            params=params,
        )
        return stats

    def get_player_stat(self, player_stats_id: int) -> PlayerStats:
        """Get player stats by Player stats ID.

        Args:
            player_stats_id: Player stats ID

        Returns:
            Player statistics
        """
        endpoint = PLAYER_STAT_ENDPOINT.format(player_stats_id=player_stats_id)
        return self._get(endpoint)

    def get_player_pims(self, player_id: int) -> PlayerStats:
        """Get player stats by PIMS ID (player id).

        Args:
            player_id: Player ID

        Returns:
            Player statistics with photo URL
        """
        endpoint = PLAYER_PIMS_ENDPOINT.format(player_id=player_id)
        data = self._get(endpoint)

        if data:
            data["photo_url"] = f"https://static.cfl.ca/wp-content/uploads/{player_id}.png"

        return data

    def get_standings(self, year: int = DEFAULT_SEASON) -> Standings:
        """Get Standings data of a season

        Args:
            year: Season year (valid options: 2023-2025)

        Returns:
            Dictionary containing standings data by division
        """
        if year < MIN_SEASON or year > MAX_SEASON:
            raise ValueError("Year must be between 2023 and 2025")

        url = f"{BASE_WEB_URL}/standings/{year}"
        standings: Standings = {"WEST": [], "EAST": []}

        try:
            with httpx.Client(timeout=DEFAULT_TIMEOUT) as client:
                response = client.get(url)
                response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")
            tables = soup.find_all("table")

            if not tables:
                return standings

            for i, table in enumerate(tables[:2]):
                division = "WEST" if i == 0 else "EAST"
                thead = table.find("thead")
                tbody = table.find("tbody")

                if not thead or not tbody:
                    continue

                headers = [th.text.strip() for th in thead.find_all("th")]

                for row in tbody.find_all("tr"):
                    cells = row.find_all("td")
                    if len(cells) != len(headers):
                        continue  # Skip malformed row

                    team_data = {}
                    for j, cell in enumerate(cells):
                        text = cell.text.strip()
                        if j == 1:
                            team_name_tag = cell.find("a")
                            text = team_name_tag.text.strip() if team_name_tag else text

                        team_data[headers[j]] = text

                    standings[division].append(team_data)

        except (httpx.HTTPStatusError, httpx.RequestError, Exception):
            return standings

        return standings

    async def get_leaderboards_async(self, season: int = DEFAULT_SEASON) -> LeagueLeaders:
        """Get league leaders for all categories asynchronously"""
        if season < MIN_SEASON or season > MAX_SEASON:
            raise ValueError(f"Season must be between {MIN_SEASON} and {MAX_SEASON}")

        result: LeagueLeaders = {OFFENCE: {}, DEFENCE: {}, SPECIAL_TEAMS: {}}
        categories: list[str] = ["offence", "defence", "special_teams"]

        async with httpx.AsyncClient(timeout=DEFAULT_TIMEOUT) as client:
            tasks = []

            for category in categories:
                url = f"{LEADERBOARD_URL}?stat_category={category}&season={season}"
                tasks.append(client.get(url, headers=self.headers))

            responses: list[httpx.Response] = await asyncio.gather(*tasks, return_exceptions=True)

            for category, response in zip(categories, responses):
                if isinstance(response, Exception):
                    continue

                if response.status_code == 200:
                    category_data = parse_leaderboard_category(response.text, category)
                    result[category.upper()] = category_data

        return result

    def get_leaderboards(self, season: int = DEFAULT_SEASON) -> LeagueLeaders:
        """Get league leaders for all categories"""
        try:
            return asyncio.run(self.get_leaderboards_async(season))

        except RuntimeError as e:
            # Fallback if there's already a running event loop
            logger.warning(f"Warning there is already a running event loop {e}")
            loop = asyncio.get_event_loop()

            return loop.run_until_complete(self.get_leaderboards_async(season))
