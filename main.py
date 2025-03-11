from deck import Deck
from player import Player
from card import Card
from hand import Hand
from mechanics import *

# Author: Jake Langenfeld
# Date Created: 03/08/2025

# The war_game function runs all the rules that encapsulate the card game, War.
def war_game() -> None:
    # Initialize variables
    
    # Build the playing deck
    deck: Deck = Deck()
    deck.shuffle()

    # Establish the player and their playing Hands
    player_1: Player = Player(input("What is your name? "))
    player_2: Player = Player("Computer")
    player_1_name: str = player_1.get_name()
    player_2_name: str = player_2.get_name()
    
    # Round variable to keep track of how many rounds it takes for a player to win
    round: int = 0
    
    # Initialize each player's play card
    player_1_card: Card = Card()
    player_2_card: Card = Card()
    
    # Total number of wars that happen in a match
    total_wars: int = 0
    
    # Count the number of wars in a row
    war_count: int = 0
    
    # Keep track of highest war count in a row
    highest_war_count: int = 0
    
    # Deal hands to players
    deal_deck(deck, player_1, player_2)
        
    print("The deck has been dealed.")
    print("Time to play, War!")
    
    while player_1.get_hand().get_deck_size() > 0 and player_2.get_hand().get_deck_size() > 0:
        input("Press Enter to start the next round.\n")
        round += 1
        print(f"Round: {round}")
        print(f"{player_1_name} has {player_1.get_hand().get_deck_size()} cards and {player_2_name} has {player_2.get_hand().get_deck_size()} cards")
        
        # Fill each player's play card
        player_1_card = player_1.get_hand().get_top_card()
        player_2_card = player_2.get_hand().get_top_card()
        
        print(f"{player_1_name} plays a {player_1_card} and {player_2_name} plays a {player_2_card}")
        
        # Check if Player 1 won the hand
        if player_1_card.get_card_rank() > player_2_card.get_card_rank():
            print(f"{player_1_name} wins round {round}")
            
            win_round(player_1, player_1_card, player_2_card)
        # Check if Player 2 won the hand
        elif player_1_card.get_card_rank() < player_2_card.get_card_rank():
            print(f"{player_2_name} wins round {round}")
            
            win_round(player_2, player_1_card, player_2_card)
        # Else a tie happened between the players
        else:
            print("There was a tie! Time to go to War!")
            
            # Put the first play card in their war hand so it doesn't get lost
            player_1.get_war_hand().add_card(player_1_card)
            player_2.get_war_hand().add_card(player_2_card)
            
            # Keep looping while the players cards are the same rank
            while player_1_card.get_card_rank() == player_2_card.get_card_rank():
                # Check if each player can participate in the war, otherwise break the loop and end the game
                if not player_can_war(player_1):
                    print(f"{player_1_name} has run out of cards for war! {player_2_name} won the game!")
                    break
                elif not player_can_war(player_2):
                    print(f"{player_2_name} has run out of cards for war! {player_1_name} won the game!")
                    break
                
                # Deal 3 "face-down" cards for each player then have the 4th card be the play card
                deal_war_hand(player_1)
                deal_war_hand(player_2)
            
                total_wars += 1
                war_count += 1
                
                # Set the war play card for each player
                player_1_card = player_1.get_war_hand().get_bottom_card()
                player_2_card = player_2.get_war_hand().get_bottom_card()
                
                print(f"War: {war_count}, {player_1_name} plays a {player_1_card} and {player_2_name} plays a {player_2_card}")
                
                # Check if player 1 beats player 2
                if player_1_card.get_card_rank() > player_2_card.get_card_rank():
                    print(f"{player_1_name} wins the War! {player_1_name} won {player_2.get_war_hand().get_deck_size()} cards from {player_2_name}")
                    win_war(player_1, player_2)
                    player_1.get_war_hand().clear_hand()
                    player_2.get_war_hand().clear_hand()
                # Check if player 2 beats player 1
                elif player_1_card.get_card_rank() < player_2_card.get_card_rank():
                    print(f"{player_2_name} wins the War! {player_2_name} won {player_1.get_war_hand().get_deck_size()} cards from {player_1_name}")
                    win_war(player_2, player_1)
                    player_1.get_war_hand().clear_hand()
                    player_2.get_war_hand().clear_hand()
                else:
                    print("There was another tie! Time to do another War!")
                     
            if war_count == 1:
                print("There was only", war_count, "war in a row.")
            else:
                print("There were", war_count, "wars in a row!")
                
            if war_count > highest_war_count:
                highest_war_count = war_count
                
            war_count = 0
        
    if player_1.get_hand().get_deck_size() > 0:
        print(f"\n{player_1_name} is the winner! {player_1_name} won in {round} rounds! There was a total of {total_wars} wars in the match! The longest consecutive war was {highest_war_count} wars!\n")
    else:
        print(f"\n{player_2_name} is the winner! {player_2_name} won in {round} rounds! There was a total of {total_wars} wars in the match! The longest consecutive war was {highest_war_count} wars!\n")
        
        
        
        
