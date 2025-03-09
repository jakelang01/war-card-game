import hand

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
    
    def get_name(self):
        return self.name