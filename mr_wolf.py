import random
random_number = random.randint(1,12)
wake_up_wolf = 0

while True:
    try:
        user_input = input("What's the time, Mr Wolf?")
        user_input = int(user_input)

        if user_input > 12:
            print("Silence.")

        elif user_input != random_number:
            wake_up_wolf += 1
            if wake_up_wolf == 1:
                print("The wolf is still.")
            elif wake_up_wolf == 2:
                print("The wolf hungers.")
            elif wake_up_wolf == 3:
                print("It's DINNERTIME")
                quit()

        elif user_input == random_number:
            print("You escape.")
            quit()

    except ValueError:
        wake_up_wolf += 1
        if wake_up_wolf == 1:
            print("The wolf stirs.")
        elif wake_up_wolf == 2:
            print("The wolf hears you.")
        elif wake_up_wolf == 3:
            print("It's DINNERTIME")
            quit()
print("Test")