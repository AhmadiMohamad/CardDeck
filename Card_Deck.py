import collections

Card = collections.namedtuple("Card",['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list("JQKA")
    suits = 'spades dimonds clubs hearts'.split()
    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self,position):
        return self._cards[position]
    

suit_values = dict(spades=3,hearts=2,dimonds=1,clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

ali = FrenchDeck()

for counter,card in enumerate(sorted(ali,key=spades_high)):
    print(counter+1,card)