from hand import Hand
from coins import Coins


class Player:

    def __init__(self):
        """
        Initializes a player with an empty hand and a wallet of coins.
        """
        self.hand = Hand()
        self.coins = Coins()

    def make_bet(self):
        """
        Allows the player to make a bet by inputting an integer value.
        Validates the bet to ensure it's within the valid range
        """
        while True:
            bet_input = input("Make a bet: ")
            try:
                bet = int(bet_input)

                # Check if the bet is within the valid range
                if bet <= 0:
                    print('Bet must be greater than 0.')
                elif bet > self.coins.total:
                    print(f'Not enough coins! You have {self.coins.total} coins.')
                else:
                    # Set the bet and break out of the loop
                    self.coins.bet = bet
                    print(f'Your bet is {bet}!\n')
                    break
            except ValueError:
                print('Not a valid bet. Please enter a valid integer value.')
