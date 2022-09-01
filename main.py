import Card_class


def is_pair(hand: Card_class.Hand):
    for i in range(len(hand.cards) - 1):
        for j in range(i + 1, len(hand.cards)):
            if hand.cards[i].rank == hand.cards[j].rank:
                return True
    return False


def is_two_pair(hand: Card_class.Hand):
    pairs = 0
    pairs_rank = None
    for i in range(len(hand.cards) - 1):
        for j in range(i + 1, len(hand.cards)):
            if (hand.cards[i].rank == hand.cards[j].rank) and (pairs_rank != hand.cards[i].rank):
                pairs += 1
                pairs_rank = hand.cards[i].rank
            if pairs >= 2:
                return True
    return False


def is_three(hand: Card_class.Hand):
    for i in range(len(hand.cards) - 1):
        count = 1
        for j in range(i + 1, len(hand.cards)):
            if hand.cards[i].rank == hand.cards[j].rank:
                count += 1
            if count == 3:
                return True
    return False


def is_straight(hand: Card_class.Hand):
    # sort list then check if sequential
    card_list = []
    for card in hand.cards:
        card_list.append(card.rank)
    card_list.sort()
    if card_list[0] == 1 and card_list[1] == 10 and card_list[2] == 11 and card_list[3] == 12 and card_list[4] == 13:
        return True
    for i in range(1, len(card_list)):
        if card_list[0] + i != card_list[i]:
            return False
        return True


def is_flush(hand: Card_class.Hand):
    for i in range(len(hand.cards)):
        count = 1
        for j in range(i+1, len(hand.cards)):
            if hand.cards[i].suit == hand.cards[j].suit:
                count += 1
            if count == 5:
                return True
    return False


def is_full_house(hand: Card_class.Hand):
    if is_two_pair(hand) and is_three(hand):
        return True
    else:
        return False


def is_four(hand: Card_class.Hand):
    for i in range(len(hand.cards) - 1):
        count = 1
        for j in range(i + 1, len(hand.cards)):
            if hand.cards[i].rank == hand.cards[j].rank:
                count += 1
            if count == 4:
                return True
    return False


def is_straight_flush(hand: Card_class.Hand):
    if is_straight(hand) and is_flush(hand):
        return True
    else:
        return False

def score(hand: Card_class.Hand):
    if is_straight_flush(hand):
        return 8
    elif is_four(hand):
        return 7
    elif is_full_house(hand):
        return 6
    elif

card1 = Card_class.Card(Card_class.Suit.Hearts, Card_class.Rank.Ace)
card2 = Card_class.Card(Card_class.Suit.Hearts, Card_class.Rank.Queen)
card3 = Card_class.Card(Card_class.Suit.Hearts, Card_class.Rank.Ten)
card4 = Card_class.Card(Card_class.Suit.Hearts, Card_class.Rank.King)
card5 = Card_class.Card(Card_class.Suit.Hearts, Card_class.Rank.Jack)
hand1 = Card_class.Hand()
hand1.cards.extend([card1, card2, card3, card4, card5])

print(hand1)
print(is_straight_flush(hand1))
