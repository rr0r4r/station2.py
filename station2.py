from random import randrange

def game():
    dice1 = randrange(1,6)
    dice2 = randrange(1,6)
    num = dice1 + dice2
    print(f'you rolled {num}')
    if(num == 7 or num == 11):
        print("you won")
    elif(num == 2 or num == 3 or num == 12):
        print("you lose")
    else:
        print(f"your goal  is {num}")
        i = num
        aa = 0
        while (i != aa) :
            dice1 = randrange(1,6)
            dice2 = randrange(1,6)
            aa = dice1 + dice2
            print(f"you rolled {aa}")
            if(aa == 7):
                print("you lose")
                break 
        if(aa != 7):
            print("you won")


game()
