# Day 3: Warm-up - ONE round of Rock, Paper, Scissors

import random

choices = ["rock", "paper", "scissors"]

player = input("rock, paper, or scissors? ")
computer = random.choice(choices)

print(f"You chose {player}. Computer chose {computer}.")

if player == computer:
    print("It's a tie!")
elif player == "rock" and computer == "scissors":
    print("You win! Rock crushes scissors.")
elif player == "paper" and computer == "rock":
    print("You win! Paper covers rock.")
elif player == "scissors" and computer == "paper":
    print("You win! Scissors cut paper.")
else:
    print("Computer wins!")

# YOUR TURN:
# 1. Run this a few times to see different results.
# 2. Read the if/elif chain out loud and make sure each line makes sense.
# 3. Tomorrow you'll turn this into a full best-of-5 game!
