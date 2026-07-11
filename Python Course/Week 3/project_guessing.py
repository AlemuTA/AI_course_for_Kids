# Weekend Project: NUMBER GUESSING GAME
# The computer picks a secret number from 1 to 20. Can you find it?

import random

print("=== GUESS MY NUMBER ===")
print("I'm thinking of a number from 1 to 20...")

secret = random.randint(1, 20)
guess = 0
tries = 0

while guess != secret:
    guess = int(input("Your guess: "))
    tries = tries + 1
    if guess < secret:
        print("Higher!")
    elif guess > secret:
        print("Lower!")

print("YOU GOT IT! The number was", secret)
print("It took you", tries, "tries.")

# YOUR TURN:
# 1. Make it harder: change the range to 1 to 100.
# 2. Rate the player at the end:
#    5 tries or fewer -> "Mind reader!", 10 or fewer -> "Nice!", more -> "Slow and steady!"
# 3. Bonus: print a warning if the guess is below 1 or above the max.
