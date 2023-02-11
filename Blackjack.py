# BLackJack or 21 Game

import random
import time

#Game Meta
print("...")
time.sleep(1)
print("... Welcome to Bilbo Swaggins' Game of Blackjack ...")
print("\n")
print("Try to beat the Dealers hand without going over 21. The Dealer is trapped inside this computer and will try to beat you...")
print("\n")
time.sleep(1)
games_played = 0
player_wins = 0
player_loose = 0

action_taken = str(input("Do you want to play? y/n"))
play_again = action_taken

if play_again.upper() == "N":
    print("You played a total of "+ str(games_played) +" games. Thanks for playing! You have won " + str(player_wins) + " and lost " + str(player_loose) + " games.")


while play_again.upper() == "Y":
    games_played = games_played + 1
    # Dealer Cards
    dealer_cards = []
    # Player Cards
    player_cards = []

    #Deal Cards
    # Dealer Cards
    print("\n")
    print("...Dealing out Cards...")
    print("\n")
    time.sleep(2)
    while len(dealer_cards) != 2:
        dealer_cards.append(random.randint(1, 11))
        if len(dealer_cards) == 2:
            print("Dealer has X &", dealer_cards[1])

    # Player Cards
    while len(player_cards) != 2:
        player_cards.append(random.randint(1, 11))
        if len(player_cards) == 2:
            print("You have", player_cards[0], "&", player_cards[1],", Total:", str(sum(player_cards)),)

    # Sum of the Dealer cards
    if sum(dealer_cards) == 21:
        print ("Dealers Cards:" + str(dealer_cards) + "Total:" + str(sum(dealer_cards)) + "Dealer wins you looser!")
    elif sum(dealer_cards) > 21:
        print ("Dealer has busted! You won")
        player_wins += 1

    # Drawing Cards
    # Player Draws Cards
    while sum(player_cards) < 21:
        time.sleep(1)
        print("\n")
        action_taken = str(input("Do you want to stay or hit? "))
        if action_taken == "hit":
            print(".. kinky ...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            player_cards.append(random.randint(1,11))
            print("You now have a total of " + str(sum(player_cards))+ " from the following cards ... ", player_cards)
        else:
            print("...")
            time.sleep(1)
            print("The dealer has a total of " +str(sum(dealer_cards)) + " with ", dealer_cards)
            print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)
            break

    if (sum(player_cards)) == 21:
        print("You have BLACKJACK! FAME AND GLORY TO YOU! FOREVER! AND EVER!")
        player_wins += 1
    elif sum(player_cards) > 21:
        print("You busted! Dealer takes all your money!")
        player_loose += 1

    # Dealer Draws Cards when Dealer has less than 17 and less than Player
    while sum(dealer_cards) < 17 and sum(dealer_cards) < sum(player_cards) < 21:
        print("Now the dealer draws a card...")
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        dealer_cards.append(random.randint(1, 11))
        print("Dealer has" + str(dealer_cards) + ". Total of " + str(sum(dealer_cards)))

    #Winning Conditions
    if sum(dealer_cards) == 21:
        print("Dealer nails it with a 21! You never had a chance...")
        player_loose += 1
    elif sum(dealer_cards) > 21:
        print("The Dealer BUSTED. YOU WIN!!! ALL THE $$$MONEY$$$!!! ....(which is = $0)")
        player_wins += 1
    elif sum(player_cards) > sum(dealer_cards) and sum(player_cards) < 21:
        print("You actually .. won?")
        player_wins += 1
        break
    elif sum(dealer_cards) > sum(player_cards):
        print("Dealer has more points than you and wins!")
        player_loose += 1
    elif sum(player_cards) == sum(dealer_cards):
        print("STALEMATE! Also known as 'You l00se, l00ser'")
        player_loose += 1
    time.sleep(1)
    print("...")
    print("You have won " + str(player_wins) + " and lost " + str(player_loose) + " games."
          )
    play_again = input("Would you like to play again? y/n ")
    play_again = play_again.upper()
if play_again == "Y":
        print("...")
        time.sleep(1)
        print("...Cleaning up the mess you made in the last game ...")
        time.sleep(3)
        print("...")
if play_again == "N":
        print("You played a total of "+ str(games_played) +" games. You have won " + str(player_wins) + " and lost " + str(player_loose) + " games. Thanks for playing!")



