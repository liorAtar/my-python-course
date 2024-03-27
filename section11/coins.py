class Coins:

    def __init__(self):
        """
        Initializes the Coins object with a total number of coins and a bet amount.
        """
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        """
        Increases the total number of coins by the amount of the current bet when the player wins.
        """
        self.total += self.bet

    def lose_bet(self):
        """
        Decreases the total number of coins by the amount of the current bet when the player loses.
        """
        self.total -= self.bet
