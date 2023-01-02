# Creates a deck of cards that can be shuffles and delt
from random import shuffle


class Deck:
    """Creates a deck of cards using the Cards class"""

    def __init__(self):
        """Creates a standard deck of cards"""
        suits = ("Hearts", "Diamonds", "Spades", "Clubs")
        values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
        self.deck_of_cards = [Card(value, suit) for suit in suits for value in values]
        # self.deck_of_cards = []
        # for suit in suits:
        #     for value in values:
        #         self.deck_of_cards.append(Card(value, suit))

    def __repr__(self):
        """returns amount of cards in the deck"""
        return f"Deck of {self.count()} cards"

    def count(self):
        """Displays how many cards are in the deck"""
        return len(self.deck_of_cards)

    def _deal(self, amount):
        """Deals amount of entered cards"""
        count = self.count()
        # Checks if there are enough cards in the deck to deal the entered amount
        if amount == 0:
            raise ValueError("There are no cards left in the deck!")
        elif amount > count:
            raise ValueError(f"There are only {count} left in the deck!")

        delt_cards = self.deck_of_cards[-amount:]
        self.deck_of_cards = self.deck_of_cards[:-amount]
        return delt_cards

    def shuffle(self):
        """Shuffles deck"""
        if self.count() != 52:
            raise ValueError("Only full decks can be shuffled")

        shuffle(self.deck_of_cards)
        return self

    def deal_card(self):
        """Deals a single card from the deck"""
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        """Deals a hand with the entered amount of cards"""
        return self._deal(hand_size)


class Card:
    """Creates cards with a specific suit and value"""

    def __init__(self, value, suit):
        """Creates a card with a specific suit and value"""
        self._value = value.upper()
        self._suit = suit

    def __repr__(self):
        """Displays card's value and suit"""
        return f"{self._value} of {self._suit}"


# d = Deck()
# d.shuffle()
# card = d.deal_card()
# print(card)
# hand = d.deal_hand(50)
# card2 = d.deal_card()
# print(card2)
# print(d.deck_of_cards)

