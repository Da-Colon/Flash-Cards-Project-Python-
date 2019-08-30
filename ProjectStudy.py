class IndexCard:
    def __init__(self,cardFront,cardBack):
        self.cardFront = cardFront
        self.cardBack = cardBack
    def viewCard(self):
        print(self.cardFront)
        print(self.cardBack)

Card001 = IndexCard('This is the Front','This is the back')
Card001.viewCard()
