import random
import card

# Author: Jake Langenfeld
# Date Created: 03/08/2025

# The Deck class is defined by a deck of cards. 
# The contructor creates a standard 52 card deck with combinations of number 1-13 and suits of Hearts, Spades, Diamonds, and Clubs. 
# Otherwise, the Deck class can be defined with a specific number of cards with each suit.
class Deck:
    def __init__(self):
        self.deck = []
        
    def build_deck(self):
        numbers = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
        suits = ["Heart", "Diamond", "Spade", "Club"]
        
        self.deck = [card.Card(num, suit) for num in numbers for suit in suits]
    
    def __repr__(self):
        for obj in self.deck:
            print(obj)

    # The shuffle function is used to randomly shuffle a deck of cards.
    def shuffle(self):
        return random.shuffle(self.deck)
    
    def get_top_card(self):
        return self.deck.pop(0)
    
deck1 = Deck()
deck1.build_deck()
deck1.__str__()