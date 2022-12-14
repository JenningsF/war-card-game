import random
import time
suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":11, "Queen":12, "King":13, "Ace":14}

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Creating Card object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_card(self, new_cards):
        # Adds a list of cards
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        # Adds a single card
        else:
            self.all_cards.append(new_cards)

    def __str__(self) -> str:
        return f"Player {self.name} has {len(self.all_cards)}"

# Game Setup
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_card(new_deck.deal_one())
    player_two.add_card(new_deck.deal_one())

game_on = True
round_num = 0
secs = 0

print("""

888       888        d8888 8888888b.  
888   o   888       d88888 888   Y88b 
888  d8b  888      d88P888 888    888 
888 d888b 888     d88P 888 888   d88P 
888d88888b888    d88P  888 8888888P"  
88888P Y88888   d88P   888 888 T88b   
8888P   Y8888  d8888888888 888  T88b  
888P     Y888 d88P     888 888   T88b 

""")

while game_on:
    round_num += 1
    print(f"Round {round_num} | {player_one} | {player_two}")
    # print(player_one)
    # print(player_two)

    if len(player_one.all_cards) == 0:
        print("Player One is out of cards! Player Two Wins!")
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print("Player Two is out of cards! Player One Wins!")
        game_on = False
        break

    # Start a new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            print(f"{player_one_cards[-1]} vs. {player_two_cards[-1]}")
            if len(player_two_cards) > 1:
                print(f"Player One wins the round to add {len(player_two_cards)} cards\n")
            else:
                print(f"Player One wins the round to add {len(player_two_cards)} card\n")
            player_one.add_card(player_one_cards)
            player_one.add_card(player_two_cards)
            at_war = False
        elif player_two_cards[-1].value > player_one_cards[-1].value:
            print(f"{player_one_cards[-1]} vs. {player_two_cards[-1]}")
            if len(player_one_cards) > 1:
                print(f"Player Two wins the round to add {len(player_one_cards)} cards\n")
            else:
                print(f"Player Two wins the round to add {len(player_one_cards)} card\n")
            player_two.add_card(player_two_cards)
            player_two.add_card(player_one_cards)
            
            at_war = False
        else:
            print(f"{player_one_cards[-1]} vs. {player_two_cards[-1]}")
            print("WAR!")

            if len(player_one.all_cards) < 3:
                print("Player One is unable to declare War!")
                print("Player Two Wins! after")
                game_on = False
                break
            elif len(player_two.all_cards) < 3:
                print("Player Two is unable to declare War!")
                print("Player One Wins!")
                game_on = False
                break
            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
                    print(f"{num + 1}", end='', flush=True)
                    for num in range(2):
                        print('.', end='', flush=True)
                        time.sleep(secs / 3)
                # print("\n")
    time.sleep(secs)