import random

def num():
    return random.randint(1, 6)
def game():
    pp = 0
    while 1:
        input("roll the dice...")
        dice1 = num()
        dice2 = num()
        roll = dice1 + dice2
        print(f"You rolled {roll}")
        if roll == 7 or roll == 11:
            print("You win")
            break
        elif roll == 2 or roll == 3 or roll == 12:
            print("You lose")
            break
        elif pp == 0:
            pp = roll
            print(f'your point is {pp}')
        elif roll == pp:
            print("You win!")
            break
        elif roll == 7:
            print("You lose!")
            break
game()
