from enum import Enum


class Card:
    def __init__(self, char):
        self.name = char
        if self.name.isdigit():
            self.value = int(self.name)
        else:
            match self.name:
                case 'T':
                    self.value = 10
                case 'J':
                    self.value = 11
                case 'Q':
                    self.value = 12
                case 'K':
                    self.value = 13
                case 'A':
                    self.value = 14
                case _:
                    self.value = 0

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return self.name

    __repr__ = __str__


class Type(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_KIND = 6
    FIVE_OF_KIND = 7


class Hand:
    def __init__(self, cards, bid):

        self.cards = []
        self.frequency = {}
        self.type = ''

        for card in cards:
            self.cards.append(Card(card))

        self.bid = bid

        for card in self.cards:
            if card.name in self.frequency:
                self.frequency[card.name] = self.frequency.get(card.name) + 1
            else:
                self.frequency.update({card.name: 1})

        self.most_freq_card = max(self.frequency, key=self.frequency.get)
        self.highest_freq = self.frequency[self.most_freq_card]

        match self.highest_freq:
            case 5:
                self.type = 'FIVE_OF_KIND'
            case 4:
                self.type = 'FOUR_OF_KIND'
            case 3:
                self.type = 'FULL_HOUSE' if 2 in self.frequency.values() else 'THREE_OF_KIND'
            case 2:
                self.type = 'TWO_PAIR' if list(self.frequency.values()).count(2) == 2 else 'ONE_PAIR'
            case 1:
                self.type = 'HIGH_CARD'

    def __lt__(self, other):
        if self.type == other.type:
            i = 0
            while i < len(self.cards):
                if self.cards[i] == other.cards[i]:
                    i += 1
                else:
                    return self.cards[i] < other.cards[i]
        else:
            return Type[self.type].value < Type[other.type].value

    def __str__(self):  # for debugging
        return str(self.cards) + " " + str(self.frequency) + " " + self.type + " (" + str(Type[self.type].value) + ")"

    __repr__ = __str__


def day_7(filename):
    winnings = 0

    text = open(filename, 'r')
    lines = text.readlines()

    hands = []

    for line in lines:
        hands.append(Hand([*line.split(' ')[0].rstrip()], int(line.split(' ')[1].rstrip())))

    hands.sort()

    for i, hand in enumerate(hands):
        # print(str(hand) + " " + str(hand.bid) + " * " + str(i + 1))
        winnings += hand.bid * (i + 1)

    return winnings
