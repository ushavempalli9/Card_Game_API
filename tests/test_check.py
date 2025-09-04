import pytest
from framework.api_client import DeckOfCardsAPI
from framework.utils import calculate_score

# Wrapper for assertions
def assert_with_message(condition, success_msg, fail_msg):
    """Assert condition, print success message if True, fail if False"""
    if condition:
        print(f" Pass!{success_msg}")
    else:
        assert False, f"fail! {fail_msg}"

# Parametrized Blackjack Test
@pytest.mark.parametrize("players, cards_per_player", [(2, 3), (3, 2)])
def test_blackjack_game(api_client: DeckOfCardsAPI, players: int, cards_per_player: int):
    """Simulate a blackjack game with variable players and card count."""

    #  Check API reachability
    status = api_client.check_site_up()
    assert_with_message(
        status == 200,
        success_msg="Deck of Cards API is reachable",
        fail_msg=f"Deck of Cards API is not reachable. Status code: {status}"
    )

    #  Setup deck
    deck_id = api_client.get_new_deck()
    shuffle_response = api_client.shuffle_deck(deck_id)
    assert_with_message(
        shuffle_response.get("shuffled") is True,
        success_msg="Deck shuffled successfully",
        fail_msg="Deck was not shuffled properly"
    )

    #  Deal cards
    total_cards = players * cards_per_player
    cards = api_client.draw_cards(deck_id, count=total_cards)
    assert_with_message(
        len(cards) == total_cards,
        success_msg=f"Dealt {total_cards} cards successfully",
        fail_msg=f"Expected {total_cards} cards, got {len(cards)}"
    )

    # Assign and score players
    print("Starting Blackjack simulation for {players} player(s), {cards_per_player} cards each")
    for i in range(players):
        hand = cards[i * cards_per_player:(i + 1) * cards_per_player]
        score = calculate_score(hand)
        card_values = [c['value'] for c in hand]
        print(f"Player {i+1} cards: {card_values}, score: {score}")

        if score > 21:
            print(f"High Score! Player {i+1} busted with score {score}")
        elif score == 21:
            print(f"Magic! Player {i+1} has Blackjack!")
        else:
            print(f"✅ Player {i+1} is safe with score {score}")


# Additional Test Cases
def test_draw_too_many_cards(api_client: DeckOfCardsAPI):
    """Test API behavior when drawing more cards than in deck"""
    deck_id = api_client.get_new_deck()
    api_client.shuffle_deck(deck_id)
    total_cards_in_deck = 52

    # Attempt to draw more cards than exist
    draw_count = 60
    cards = api_client.draw_cards(deck_id, count=draw_count)

    assert_with_message(
        len(cards) <= total_cards_in_deck,
        success_msg=f"API returned {len(cards)} cards, not exceeding deck limit",
        fail_msg=f"API returned more cards than deck size: {len(cards)} > {total_cards_in_deck}"
    )


def test_deck_id_unique(api_client: DeckOfCardsAPI):
    """Check if each new deck has a unique deck_id"""
    deck1 = api_client.get_new_deck()
    deck2 = api_client.get_new_deck()
    assert_with_message(
        deck1 != deck2,
        success_msg=f"New decks have unique IDs: {deck1} vs {deck2}",
        fail_msg=f"Deck IDs are not unique: {deck1} vs {deck2}"
    )


def test_shuffle_changes_order(api_client: DeckOfCardsAPI):
    """Check if shuffling actually changes card order"""
    deck_id = api_client.get_new_deck()
    original_cards = api_client.draw_cards(deck_id, count=5)
    api_client.shuffle_deck(deck_id)
    shuffled_cards = api_client.draw_cards(deck_id, count=5)

    assert_with_message(
        original_cards != shuffled_cards,
        success_msg="Deck shuffled changed card order",
        fail_msg="Deck shuffle did not change card order"
    )
