print('Welcome to FLASHCARDS EXTREME!!!!')

def START():
    print('What would you like to do? ')
    usrChoice = input('New Card(A) | Play EXTREME(P) | Exit Game(E): ')
    if usrChoice == 'a':
        print('ChangeME')
    elif usrChoice == 'p':
        print('EXTREME')
    elif usrChoice == 'e':
        print('EXIT')
    else:
        print('You did not imnput a correct response')
        print('Please Try Again')
        START()
#Start GAME
START()


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

