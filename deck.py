from random import shuffle
from card import Card

# Author: Jake Langenfeld
# Date Created: 03/08/2025

# The Deck class is defined by a deck of cards. 
# The contructor creates a standard 52 card deck with combinations of ranks 2-14 (Ace is played as a high card) and suits of Hearts, Spades, Diamonds, and Clubs. 
class Deck:
    ranks: list[int] = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    suits: list[str] = ["Hearts", "Diamonds", "Spades", "Clubs"]
        
    def __init__(self):
        self.deck: list[Card] = self.build_deck()
        
    def build_deck(self) -> list[Card]:
        return [Card(rank, suit) for rank in Deck.ranks for suit in Deck.suits]
    
    def __str__(self) -> str:
        return ", ".join(str(card) for card in self.deck)

    # The shuffle function is used to randomly shuffle a deck of cards.
    def shuffle(self) -> None:
        shuffle(self.deck)
    
    def get_top_card(self) -> Card:
        return self.deck.pop(0)
    
    def get_deck_size(self) -> int:
        size: int = 0
        for card in self.deck:
            size += 1
            
        return size
