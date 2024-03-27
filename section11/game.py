from hand import Hand
from deck import Deck
from player import Player


def hit(deck: Deck, hand: Hand):
    """
       Function to deal a card from the deck and adjust the hand's value for Aces.
    """
    hand.add_card(deck.deal_one())
    hand.adjust_for_ace()


def start_deal(deck: Deck, dealer_hand: Hand, player: Player):
    """
       Initial dealing of cards for both player and dealer.
    """
    for num in range(2):
        hit(deck, player.hand)
        hit(deck, dealer_hand)


def is_player_chose_hit():
    """
       Function to prompt the player for hitting or standing.
    """
    while True:
        player_choice = input("Hit or Stand [H/S]? ").upper()
        if player_choice == 'H':
            return True
        elif player_choice == 'S':
            return False
        else:
            print('Invalid input! Please choose H for Hit or S for Stand.')


def player_lose(player: Player):
    """
        Function to handle player losing the round.
    """
    player.coins.lose_bet()
    print(f'\nPlayer Lost! Total coins: {player.coins.total}')


def player_win(player: Player):
    """
        Function to handle player winning the round.
    """
    player.coins.win_bet()
    print(f'\nPlayer Won! Total coins: {player.coins.total}')


def dealer_win(player):
    """
        Function to handle dealer winning the round.
    """
    player.coins.lose_bet()
    print(f"\nDealer Wins! Player's Total coins: {player.coins.total}")


def show_hands(dealer_hand: Hand, player_hand: Hand, players_turn=False):
    """
        Function to display hands.
    """
    dealer_cards = [str(card) for card in dealer_hand.cards]
    if players_turn:
        dealer_cards[1] = '<Secret Card>'
    print(f"Player Hand: {[str(card) for card in player_hand.cards]} Sum: {player_hand.value}")
    print(f"Dealer Hand: {dealer_cards} Sum: {dealer_hand.value}")


def start_game():

    deck = Deck()
    deck.shuffle()

    dealer_hand = Hand()
    player = Player()

    # Make a bet before starting the game
    player.make_bet()

    # Initial deal
    start_deal(deck, dealer_hand, player)
    show_hands(dealer_hand, player.hand, True)
    player_game_on = True

    while player_game_on and player.hand.value != 21:

        if is_player_chose_hit():
            # Player chose to hit
            hit(deck, player.hand)
            show_hands(dealer_hand, player.hand, True)
        else:
            # Player chose to stand
            print('\nReveal secret card:')
            player_game_on = False

        if player.hand.value > 21:
            # Player busts
            player_lose(player)
            player_game_on = False

    if player.hand.value <= 21:
        # Player didn't bust, dealer's turn
        show_hands(dealer_hand, player.hand)

        while dealer_hand.value <= player.hand.value < 21:
            print("\nDealer Turn: ")
            hit(deck, dealer_hand)
            show_hands(dealer_hand, player.hand)

            if dealer_hand.value > 21 >= player.hand.value:
                # Dealer busts, player wins
                player_win(player)
                break

        if player.hand.value < dealer_hand.value <= 21:
            # Dealer wins
            dealer_win(player)
        elif player.hand.value == 21 and dealer_hand.value == 21:
            # Tie
            print(f'\nTie! Total coins: {player.coins.total}')


if __name__ == "__main__":
    start_game()
