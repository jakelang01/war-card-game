from deck import Deck
from player import Player
from card import Card
from hand import Hand

# Author: Jake Langenfeld
# Date Created: 03/08/2025

# The main function runs all the rules that encapsulate the card game, War.
def war() -> None:
    # Initialize variables
    
    # Build the playing deck
    deck: Deck = Deck()
#    deck.shuffle()

    # Establish the player and their playing Hands
    player_1: Player = Player(input("What is your name? "))
    player_2: Player = Player("Computer")
    
    # Round variable to keep track of how many rounds it takes for a player to win
    round: int = 1
    
    # Total number of wars that happen in a match
    total_wars: int = 0
    
    # Count the number of wars in a row
    war_count: int = 0
    
    # Each player needs a separate hand for when they go to war and have several cards in play
    player_1_war_hand: list[Card] = []
    player_2_war_hand: list[Card] = []
    
    # Deal hands to players
    while deck.get_deck_size() > 0:
        # Deal computer first
        player_2.receive_card(deck.get_top_card())
        # Deal player second
        player_1.receive_card(deck.get_top_card())
        
    print("The deck has been dealed.")
    print("Time to play, War!")
    input("Press any key to start the next round.\n")
    
    while player_1.get_hand().get_deck_size() > 0 and player_2.get_hand().get_deck_size() > 0 and round <= 10:

        print(f"Round: {round}")
        print(f"{player_1.get_name()} has {player_1.get_hand().get_deck_size()} cards and {player_2.get_name()} has {player_2.get_hand().get_deck_size()} cards")
        
        # Declare the player's play card
        player_1_card: Card = player_1.get_hand().get_top_card()
        player_2_card: Card = player_2.get_hand().get_top_card()
        
        print(f"{player_1.get_name()} plays a {player_1_card} and {player_2.get_name()} plays a {player_2_card}")
        
        # Check if Player 1 won the hand
        if player_1_card.get_card_rank() > player_2_card.get_card_rank():
            print(f"{player_1.get_name()} wins round {round}")
            
            # Add the played cards to the bottom of the winner's hand
            player_1.get_hand().add_card(player_1_card)
            player_1.get_hand().add_card(player_2_card)
        # Check if Player 2 won the hand
        elif player_1_card.get_card_rank() < player_2_card.get_card_rank():
            print(f"{player_2.get_name()} wins round {round}")
            
            # Add the played cards to the bottom of the winner's hand
            player_2.get_hand().add_card(player_1_card)
            player_2.get_hand().add_card(player_2_card)
        # Else a tie happened between the players
        else:
            print("There was a tie! Time to go to War!")
            
            # Put the first play card in their war hand so it doesn't get lost
            player_1_war_hand.append(player_1_card)
            player_2_war_hand.append(player_2_card)
            
            # Deal 3 "face-down" cards for each player then have the 4th card be the play card
            for i in range(4):
                player_1_war_hand.append(player_1.get_hand().get_top_card())
                player_2_war_hand.append(player_2.get_hand().get_top_card())
            
            # Keep looping while the players cards are the same rank
            while player_1_card.get_card_rank() == player_2_card.get_card_rank():
                total_wars += 1
                war_count += 1
                
                # Set the war play card for each player
                player_1_card = player_1_war_hand[-1]
                player_2_card = player_2_war_hand[-1]
                
                print(f"{player_1.get_name()} plays a {player_1_card} and {player_2.get_name()} plays a {player_2_card}")
                
                # Check if player 1 beats player 2
                if player_1_card.get_card_rank() > player_2_card.get_card_rank():
                    print(f"{player_1.get_name()} wins the War! {player_1.get_name()} won {len(player_2_war_hand)} cards from {player_2.get_name()}")
                    
                    # Put player 1s cards back in their hand
                    for card in player_1_war_hand:
                        player_1.get_hand().add_card(card)
                        
                    # Put player 2s cards in player 1s hand
                    for card in player_2_war_hand:
                        player_1.get_hand().add_card(card)
                # Check if player 2 beats player 1
                elif player_1_card.get_card_rank() < player_2_card.get_card_rank():
                    print(f"{player_2.get_name()} wins the War! {player_2.get_name()} won {len(player_1_war_hand)} cards from {player_1.get_name()}")
                
                    # Put player 1s cards in player 2s hand
                    for card in player_1_war_hand:
                        player_2.get_hand().add_card(card)
                        
                    # Put player 2s cards back in their hand
                    for card in player_2_war_hand:
                        player_2.get_hand().add_card(card)
                else:
                    print("There was another tie! Time to go to War!")
                    
                    # Deal another 3 "face-down" cards for each player then have the 4th card be the play card
                    for i in range(4):
                        player_1_war_hand.append(player_1.get_hand().get_top_card())
                        player_2_war_hand.append(player_2.get_hand().get_top_card())
                    
                
            player_1_war_hand.clear()
            player_2_war_hand.clear()
            
            if war_count == 1:
                print("There was only", war_count, "war in a row.")
            else:
                print("There were", war_count, "wars in a row!")
            
        # Input to start the next round
        input("Press any key to start the next round.\n")
        round += 1
        
    if len(player_1.get_hand().get_deck_size()) > 0:
        print(f"{player_1.get_name()} is the winner! {player_1.get_name()} won in {round} rounds! There was a total of {total_wars} wars in the match!")
    else:
        print(f"{player_2.get_name()} is the winner! {player_2.get_name()} won in {round} rounds! There was a total of {total_wars} wars in the match!")
        
def simulate_war() -> None:
    pass

# This runs the main function which emulates the card game, War.
if __name__ == "__main__":
    war()