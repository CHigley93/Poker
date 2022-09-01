import random
from enum import Enum, auto, IntEnum


class Suit(Enum):
    Clubs = auto()
    Diamonds = auto()
    Hearts = auto()
    Spades = auto()


class Rank(IntEnum):
    Ace = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13


class Card:
    # Initialize the card with valid rank and suit
    def __init__(self, suit: Suit, rank: Rank):
        # check if suit is valid and raise an error if not
        if not isinstance(suit, Suit):
            raise ValueError(f"{suit} is not a valid Suit.")
        self.suit = suit
        # check if rank is valid and raise an error if not
        if not isinstance(rank, Rank):
            raise ValueError(f"{rank} is not a valid Rank.")
        self.rank = rank
        self.value = [suit, rank]

    def __str__(self):
        return self.rank.name + " of " + self.suit.name


class Deck:

    # Initialize a standard 52 card deck
    def __init__(self):
        self.cards = []
        for s in Suit:
            for r in Rank:
                self.cards.append(Card(s, r))

    # Change __str__ method so that the deck prints out each card with 13 cards per line
    def __str__(self):
        names = ""
        count = 0
        for card in self.cards:
            names += str(card) + ", "
            count += 1
            if count % 13 == 0:
                names += "\n"
        return names

    # shuffle method to randomly shuffle the order of cards
    def shuffle(self):
        random.shuffle(self.cards)

    # deal method to remove cards from deck and return them as a list
    def deal(self, num: int):
        dealt = []
        if type(num) != int or num < 1:
            raise ValueError("You must choose a positive integer value")
        elif num > len(self.cards):
            raise ValueError("There aren't that many cards to deal")
        else:
            while num > 0:
                dealt.append(self.cards[0])
                del self.cards[0]
                num -= 1
            return dealt


class Hand(Deck):
    # create an empty list for cards to be put in
    def __init__(self, wager=0):
        super().__init__()
        self.cards = []
        self.wager = wager
