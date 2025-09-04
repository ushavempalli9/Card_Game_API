import requests
from requests import Response
from framework.config import BASE_URL, HEALTH_URL, DEFAULT_TIMEOUT


class DeckOfCardsAPI:
    """Client wrapper for Deck of Cards API."""

    def __init__(self, base_url: str = BASE_URL, timeout: int = DEFAULT_TIMEOUT):
        self.base_url = base_url
        self.timeout = timeout

    def _get(self, endpoint: str) -> dict:
        """Helper for GET requests with error handling."""
        url = endpoint if endpoint.startswith("http") else f"{self.base_url}/{endpoint}"
        response: Response = requests.get(url, timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    def check_site_up(self) -> int:
        """Check if the API site is up."""
        response: Response = requests.get(HEALTH_URL, timeout=self.timeout)
        response.raise_for_status()
        return response.status_code

    def get_new_deck(self) -> str:
        """Create a new deck and return its ID."""
        return self._get("new/")["deck_id"]

    def shuffle_deck(self, deck_id: str) -> dict:
        """Shuffle an existing deck."""
        return self._get(f"{deck_id}/shuffle/")

    def draw_cards(self, deck_id: str, count: int) -> list[dict]:
        """Draw a given number of cards from a deck."""
        return self._get(f"{deck_id}/draw/?count={count}")["cards"]