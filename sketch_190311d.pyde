import random
napis = ['KULKA', 'DZIEN', 'WODA']
def draw ():
    if mousePressed:
        print(random.choice(napis))
    else:
        print('You have to press')
        
