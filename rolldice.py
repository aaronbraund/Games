import random
d100 = random.randint(1,100)

import time

print("The dice will seal your fate...")
time.sleep(3)
if d100:
    print(f"You rolled {d100}")
time.sleep(3)

while True:
    if 1 <= d100 <= 10:
        print("You fall into the bog")
        break
    else:
        print("Magic needs time to cook")
        break


