import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]


# # con este primer metodo se consigue un array asociativo:
#     def __len__(self):
#         return len(self._cards)


# con este segundo metodo se provee una representacion para mostrar en pantalla


    def __getitem__(self, position):
         return self._cards[position]

if __name__ == "__main__":
    deck = FrenchDeck()
    #print(deck._cards)
         
    #Iterar sobre las cartas e imprimirlas
    for card in deck:
      print(f'{card.rank} of {card.suit}')
