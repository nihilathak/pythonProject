
char_name = "John"

print("Hello\"World")
print("Hello "+ char_name + ", ")

char_name = "test"

print("Hello World")
print("Hello "+ char_name + ", ")

test_var = 50
boo_var = True
if test_var >= 10:
    print("success")
    boo_var = False

print(boo_var)

print(len(char_name.upper()))

yes = "yes"

-------------------------------------------------
while yes == "yes":

    var = input("provide a number: ")
    var1 = input("another number cunt: ")

    test = float(var) + float(var1)

    print(test)
    yes = input("do you want to do more math? yes or no: ")

-------------------------------------------------
list = [1, "var", False, "dood"]

yes = "yes"

while yes == "yes":
    usr = int(input("lets adjust this list, which position do you want to adjust?: "))

    print("okay we will adjust " + str(usr) + " position")

    usr_val = input("what do you want to put there nigga?: ")

    print("cool i will place " + str(usr_val) + " at " + str(usr))

    usr = int(usr)

    list[usr] = usr_val

    print(str(list[0:]))

    yes = input("do you want to continue?: ")


-------------------------------------------------

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= 3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

def math_add(var1, var2):
    return var1 + var2
    #print("result:" + var3)

def math_sub(var1, var2):
    return var1 + var2
    #print("result:" + var3)

def math_mult(var1, var2):
    return var1 * var2

def math_div(var1, var2):
    return var1 / var2

def exp (base, pow):
    return base**pow

def exp_loop(base, pow)
    result = 1
    for index in range(pow):
        result = result * base

yes = "yes"

while yes == "yes":

    op = input("lets do some math: add, sub, mult, div?: ")
    var1 = float(input("value 1: "))
    var2 = float(input("value 2: "))

    if op == "add":
        print(math_add(var1, var2))
    elif op == "sub":
        print(math_sub(var1, var2))
    elif op == "mult":
        print(math_mult(var1, var2))
    elif op == "div":
        print(math_div(var1, var2))
    else:
        print("invalid operator")

    yes = input("anymore or try again?: ")

print("cant even math yourself loser")

-----------------------------------------------
monthConversions = {

    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
}


print(monthConversions["Jan"])
print(monthConversions.get("dfs", "Not valid"))

--------------------------------------------------

sec_word = "guess"
guess = ""

while guess != sec_word:
    guess = input("Enter the secret word: ")

print("Yep u got it: " + sec_word)

----------------------------------------------------

sec_word = "guess"
guess = ""

print("you got 3 chances to get the word right, or SHE DIES!")
count = 0
limit = 3
out = False

while guess != sec_word and not(out):
    if count < limit:
        guess = input("Enter the secret word: ")
        count += 1
        print("Attempts: " + str(count))
    else:
        out = True

if out:
    print("She ded, the word was: " + sec_word)
else:
    print("She lives! Word was: " + sec_word)

------------------------------------------------

values = [1, "var", False, "dood"]

for value in values:
    print(value)

for index in range(len(values)):
    print(values[index])

-----------------------------------------------------
num_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(num_grid[2][1])

for row in num_grid:
    for col in row:
        print(col)

------------------------------------------------------
def translate_grif(word):
    result = ""
    for letter in word:
        if letter.lower() in "aeiou":
            if letter.isupper():
                result = result + "G"
            else:
                result = result + "g"
        else:
            result = result + letter
    return result

print(translate_grif(input("enter a word: ")))

------------------------------------------------------

try:
    answer = 10 / 0
    number = int(input("put in a number: "))
    print(number)

except ZeroDivisionError as err:
    print(err)

except ValueError as err1:
    print(err1)

--------------------------------------------------------

employee_file = open("readfile.txt", "r+")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()

--------------------------------------------------------

import random

yes = "yes"

while yes == "yes":

    yes = input("Do you want to roll some new dice? yes or no?: ")

    dice_size = int(input("How many sides should the dice have?: "))

    dice_size = dice_size + 1

    roll_again = "yes"

    while roll_again == "yes":
        val1 = random.randint(1, dice_size)
        val2 = random.randint(1, dice_size)

        print("Dice 1: " + str(val1) + "\nDice 2: " + str(val2))

        roll_again = input("Roll same dice again?: ")

--------------------------------------------------------
class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False


from Student import Student

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pim", "Barf", 3.5, False)

print(student1.name)


--------------------------------------------------------

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

questions_prompts = [
    "what color?\n(a) red \n(b) green\n",
    "what colorss?\n(a) red \n(b) green\n",
    "what colorsss?\n(a) red \n(b) green\n"
]

questions = [
    Question(questions_prompts[0], "a"),
    Question(questions_prompts[1], "b"),
    Question(questions_prompts[2], "a")
]

run_test(questions)

--------------------------------------------------------



--------------------------------------------------------



--------------------------------------------------------