# The simulate_war_game function runs all the rules that encapsulate the card game, War, without any user input besides getting the user's name.
def simulate_war_game() -> None:
    # Initialize variables
    
    # Build the playing deck
    deck: Deck = Deck()
    deck.shuffle()

    # Establish the player and their playing Hands
    player_1: Player = Player(input("What is your name? "))
    player_2: Player = Player("Computer")
    player_1_name: str = player_1.get_name()
    player_2_name: str = player_2.get_name()
    
    # Round variable to keep track of how many rounds it takes for a player to win
    round: int = 0
    
    # Initialize each player's play card
    player_1_card: Card = Card()
    player_2_card: Card = Card()
    
    # Total number of wars that happen in a match
    total_wars: int = 0
    
    # Count the number of wars in a row
    war_count: int = 0
    
    # Keep track of highest war count in a row
    highest_war_count: int = 0
    
    # Deal hands to players
    deal_deck(deck, player_1, player_2)
        
    print("The deck has been dealed.")
    print("Time to play, War!")
    
    while player_1.get_hand().get_deck_size() > 0 and player_2.get_hand().get_deck_size() > 0:
        round += 1
        print(f"\nRound: {round}")
        print(f"{player_1_name} has {player_1.get_hand().get_deck_size()} cards and {player_2_name} has {player_2.get_hand().get_deck_size()} cards")
        
        # Fill each player's play card
        player_1_card = player_1.get_hand().get_top_card()
        player_2_card = player_2.get_hand().get_top_card()
        
        print(f"{player_1_name} plays a {player_1_card} and {player_2_name} plays a {player_2_card}")
        
        # Check if Player 1 won the hand
        if player_1_card.get_card_rank() > player_2_card.get_card_rank():
            print(f"{player_1_name} wins round {round}")
            
            win_round(player_1, player_1_card, player_2_card)
        # Check if Player 2 won the hand
        elif player_1_card.get_card_rank() < player_2_card.get_card_rank():
            print(f"{player_2_name} wins round {round}")
            
            win_round(player_2, player_1_card, player_2_card)
        # Else a tie happened between the players
        else:
            print("There was a tie! Time to go to War!")
            
            # Put the first play card in their war hand so it doesn't get lost
            player_1.get_war_hand().add_card(player_1_card)
            player_2.get_war_hand().add_card(player_2_card)
            
            # Keep looping while the players cards are the same rank
            while player_1_card.get_card_rank() == player_2_card.get_card_rank():
                # Check if each player can participate in the war, otherwise break the loop and end the game
                if not player_can_war(player_1):
                    print(f"{player_1_name} has run out of cards for war! {player_2_name} won the game!")
                    break
                elif not player_can_war(player_2):
                    print(f"{player_2_name} has run out of cards for war! {player_1_name} won the game!")
                    break
                
                # Deal 3 "face-down" cards for each player then have the 4th card be the play card
                deal_war_hand(player_1)
                deal_war_hand(player_2)
            
                total_wars += 1
                war_count += 1
                
                # Set the war play card for each player
                player_1_card = player_1.get_war_hand().get_bottom_card()
                player_2_card = player_2.get_war_hand().get_bottom_card()
                
                print(f"War: {war_count}, {player_1_name} plays a {player_1_card} and {player_2_name} plays a {player_2_card}")
                
                # Check if player 1 beats player 2
                if player_1_card.get_card_rank() > player_2_card.get_card_rank():
                    print(f"{player_1_name} wins the War! {player_1_name} won {player_2.get_war_hand().get_deck_size()} cards from {player_2_name}")
                    win_war(player_1, player_2)
                    player_1.get_war_hand().clear_hand()
                    player_2.get_war_hand().clear_hand()
                # Check if player 2 beats player 1
                elif player_1_card.get_card_rank() < player_2_card.get_card_rank():
                    print(f"{player_2_name} wins the War! {player_2_name} won {player_1.get_war_hand().get_deck_size()} cards from {player_1_name}")
                    win_war(player_2, player_1)
                    player_1.get_war_hand().clear_hand()
                    player_2.get_war_hand().clear_hand()
                else:
                    print("There was another tie! Time to do another War!")
                     
            if war_count == 1:
                print("There was only", war_count, "war in a row.")
            else:
                print("There were", war_count, "wars in a row!")
                
            if war_count > highest_war_count:
                highest_war_count = war_count
                
            war_count = 0
        
    if player_1.get_hand().get_deck_size() > 0:
        print(f"\n{player_1_name} is the winner! {player_1_name} won in {round} rounds! There was a total of {total_wars} wars in the match! The longest consecutive war was {highest_war_count} wars!\n")
    else:
        print(f"\n{player_2_name} is the winner! {player_2_name} won in {round} rounds! There was a total of {total_wars} wars in the match! The longest consecutive war was {highest_war_count} wars!\n")

# This runs the main function which emulates the card game, War.
if __name__ == "__main__":
    choice: str = input("Type 1 to play War manually or Type 2 to simulate War. ")
    
    while choice != "1" and choice != "2":
        print("Invalid Input. Try Again.")
        choice = input("Type 1 to play War manually or Type 2 to simulate War. ")
    
    if choice == "1":
        war_game()
    else:
        simulate_war_game()