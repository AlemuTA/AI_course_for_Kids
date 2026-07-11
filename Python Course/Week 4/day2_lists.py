# Day 2: Lists - an inventory for your data

import random

inventory = ["sword", "shield", "potion"]

print(inventory[0])   # first item - counting starts at 0!
print(inventory[2])   # third item

inventory.append("map")
print(f"You now carry {len(inventory)} items:")

for item in inventory:
    print(f" - {item}")

# Random pick:
lucky = random.choice(inventory)
print(f"A goblin steals your {lucky}!")

# YOUR TURN:
# 1. Make a list of your 4 favorite games.
# 2. Print each one with a for loop.
# 3. Use random.choice to let Python pick which one you play tonight!
# 4. Append a game you want to try someday, then print len() of the list.
