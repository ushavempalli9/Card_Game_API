import pytest
from framework.api_client import DeckOfCardsAPI


@pytest.fixture(scope="session")
def api_client() -> DeckOfCardsAPI:
    """Provide a reusable API client instance."""
    return DeckOfCardsAPI()