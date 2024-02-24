import time

#function that adds a time delay parameter to delay print statements
def p_delay(message,delay=1):
    print(message)
    time.sleep(delay)

#function that prints full stops one by one for suspense
def pause_stop(num_stops, delay=1):
    for stops in range(num_stops):
        print('.', end='', flush=True)
        time.sleep(delay)

#setting the scene
p_delay("You are walking through a forest.",3)
p_delay("You're not sure how you got here.",3)
p_delay("It is dark, moonlight breaks through the trees.",3)
p_delay("It offers little reprieve against the darkness.",3)
p_delay("You remember.",3)
p_delay("Your sister is lost.",3)
p_delay("Somewhere in this forest.",3)
p_delay("Save her. She's all you have left.",3)
p_delay("You have a knife. Use it.",3)

#goblin encounter
p_delay("You continue to walk.",3)
p_delay("A dark figure looms from a tree.",3)
p_delay("A goblin... what do you do?",3)

#player choice
while True:
    try:
        player_choice = input("Flee, scare or fight? Choose. ").lower()
        if player_choice == "scare":
            goblin_enc = 1
            p_delay("You let out a sudden howl, scaring the goblin away.",3)
            break
        elif player_choice == "flee":
            goblin_enc = 2
            p_delay("You run from the monster. You have to save Ayla.",3)
            break
        elif player_choice == "fight":
            goblin_enc = 3
            p_delay("You steady your nerves and draw the dagger.",3)
            break
        else:
            print("The action had no effect. You must save your sister.")
    except ValueError:
        print("You must choose to flee, scare or fight")

#ending A and ending B
if goblin_enc == 1:
    p_delay("The forest is silent once again.",3)
    p_delay("You continue to walk.",3)
    p_delay("You smell something faint, metallic, sickening.",3)
    p_delay("From one of the bushes, a small, pale leg, specked with crimson.",3)
    p_delay("Long, golden hair - matted, bloodied.",3)
    p_delay("Your sister... Ayla.",3)
    p_delay("Her body is cold.",3)
    p_delay("She is dead.",3)
    p_delay("She was all you had left",3)

    while True:
            try:
                player_choice_2 = input("Use your dagger? Yes or No: ").lower()
                if player_choice_2 == "yes":
                    p_delay("You bury the blade deep into your neck.",3)
                    p_delay("You feel the slick of hot blood.",3)
                    p_delay("Your legs buckle - and you fall.",3)
                    p_delay("Everything goes dark.",3)
                    p_delay("You failed her.",3)
                    print("Ending A")
                    break
                elif player_choice_2 == "no":
                    p_delay("No...Ayla wouldn't want that.",3)
                    p_delay("You drop the dagger.",3)
                    p_delay("You fall to your knees, reaching over at her lifeless body.",3)
                    p_delay("You embrace your sister one last time.",3)
                    p_delay("You failed her.",3)
                    print("Ending B")
                    break
            except ValueError:
                print("Ayla is gone")

#ending C and ending D
if goblin_enc == 2:
    p_delay("You run.",3)
    p_delay("And run.",3)
    p_delay("And run.",3)
    p_delay("You finally stop, your chest burning.",3)
    p_delay("You have to find Ayla.",3)
    p_delay("Your eyes dart around the forest.",3)
    p_delay("A single, bulging eye, fixed on you.",3)
    p_delay("You freeze.",3)
    p_delay("A disgusting, impossible contortion of flesh, edges closer.",3)
    p_delay("Something splits, a bloody crack in the disfigured flesh.",3)
    p_delay("Blue eyes, golden hair, snow-like skin...",3)
    p_delay("It's a face you know, all too well.",3)
    p_delay("Your sister's face.",3)
    p_delay("Ayla speaks, it is her voice",3)
    p_delay("Brother.",3)
    p_delay("Join us.",3)
    p_delay("It is warm, we are loved here.",3)
    p_delay("Take my hand, and we will be together.",3)
    p_delay("From the oozing flesh, a limp, severed hand slowly reaches towards yours.",3)

    while True:
        try:
            player_choice_3 = input("Will you join her? Yes or no: ").lower()
            if player_choice_3 == "yes":
                p_delay("You take the hand.",3)
                p_delay("Slowly, you are drawn into a pitch back abyss.",3)
                p_delay("From the darkness, you hear the grinding teeth.",3)
                p_delay("Something sharp - and then darkness",3)
                p_delay("You failed her.",3)
                print("Ending C")
                break
            elif player_choice_3 == "no":
                p_delay("It's a trap.",3)
                p_delay("This isn't your sister.",3)
                p_delay("You step back from the monster.",3)
                p_delay("Something heavy, immovable - constricting your throat",3)
                p_delay("It draws you back.",3)
                p_delay("A gaping maw of teeth awaits.",3)
                p_delay("And - darkness.",3)
                p_delay("You failed her.",3)
                print("Ending D")
                break
        except ValueError:
            print("Your sister...")

if goblin_enc == 3:
    p_delay("The goblin moves slowly towards you.",3)
    p_delay("Moonlight illuminates its scarred, dishevelled body.",3)
    p_delay("A tapestry of battles - won and lost.",3)
    p_delay("In its hand, a jagged club, worn and battered.", 3)
    p_delay("A hunter who wants to spill your blood.",3)
    p_delay("You grip the dagger, with all your might.",3)
    p_delay("You must kill this creature.",3)
    p_delay("You must find Ayla.")

    while True:
        try:
            goblin_counter = 0
            player_choice_4 = input("Attack or dodge? ").lower()
            if player_choice_4 == "attack":
                goblin_enc_2 = 1
                p_delay("You lunge with your blade, aiming for the creature's heart.", 3)
                break
            elif player_choice_4 == "dodge":
                goblin_enc_2 = 2
                p_delay("You sense a blow coming and adjust your footing.", 3)
                break
        except ValueError:
            print("The goblin prepares to strike. You must attack.",3)
            goblin_counter =+ 1
            if goblin_counter == 3:
                goblin_enc_2 = 3
                break
#ending E
if goblin_enc_2 == 1:
    p_delay("The sudden attack - too swift for the creature.",3)
    p_delay("You bury the blade deep into the monster's heart.",3)
    p_delay("Your blood boils beneath your skin.",3)
    p_delay("The monster does nothing, its mouth agape, a small pained groaning sound.",3)
    p_delay("You stab again, your other hand keeping the monster in place.",3)
    p_delay("Shock. Blood loss. It falls to its knees.")
    p_delay("You stab again, and again, and again.",3)
    p_delay("You carve your hatred on the beast.",3)
    p_delay("Again. And again. And again.",3)
    p_delay("The creature is dead.",3)
    p_delay("You have to find Ayla.",3)
    p_delay("Tightness in your arms",3)
    p_delay("Throbbing muscles",3)
    p_delay("You gasp for breath.",3)
    pause_stop(3,2)
    p_delay("Finally, you look down at your sister's body.",3)
    p_delay("She is so still, so beautiful in death.")
    p_delay("She was all you had left.",3)
    p_delay("On this night, the dagger claims two souls.",3)
    p_delay("You failed her.",3)
    print("Ending E")

#ending F
if goblin_enc_2 == 2:
    p_delay("The goblin moves to kill.",3)
    p_delay("A vicious, downward strike.",3)
    p_delay("You avoid the blow, readying your stance to counter.",3)
    p_delay("Darkness.",2)
    pause_stop(5,2)

print("More coming soon!")
