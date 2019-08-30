class IndexCard:
    def __init__(self,cardFront,cardBack):
        self.cardFront = cardFront
        self.cardBack = cardBack
    def viewCard(self):
        print(self.cardFront)
        print(self.cardBack)

usrInptF = input('Please enter a Term or Phraze ')
usrInptB = input('Please enter the meaning of ' + usrInptF + ' ')






card_One = IndexCard(usrInptF,usrInptB) 
card_One.viewCard()

