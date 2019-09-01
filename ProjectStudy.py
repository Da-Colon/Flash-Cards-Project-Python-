import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

cprint(figlet_format('Flash Cards ExTREME!', font='starwars'),
       'yellow', 'on_grey', attrs=['bold'])


class IndexCard:
    def __init__(self, card):
        self.card = card
        self.card_front = []
        self.card_back = []
    def add_card(self, front, back):
        self.card_front.append(front)
        self.card_back.append(back)
    

card_dict = {}
def START():
    print('What would you like to do? ')
    usrChoice = input('Add New Card(a) | Play EXTREME(p) | Exit Game(e): ')
    if usrChoice == 'a':
        #add a loop with? if to increment new card)
        c = IndexCard('001')
        c.add_card(input('front: '), input('back: '))
        START()
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





