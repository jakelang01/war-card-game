from deck import Deck
from card import Card

# Author: Jake Langenfeld
# Date Created: 03/08/2025

class Hand:
    def __init__(self):
        self.hand: list[Card] = []
        
    def __str__(self) -> str:
        return ", ".join(str(card) for card in self.hand)
            
    def add_card(self, card: Card) -> None:
        self.hand.append(card)
        
    def get_top_card(self) -> Card:
        return self.hand.pop(0)
    
    def get_bottom_card(self) -> Card:
        return self.hand[-1]

    def get_deck_size(self) -> int:
        size: int = 0
        for card in self.hand:
            size += 1
            
        return size
    
    def clear_hand(self) -> None:
        self.hand.clear()