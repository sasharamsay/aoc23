from enum import Enum


class Card:
    def __init__(self, char, joker):
        self.name = char
        if self.name.isdigit():
            self.value = int(self.name)
        else:
            match self.name:
                case 'T':
                    self.value = 10
                case 'J':
                    self.value = 11 if joker is False else 1
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
    def __init__(self, cards, bid, joker):

        self.cards = []
        self.frequency = {}
        self.type = ''
        self.bid = bid

        for card in cards:
            self.cards.append(Card(card, joker))

        j = 0
        for card in self.cards:
            if joker and card.name == 'J':
                j += 1
            elif card.name in self.frequency:
                self.frequency[card.name] = self.frequency.get(card.name) + 1
            else:
                self.frequency.update({card.name: 1})
        if joker and j == 5:
            self.frequency.update({'J': 5})
            self.most_freq_card = 'J'
            self.highest_freq = 5
        elif joker and j > 0:
            self.most_freq_card = max(self.frequency, key=self.frequency.get)
            self.frequency[self.most_freq_card] = self.frequency.get(self.most_freq_card) + j
            self.highest_freq = self.frequency[self.most_freq_card]
        else:
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
            case _:
                self.type = 'NO'

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


def get_winnings(lines, joker):
    winnings = 0
    hands = []

    for line in lines:
        hands.append(Hand([*line.split(' ')[0].rstrip()], int(line.split(' ')[1].rstrip()), joker))

    hands.sort()

    for i, hand in enumerate(hands):
        # print(str(hand) + " " + str(hand.bid) + " * " + str(i + 1))
        winnings += hand.bid * (i + 1)

    return winnings


def day_7(filename):
    text = open(filename, 'r')
    lines = text.readlines()

    return get_winnings(lines, False)


def day_7_part_2(filename):
    text = open(filename, 'r')
    lines = text.readlines()

    return get_winnings(lines, True)
