# Author: Jake Langenfeld
# Date Created: 03/08/2025

# The Card class creates a specific card with a number between 1-13 and a suit of Heart, Spade, Diamond, or Club.
class Card:
    # Constructor
    def __init__(self, rank: int, suit: str):
        self.rank: str = rank
        self.suit: str = suit

    # The get_card_number function returns the number of the card parameter as a string
    def get_card_value(self) -> str:
        match self.rank:
            case 1:
                return "Ace"
            case 11:
                return "Jack"
            case 12:
                return "Queen"
            case 13:
                return "King"
            case _:
                return str(self.rank)
            
    def get_card_rank(self) -> int:
        return self.rank
    
    # The get_card_suit function gets the suit of the card parameter
    def get_card_suit(self) -> str:
        return self.suit
    
    # The __str__ function will return the Card object in a readable format
    def __str__(self) -> str:
        return f"{self.get_card_value()} of {self.suit}"