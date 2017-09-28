import random

def magic_number():
    while True:
        random_number = random.randint(0,10)
        user_num = input("Choose a number between 1 and 10: ")
        if int(user_num) == random_number:
            print("You've won!")
            return False

        else:
            print("you've lost!")
            print("The answer was {}.".format(random_number))

magic_number()