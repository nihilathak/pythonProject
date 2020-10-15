import random

#def str_append(length, character):
    #print()

#Fail Drawings
# Fail 1
fail1 = "----------| \n|\n|\n|\n|\n|\n|"
# Fail 2
fail2 = "----------| \n|         | \n|\n|\n|\n|\n|"
# Fail 3
fail3 = "----------| \n|         | \n|         0\n|\n|\n|\n|"
# Fail 4
fail4 = "----------| \n|         | \n|         0\n|       / | \ \n|\n|"
# Fail 5
fail5 = "----------| \n|         | \n|         0\n|       / | \ \n|         |\n|"
# Fail 6
fail6 = "----------| \n|         | \n|         0\n|       / | \ \n|         |\n|        / \ "


words = ["filename", "fart", "matter", "dog"]

print("Welcome to Lynchman! Where we build a noose out of your mistakes!")

word_picker = random.randint(0,3)

picked_word = words[word_picker]

print("A word has been picked! It contains " + str(len(picked_word)) + " letters")

#game_status = True
fault_tracker = 5


guess_tracker = []
blanks = '_' * len(picked_word)
win_tracker = False

while fault_tracker != 0 and blanks != picked_word:

    guess = str(input("Please guess 1 letter: "))
    guess.lower()
    guess_tracker.append(guess)

    if guess in picked_word:
        print(picked_word.find(guess))
        print("Good! That is a correct letter.")

        for i in range(len(picked_word)):  # Replace blanks with correctly
            if picked_word[i] in guess_tracker:
                blanks = blanks[:i] + picked_word[i] + blanks[i+1:]

    else:
        fault_tracker -= 1
        print("WRONG! You have " + str(fault_tracker) +  " chance/s left. The letter " + guess + " is not contained in the secret word")



    if fault_tracker == 5:
        print(fail1)
        print("\nSecret Word: " + blanks)
    elif fault_tracker == 4:
        print(fail2)
        print("\nSecret Word: " + blanks)
    elif fault_tracker == 3:
        print(fail3)
        print("\nSecret Word: " + blanks)
    elif fault_tracker == 2:
        print(fail4)
        print("\nSecret Word: " + blanks)
    elif fault_tracker == 1:
        print(fail5)
        print("\nSecret Word: " + blanks)
    elif fault_tracker == 0:
        print(fail6)
        print("\nSecret Word: " + blanks)

    print("Your guesses so far: ")
    print(*guess_tracker, sep = ", ")


if fault_tracker == 0:
    print("You failed! The justice system prevails!")
else:
    print("Congrats! Another Biden voter has been released!")