from card import Card


class Hand:

    def __init__(self):
        """
        Initializes a hand with an empty list of cards, a value of 0, and no aces.
        """
        self.cards = []
        self.value = 0
        self.aces = 0

    def __str__(self):
        """
        Returns a string representation of the hand, showing all cards in the hand.
        """
        return [card for card in self.cards]

    def add_card(self, new_card: Card):
        """
        Adds a new card to the hand and updates the hand's value.
        If the new card is an Ace, increments the count of aces.
        """
        self.cards.append(new_card)
        self.value += new_card.value
        if new_card.rank == 'Ace':
            self.aces += 1  # add to self.aces

    def adjust_for_ace(self):
        """
        Adjusts the hand's value if it's over 21 and there are aces present.
        """
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


