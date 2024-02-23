import random
dice_roll_1 = random.randint(1,6)
dice_roll_2 = random.randint(1,6)

end_roll = dice_roll_1 + dice_roll_2

while True:
    try:
        user_input = int(input("Guess the two dice roll - and win a prize! Enter a number between 1 and 12: "))
        if user_input > 12:
            print("You can't go higher than 12 on a two sided dice.")
        elif user_input < 1:
            print("You can't have negative numbers.")
        else:
            if user_input == end_roll:
                print("We have a winner! Please collect your prize.")
                break
            else:
                print("Better luck next time!")
                break

    except ValueError:
        print("That's not a number.")