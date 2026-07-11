# Day 2: random - dice rolls and surprises

import random

dice = random.randint(1, 6)
print("You rolled:", dice)

# A loot box!
loot = random.randint(1, 3)
if loot == 1:
    print("You found a WOODEN SWORD.")
elif loot == 2:
    print("You found a GOLDEN SHIELD!")
else:
    print("You found a LEGENDARY DRAGON EGG!!!")

# YOUR TURN:
# 1. Roll TWO dice and print both, then print their total.
# 2. Make a coin flip: random.randint(1, 2) - print "Heads" for 1, "Tails" for 2.
# 3. Add more prizes to the loot box (use randint(1, 5) and more elifs).
