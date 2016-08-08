from random import randint

def lines():
    print "----------------------------------------"




def dice_roll_game():

    player_dice_roll1 = randint(1, 10)
    andoar_dice_roll1 = randint(1, 10)
    player_dice_roll2 = randint(1, 10)
    andoar_dice_roll2 = randint(1, 10)
    player_dice_roll3 = randint(1, 10)
    andoar_dice_roll3 = randint(1, 10)
    player_total = 0
    andoar_total = 0
    lines()
    print "First roll: "
    print "You roll: %s" % player_dice_roll1
    print "Andoar rolls: %s" % andoar_dice_roll1
    player_total += player_dice_roll1
    andoar_total += andoar_dice_roll1
    lines()
    print "Second roll: "
    print "You roll: %s" % player_dice_roll2
    print "Andoar rolls: %s" % andoar_dice_roll2
    player_total += player_dice_roll2
    andoar_total += andoar_dice_roll2
    lines()
    print "Third roll: "
    print "You roll: %s" % player_dice_roll3
    print "Andoar rolls: %s" % andoar_dice_roll3
    player_total += player_dice_roll3
    andoar_total += andoar_dice_roll3
    lines()
    print "Your final score: %s" % player_total
    print "Andoar's final score: %s" % andoar_total
    if player_total > andoar_total:
        print "You won!"
    elif player_total < andoar_total:
        print "You lost!"
    else:
        print "It's a draw! You will roll until one of you rolls more than the other!"
        while player_total == andoar_total:
            you_roll = randint(1,10)
            andoar_roll = randint(1,10)
            print "You roll: %s" % you_roll
            print "Andoar rolls: %s " % andoar_roll
            if you_roll > andoar_roll:
                print "You've won!"
            else:
                print "You've lost!"
