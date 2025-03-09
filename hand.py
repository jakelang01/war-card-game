import deck
import card

class Hand:
    def __init__(self, player, deck):
        self.player = player
        self.deck = []
        
    def __repr__(self):
        for obj in self.deck:
            print(obj)
            
    def add_card(self, card):
        self.deck.append(card)
        
    def get_top_card(self):
        return self.deck.pop(0)