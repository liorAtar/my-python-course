suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

import random
from card import Card


class Deck:

    def __init__(self):
        """
        Initializes a deck of cards by creating a list containing all 52 cards in a standard deck.
        """
        # Note this only happens once upon creation of a new Deck
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        """
        Shuffles the deck by randomizing the order of cards.
        """
        random.shuffle(self.all_cards)

    def deal_one(self):
        """
        Deals one card from the deck by removing and returning the top card.
        """
        return self.all_cards.pop()
