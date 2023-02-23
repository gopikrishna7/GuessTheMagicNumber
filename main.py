import random
def ask_guess():
    guess=0
    while guess==0:
        try:
            guess = int(input('Please enter the magic number({} to {}) :'.format(MIN_NUM, MAX_NUM)))
            if guess<MIN_NUM or guess>MAX_NUM:
                print("Please enter the value in b/w {} and {}".format(MIN_NUM,MAX_NUM))
                guess=0
        except ValueError:
            print("Error! Please enter the valid input")
    return guess

def check():
    guess=0
    lives = NO_LIFE
    win=False
    while guess!=MAGIC_NUMBER and lives!=0:
        guess= ask_guess()
        if guess==MAGIC_NUMBER:
            print("you are correct")
            win=True
        elif guess<MAGIC_NUMBER:
            if lives==1:
                break
            print("The magic number is greater")
            lives=lives-1
        elif guess>MAGIC_NUMBER:
            if lives==1:
                break
            print("The magic number is less")
            lives=lives-1
    if win==False:
        print("You have lost the game")


MIN_NUM=1
MAX_NUM=10
MAGIC_NUMBER=random.randint(MIN_NUM,MAX_NUM)
NO_LIFE=3

check()