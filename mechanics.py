from player import Player
from deck import Deck
from card import Card

def player_can_war(player: Player) -> bool:
    if player.get_hand().get_deck_size() > 0:
        return True
    else:
        return False

def deal_deck(deck: Deck, player_1: Player, player_2: Player) -> None:
    while deck.get_deck_size() > 0:
        # Deal computer first
        player_2.receive_card(deck.get_top_card())
        # Deal player second
        player_1.receive_card(deck.get_top_card())

def has_cards(player: Player) -> bool:
    if player.get_hand().get_deck_size() > 0:
        return True
    else:
        return False

def deal_war_hand(player: Player) -> None:
    num_war_cards: int = 0
    if player.get_hand().get_deck_size() >= 4:
        num_war_cards = 4
    else:
        num_war_cards = player.get_hand().get_deck_size()
    
    for i in range(num_war_cards):
        player.get_war_hand().add_card(player.get_hand().get_top_card())

def win_war(winner: Player, loser: Player) -> None:
    # Put winner's cards back in their hand
    for card in range(winner.get_war_hand().get_deck_size()):
        winner.get_hand().add_card(winner.get_war_hand().get_top_card())
        
    # Put loser's cards in player 1s hand
    for card in range(loser.get_war_hand().get_deck_size()):
        winner.get_hand().add_card(loser.get_war_hand().get_top_card())
        
def win_round(winner: Player, card_1: Card, card_2: Card) -> None:
    # Add the played cards to the bottom of the winner's hand
    winner.get_hand().add_card(card_1)
    winner.get_hand().add_card(card_2)