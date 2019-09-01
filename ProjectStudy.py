import decimal
import threading

print('Welcome to FLASHCARDS EXTREME!!!!')

def START():
    print('What would you like to do? ')
    usrChoice = input('Add New Card(a) | Play EXTREME(p) | Exit Game(e): ')
    if usrChoice == 'a':
        
    elif usrChoice == 'p':
        print('EXTREME')
    elif usrChoice == 'e':
        print('Thanks For Playing!!!')
        exit()
    else:
        print('You did not imnput a correct response')
        print('Please Try Again')
        START()
#Start GAME########################################
START()


class IndexCard:
    def __init__(self,cardFront,cardBack):
        self.cardFront = cardFront
        self.cardBack = cardBack
    # def storeCard(self):
    def viewCard(self):
         print(self.cardFront)
         print(self.cardBack)


# usrInptF = input('Please enter a Term or Phraze ')                    #Erase
# usrInptB = input('Please enter the meaning of ' + usrInptF + ' ')     #Erase

card_One = IndexCard(usrInptF,usrInptB) 
card_One.viewCard()

