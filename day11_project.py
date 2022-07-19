import art
import random


print(art.logo)

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10] # Cards with a proportion of 4 that represents a deck.
random.shuffle(cards)

#* Standard Deck Of 52 Cards.
std_deck = [] # Standard Deck of 52 cards
for std in range(0,4): 
    std_deck.extend(cards)


#* The dealer shuffle the standard deck.
random.shuffle(std_deck) 
random.shuffle(std_deck) 
random.shuffle(std_deck)

#* The dealer give the firt hand (two cards) to the gambler player. Then, the dealer pick two cards (one side down).
players_hands = {
    "gambler": [std_deck[0], std_deck[1]], # First two cards of the shuffle list to the gambler.
    "dealer": [std_deck[2], std_deck[3]] #! The second element of the list cannot be shown to the gambler player if they decide to hit another card.
}

def blackjack(player__hands):
    

# TODO Print the gambler & dealer hands

#? I want to include an Unicode Representation of the player hands in order to improve the user experience.




# TODO Give the gambler the option to 'hit' another card or to 'stand'  