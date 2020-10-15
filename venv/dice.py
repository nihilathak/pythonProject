import random

def roll_dice(size):
    return random.randint(1, size)

yes = "yes"

while yes == "yes":

    yes = input("Do you want to roll some new dice? yes or no?: ")

    dice_size = int(input("How many sides should the dice have?: "))

    dice_size = dice_size + 1

    roll_again = "yes"

    while roll_again == "yes" and yes == "yes":
        val1 = roll_dice(dice_size)
        val2 = roll_dice(dice_size)

        print("Dice 1: " + str(val1) + "\nDice 2: " + str(val2))

        roll_again = input("Roll same dice again?: ")