import random

# Initializing the deck
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
               'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}



deck_art = """
   _______
  |       |
  |   ♠   |
  |   A   |
  |       |
   ‾‾‾‾‾‾‾
"""




table_art = """
  _______________
 |  BLACKJACK   |
 |     TABLE     |
 |_______________|
  _______  _______
 |       ||       |
 |   ♠   ||   ♦   |
 |   A   ||   K   |
 |       ||       |
  ‾‾‾‾‾‾  ‾‾‾‾‾‾
"""





# Creating the deck of cards

def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(f'{rank} of {suit}')
    return deck



# Shuffling

def shuffle_deck(deck):
    random.shuffle(deck)



# Dealing a card

def deal_card(deck):
    return deck.pop()




# Calculating total value of a hand

def calc_handVal(hand):
    value = 0
    num_aces = 0
    for card in hand:
        rank = card.split()[0]
        value += card_values[rank]
        if rank == 'Ace':
            num_aces += 1
    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1
    return value



#player data

def init_players(num_players):
    players = []
    for i in range(num_players):
        player_name = input(f'Enter Player {i + 1}\'s name: ')

        player_balance = 1000 

        players.append({'name': player_name, 'balance': player_balance})
    return players




def display_deck():
    print(deck_art)


def display_table():
    print(table_art)




# Game


def play_blackjack(num_players):
    players = init_players(num_players)
    round_num = 1

    display_table()

    while True:
        print(f'Round {round_num}\n')
        round_num += 1



        # Initialize deck and shuffle

        deck = create_deck()
        shuffle_deck(deck)




        # Dealing two cards to each player / dealer


        player_hands = [[] for _ in range(num_players)]
        dealer_hand = []
        for _ in range(2):
            for i in range(num_players):
                player_hands[i].append(deal_card(deck))
            dealer_hand.append(deal_card(deck))



        


        for i in range(num_players):
            print(f"{players[i]['name']}'s turn:")
            while True:
                display_deck()
                print('\nYour hand:', ', '.join(player_hands[i]))
                player_value = calc_handVal(player_hands[i])
                print('Your hand value:', player_value)





                # Checking if player has blackjack
                if player_value == 21:
                    print('Congratulations! You have Blackjack!')
                    players[i]['balance'] += 1.5  # Blackjack pays 1.5 times the bet
                    break



                # Asking the player to hit/ stand/ double down/ surrender / quit
                while True:
                    choice = input('Do you want to "hit", "stand", "double down", "surrender", or "quit"? ').strip().lower()
                    if choice in ['hit', 'stand', 'double down', 'surrender', 'quit']:
                        break



                # If hit, deal a card
                
                if choice == 'hit':
                    player_hands[i].append(deal_card(deck))
                
                
                
                # If double down, double the bet and deal one card

                elif choice == 'double down':
                    player_hands[i].append(deal_card(deck))
                    players[i]['balance'] -= 1  # Double the bet
                    break



                # If surrender, return half of the bet and end round


                elif choice == 'surrender':
                    print('You surrendered. Half of your bet is returned.')
                    players[i]['balance'] += 0.5  # Return half of the bet
                    break
                
                
                
                # If stand, end turn

                elif choice == 'stand':
                    break



                # Check if player busts (goes over 21)

                if calc_handVal(player_hands[i]) > 21:
                    print('Bust! You lose.')
                    players[i]['balance'] -= 1
                    break

        # Dealer


        print('\nDealer\'s turn:')
        while calc_handVal(dealer_hand) < 17:
            dealer_hand.append(deal_card(deck))

        # Showing dealer's hand and value


        print('\nDealer\'s hand:', ', '.join(dealer_hand))
        dealer_value = calc_handVal(dealer_hand)
        print('Dealer\'s hand value:', dealer_value)




        # Determining the winner

        for i in range(num_players):
            player_value = calc_handVal(player_hands[i])
            if dealer_value > 21:
                print(f'{players[i]["name"]} wins! Dealer busts.')
                players[i]['balance'] += 1
            elif dealer_value > player_value:
                print(f'{players[i]["name"]} loses. Dealer wins.')
                players[i]['balance'] -= 1
            elif dealer_value < player_value:
                print(f'{players[i]["name"]} wins!')
                players[i]['balance'] += 1
            else:
                print(f'{players[i]["name"]} ties with the dealer.')







       
        play_again = input('Do you want to play another round (yes/no)? ').strip().lower()
        if play_again != 'yes':
            break



    # Displaying final balances


    print('\nFinal player balances:')
    for i in range(num_players):
        print(f'{players[i]["name"]}: ${players[i]["balance"]}')






if __name__ == "__main__":
    try:
        num_players = int(input('Enter the number of players: '))
        if num_players < 1:
            print('Please enter a valid number of players (at least 1).')
        else:
            play_blackjack(num_players)
    except ValueError:
        print('Invalid input. Please enter a valid number of players.')
