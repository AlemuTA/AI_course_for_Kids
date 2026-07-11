# Day 3: elif - more than two choices

score = int(input("Enter your game score (0 to 100): "))

if score >= 90:
    print("Rank: S - LEGENDARY!")
elif score >= 70:
    print("Rank: A - Great job!")
elif score >= 50:
    print("Rank: B - Not bad!")
else:
    print("Rank: C - Keep practicing!")

# YOUR TURN:
# 1. Add a new top rank: if score is exactly 100, print "Rank: SS - PERFECT!"
#    (Hint: put it FIRST, and use ==)
# 2. Make a level picker: ask the player to type easy, normal, or hard,
#    and print a different message for each one.
