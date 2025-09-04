## The Card Game Test Suite

This project contains API Test Automation Framework for the card game at (https://deckofcardsapi.com) using Python.

## Test Requirements

The test suite covers the following requirements:

1. Navigate to https://deckofcardsapi.com/
2. Confirm the site is up
3. Get a new deck
4. Shuffle it
5. Deal three cards to each of two players
6. Check whether either has blackjack
7. If either has, write out which one does

## Prerequisites

- Python 3.7 or higher
- pip install pytest requests

## Running the Tests

### Run All Tests
```bash
pytest -v
```

### Run Tests
pytest -v


## Test Descriptions

### Test 1: API is reachable
- Call the Deck of Cards API.
- Validates the API is reachable

### Test 2: SetUp Deck
- Confirms the Deck shuffled.
- Validates whether deck is shuffled successfully.

### Test 3:Deal Cards
- Verify that the API returned the expected number of cards.
- Validates whether the cards were successfully dealt.

### Test 4: Blackjack simulation - Assign and Score
- Ensures the Player is busted when the score is greater than 21.
- Validates and display "High Score! Player X busted with score greater than 21" is printed.

### Test 5: Player Hits Blackjack
- Tests when score equals to 21.
- Verifies player points exactly and display "Magic! Player X has Blackjack!" is printed.

### Test 6: Check Player Safe Level based on the score
- Tests when score is less than 21.
- Verifies player points and display "Player X is safe with score Y" is printed.
  
### Test 7: Check Multiple players Score Calculation
- Ensure calculate_score correctly computes totals.
- Score matches manual calculation.

### Test 8: Check if too many cards were drawn
- Ensure API returns only 52 cards.
- Count should match, otherwise display message exceeding deck limit.

