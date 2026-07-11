# Weekend Project: QUIZ GAME with score!

print("=== THE ULTIMATE QUIZ ===")
score = 0

answer = input("Question 1: What planet do we live on? ")
if answer == "Earth" or answer == "earth":
    print("Correct! +10 points")
    score = score + 10
else:
    print("Nope, it was Earth!")

answer = input("Question 2: How many legs does a spider have? ")
if answer == "8":
    print("Correct! +10 points")
    score = score + 10
else:
    print("Nope, it was 8!")

print()
print("Your final score:")
print(score)

if score == 20:
    print("PERFECT SCORE! You are a quiz champion!")
elif score == 10:
    print("Good try! Play again to beat your score.")
else:
    print("Better luck next time!")

# YOUR TURN:
# 1. Add 3 more questions about YOUR favorite games (worth 10 points each).
# 2. Update the final rank messages so a perfect score is now 50.
