# FINAL PROJECT: Rock, Paper, Scissors - BEST OF 5!
# Uses everything you learned: variables, input, if/elif, while, random, f-strings.

import random

print("=== ROCK, PAPER, SCISSORS: BEST OF 5 ===")

choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

while player_score < 3 and computer_score < 3:
    player = input("rock, paper, or scissors? ")
    computer = random.choice(choices)
    print(f"You: {player} | Computer: {computer}")

    if player == computer:
        print("Tie! Go again.")
    elif player == "rock" and computer == "scissors":
        print("You win this round!")
        player_score = player_score + 1
    elif player == "paper" and computer == "rock":
        print("You win this round!")
        player_score = player_score + 1
    elif player == "scissors" and computer == "paper":
        print("You win this round!")
        player_score = player_score + 1
    else:
        print("Computer wins this round!")
        computer_score = computer_score + 1

    print(f"SCORE - You: {player_score} | Computer: {computer_score}")
    print()

if player_score == 3:
    print("CHAMPION! You beat the computer!")
else:
    print("The computer wins this time. Rematch?")

# YOUR TURN - level it up:
# 1. If the player types something that isn't rock/paper/scissors,
#    print "Invalid choice!" and don't count the round.
#    (Hint: add this check FIRST: if player not in choices:)
# 2. Ask the player's name at the start and use it in the messages.
# 3. Bonus: at the end, ask "Play again? (yes/no)" - can you make
#    the WHOLE game repeat? (Hint: another while loop around everything!)
