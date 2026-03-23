import random

def roll_dice():
    dice_total = random.randint(1, 6) + random.randint(1, 6)
    return dice_total

def main():

    player1 = input('Enter name P1\n')
    player2 = input('Enter name P2\n')

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(player1, 'rolled', roll1)
    print(player2, 'rolled', roll2)

    if roll1 > roll2:
        prnt(player1, 'wins!')
    elif roll2 > roll1:
        print(player2, 'wins!')
    else:
        print('TIE')

main()