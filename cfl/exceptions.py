"""Exception classes for the CFL API SDK."""


class CFLAPIError(Exception):
    """Base exception for CFL API errors."""

    pass


class CFLAPIConnectionError(CFLAPIError):
    """Raised when connection to the API fails."""

    pass


class CFLAPITimeoutError(CFLAPIError):
    """Raised when API request times out."""

    pass


class CFLAPIResponseError(CFLAPIError):
    """Raised when API returns an error response."""

    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        super().__init__(f"API Error ({status_code}): {message}")


class CFLAPINotFoundError(CFLAPIResponseError):
    """Raised when a resource is not found (404)."""

    def __init__(self, message: str = "Resource not found"):
        super().__init__(404, message)


class CFLAPIAuthenticationError(CFLAPIResponseError):
    """Raised for authentication errors (401, 403)."""

    def __init__(self, status_code: int, message: str):
        super().__init__(status_code, message)


class CFLAPIValidationError(CFLAPIResponseError):
    """Raised for validation errors (400)."""

    def __init__(self, message: str = "Invalid request"):
        super().__init__(400, message)


class CFLAPIServerError(CFLAPIResponseError):
    """Raised for server errors (500+)."""

    def __init__(self, status_code: int, message: str = "Server error"):
        super().__init__(status_code, message)
