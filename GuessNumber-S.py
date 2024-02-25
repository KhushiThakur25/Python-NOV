import random

cpu = random.randint(1,100)
count = 5

while True:
    user = int(input("Guess the number between 1 - 100"))
    if cpu == user:
        print("You win..")
        break
    elif cpu < user:
        print("You have guessed larger number..")
    elif cpu > user:
        print("You have guessed smaller number..")
    else:
        print("Invalid input..")

    count -= 1
    print("Chances left",count)

    if count == 0:
        print("You loose the match..")
        break
