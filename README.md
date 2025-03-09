# war-card-game
This game emulates playing the card game, War, using Python.

Rules to War:
 - A deck of cards is created at the beginning of the game
 - 2 players are defined
    - Each player gets a hand of cards
        - A hand consists of half the deck of cards, dealed alternatively
 - Each player puts down their top card
 - Whoever has the higher card value takes both cards
 - If both players have cards of the same value, they go to war
    - Each player puts down 3 more cards face down, then they go to war over the 4th card revealed
 - Winner takes all cards, unless there is another tie, then both players go to war again, until there is a winner
 - The winner of the game is decided when one person holds all 52 cards and the other person runs out