from hand import Hand
from card import Card

# Author: Jake Langenfeld
# Date Created: 03/08/2025

class Player:
    def __init__(self, name: str):
        self.name: str = name
        self.hand: Hand = Hand()
    
    def get_name(self) -> str:
        return self.name
    
    def get_hand(self) -> Hand:
        return self.hand
    
    def receive_card(self, card: Card) -> None:
        self.hand.add_card(card)
