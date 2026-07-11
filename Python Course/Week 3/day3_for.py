# Day 3: for loops - repeat an exact number of times

for i in range(5):
    print("Attack number", i)

print()

# Combine a for loop with random for 3 dice rolls:
import random

for i in range(3):
    dice = random.randint(1, 6)
    print("Roll", i, "was:", dice)

# YOUR TURN:
# 1. Print "Level up!" 10 times using a for loop.
# 2. Open 5 loot boxes in a loop: each time, pick random.randint(1, 100)
#    coins and print how many coins you got.
