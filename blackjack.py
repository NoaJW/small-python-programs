# Qns: https://inventwithpython.com/bigbookpython/project4.html

# TODO: Double down only on first move

import itertools, random

suits = {"HEART":chr(9829), "DIAMOND": chr(9830), "SPADE": chr(9824), "CLUB": chr(9827)}
specials = {1: "A", 11: "J", 12: "Q", 13: "K"}


def main(): 
    print("""
    Rules:
        Try to get as close to 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.
    """)

    money = 5000       
    dealer_hand = []
    player_hand = []
    # Deck of 52 cards. Shuffle 
    deck = list(itertools.product(range(1,14),['SPADE','HEART','DIAMOND','CLUB']))
    random.shuffle(deck)
    player_end = False
    replay = True
    replay_val = None
    break_flag = False

    while replay: 
        print("Money: ${}".format(money))
        # Player place bet amount  
        bet = place_bet(money)
        
        if bet: 
            print("Bet: ${}".format(bet))

            # Draw 2 cards for player and dealer initially
            for i in range(2): 
                dealer_hand.append(draw_card(deck))
                player_hand.append(draw_card(deck))

            print("\n== PLAYER'S TURN ==")
            while player_end == False: 
                # Check if player has bust
                if get_cards_value(player_hand) > 21: 
                    display_cards(dealer_hand)
                    display_cards(player_hand)
                    print("\nYou have bust!")
                    print("You lost ${}!".format(bet))
                    money -= bet 
                    break_flag = True
                    break

                print("\nDEALER: ???")
                display_cards(dealer_hand, True)
                print("\nPLAYER: {}".format(get_cards_value(player_hand)))
                display_cards(player_hand)

                # Player's next move 
                while True: 
                    print("\n(H)it, (S)tand, (D)ouble down")
                    move = input("> ")
                    if move.upper() in ['H', 'S', 'D']: 
                        if (move.upper() == 'D') and (bet * 2) > money:
                            print("Not enough money to double down")
                            continue
                        else: 
                            break
                    else: 
                        print("Invalid input")

                # Hit 
                if move.upper() == 'H':
                    drawn_card = draw_card(deck)
                    num, suit = drawn_card
                    suit = suits.get(suit)
                    if num in specials: 
                        num = specials.get(num)
                    print("\nYou drew a {} of {}".format(num, suit))
                    player_hand.append(drawn_card)
                # Stand
                elif move.upper() == 'S': 
                    player_end = True
                # Double down 
                else: 
                    # Double bet amount
                    bet *= 2    
                    print("\nBet amount doubled to ${}".format(bet))
                    # Draw 1 more card only
                    player_hand.append(draw_card(deck))
                    player_end = True

            # Ask for replay if player lost (bust)
            if break_flag: 
                replay_val = replay_fn(money)
                if replay_val == False: 
                    replay = False
                    break
                else:
                    money, dealer_hand, player_hand, deck, player_end, break_flag = replay_val
                    continue

            print("\n== DEALER'S TURN ==")
            print("\nDEALER: {}".format(get_cards_value(dealer_hand)))
            display_cards(dealer_hand)
            display_cards(player_hand)
            print("\nPLAYER: {}".format(get_cards_value(player_hand)))
            
            # Dealer has to draw as long as his hand value <= 17
            while get_cards_value(dealer_hand) <= 17: 
                drawn_card = draw_card(deck)
                num, suit = drawn_card
                suit = suits.get(suit)
                if num in specials: 
                    num = specials.get(num)
                print("\nDealer drew a {} of {}".format(num, suit))
                dealer_hand.append(drawn_card)
            
                print("\nDEALER: {}".format(get_cards_value(dealer_hand)))
                display_cards(dealer_hand)
                display_cards(player_hand)
                print("\nPLAYER: {}".format(get_cards_value(player_hand)))

            # Check if dealer has bust
            if get_cards_value(dealer_hand) > 21:
                print("\nDealer has bust!")
                print("You won ${}!".format(bet))
                money += bet

                # Ask for replay if dealer bust
                replay_val = replay_fn(money)
                if replay_val == False: 
                    replay = False
                    break
                else:
                    money, dealer_hand, player_hand, deck, player_end, break_flag = replay_val
                    continue
                    
            # Compare values 
            if get_cards_value(player_hand) > get_cards_value(dealer_hand):
                print("\nYou won ${}!".format(bet))
                money += bet
            elif get_cards_value(player_hand) < get_cards_value(dealer_hand):
                print("\nYou lost ${}!".format(bet))
                money -= bet
            else: 
                print("\nIt's a tie!")

            # Ask for replay on end of round
            replay_val = replay_fn(money)
            if replay_val == False: 
                replay = False
                break
            else:
                money, dealer_hand, player_hand, deck, player_end, break_flag = replay_val


def get_cards_value(hand): 
    aces = 0
    cards_value = 0

    for index in range(len(hand)):
        card_value = hand[index][0]

        # Check if num is a special value (A, J, Q or K)
        if card_value in specials:
            # Jack, Queen and King have value of 10 each 
            if card_value in [11, 12, 13]: 
                card_value = 10
                cards_value += card_value
            else:   # Ace
                aces += 1   # Add ace value 1 first for optimising its value later 
                cards_value += 1
        else:       # Normal value (2 - 10)
            cards_value += card_value

    # Ace value can be 1 or 11 depending on the value of the hand. Optimise to ensure that it does not bust 
    if aces >= 1: 
        multiple = int((21 - cards_value) / 10)  
        cards_value += multiple * 10    # multiple can be max 1 as the smallest hand is 2 aces  

    return cards_value


def draw_card(deck):    
    card = deck.pop()
    return card         


def display_cards(hand, hide_first=False):
    rows = ["", "", "", ""]     # Empty strings to access their indexes 
    
    # Dealer's face-down card, initially, before his turn
    if hide_first:
        hand = hand[1:]
        rows[0] += " ___ "
        rows[1] += "|## |"
        rows[2] += "|###|"
        rows[3] += "|_##|"

    for card in hand:
        num, suit = card

        suit = suits.get(suit)
        if num in specials: 
            num = specials.get(num)

        rows[0] += " ___  "
        rows[1] += "|{} | ".format(str(num).ljust(2))
        rows[2] += "| {} | ".format(suit)
        rows[3] += "|_{}| ".format(str(num).rjust(2, '_'))
    
    for row in rows:
        print(row)
        
          
def place_bet(money):
    print("How much do you bet? (1-5000, or QUIT)")
    while True: 
        bet = input("> ")

        if bet.isdecimal(): 
            if (int(bet) <= money): 
                return int(bet)
            else: 
                print("Not enough money!") 
                continue
        else:       # Exit out of program on QUIT or other non-decimal input
            print("Quitting...")
            return 


def replay_fn(money): 
    print("\nPlay again? (Y or N)")
    replay = input("> ")

    if replay.upper() == 'Y':
        dealer_hand = []
        player_hand = []
        deck = list(itertools.product(range(1,14),['SPADE','HEART','DIAMOND','CLUB']))
        random.shuffle(deck)
        player_end = False
        break_flag = False
        
        while True: 
            print("Reset money or continue with remaining money (1 - Reset, or 2 - Continue)")
            money_reset = input("> ")

            if money_reset == '1' or money == 0:    # Reset money on player's choice or if there is no money left
                money = 5000
                return money, dealer_hand, player_hand, deck, player_end, break_flag
            elif money_reset == '2':
                return money, dealer_hand, player_hand, deck, player_end, break_flag
            else: 
                print("Invalid input.")
                continue
    else: 
        print("Quitting...")
        return False


if __name__ == '__main__':
    main()