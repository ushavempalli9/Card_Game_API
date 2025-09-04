from typing import List, Dict


def calculate_score(cards: List[Dict]) -> int:
    """
    Calculate Blackjack score:
    - 2–10 = face value
    - J, Q, K = 10
    - A = 11 (or 1 if score would bust)
    """
    value_map = {"JACK": 10, "QUEEN": 10, "KING": 10}
    score = 0
    aces = 0

    for card in cards:
        rank = card["value"]
        if rank.isdigit():
            score += int(rank)
        elif rank == "ACE":
            aces += 1
            score += 11
        else:
            score += value_map.get(rank, 0)

    # Downgrade Aces if needed
    while score > 21 and aces:
        score -= 10
        aces -= 1

    return score
