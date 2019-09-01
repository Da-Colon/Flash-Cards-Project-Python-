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
        self.card_front = '\n'
        self.card_back = '\n'
    def add_card(self, front, back):
        cf = []
        cb = []
        cf = self.card_front.join(front)
        cb = self.card_back.join(back)
        stored = open('stored_card.txt' , 'w')
        stored.write(cf)
        stored.write(cb)
        stored.close()

c = IndexCard('001')
def START():
    print('What would you like to do? ')
    usr_choice = input('Add New Card(a) | Play EXTREME(p) | Exit Game(e): ')
    if usr_choice == 'a':
        #add a loop with? if to increment new card)
        c.add_card(input('front: '), input('back: '))
        START()
    elif usr_choice == 'p':
        print(f'front: {c.card_front}') 
        print(f'back: {c.card_back}' )
    elif usr_choice == 'e':
        cprint(figlet_format('Thanks For Playing!!', font="standard"), 'red', 'on_grey', attrs=['bold'])
        exit()
    else:
        print('You did not imnput a correct response')
        print('Please Try Again')
        START()

START()

def read_file():
    stored_read = open('stored_card.txt', 'r')
    card = stored_read.read()
    stored_read.close()
    print(card)
read_file()
