import random
random_number = random.randint(1, 10)

#counting guesses
guess_count = 3

while True:
    user_input = input("Guess the number")
    user_input = int(user_input)

    if user_input > random_number:
        guess_count -= 1
        print("That guess is too high")

    elif user_input < random_number:
        guess_count -= 1
        print("That guess is too low")

    if guess_count == 2:
        print("You have two more guesses")
    elif guess_count == 1:
        print("You have one more guess")
    elif guess_count == 0:
        print("You are lose!")
        break

    else:
        print("You are winner!")
        break
