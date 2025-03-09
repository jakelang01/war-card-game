# Author: Jake Langenfeld
# Date Created: 03/08/2025

# The Card class creates a specific card with a number between 1-13 and a suit of Heart, Spade, Diamond, or Club.
class Card:
    # Constructor
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    # The get_card_number function gets the number of the card parameter
    def get_card_number(self):
        return self.number
    
    # The get_card_suit function gets the suit of the card parameter
    def get_card_suit(self):
        return self.suit
    
    def __str__(self):
        return f"{self.number} of {self.suit}"
    
    def __repr__(self):
        return self.__str__