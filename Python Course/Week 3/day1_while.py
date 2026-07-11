# Day 1: while loops - repeat until something happens

health = 5

while health > 0:
    print("Still alive! Health:", health)
    health = health - 1

print("GAME OVER")

# A countdown, like a game starting:
countdown = 3
while countdown > 0:
    print(countdown, "...")
    countdown = countdown - 1
print("GO!")

# YOUR TURN:
# 1. Make a rocket launch countdown from 10 that ends with "BLAST OFF!"
# 2. Make a coins counter that starts at 0 and ADDS 10 each loop
#    while coins < 50, printing coins each time.
