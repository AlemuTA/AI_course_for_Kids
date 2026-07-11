# Day 2: if - the computer makes choices

health = int(input("Enter your health (0 to 100): "))

if health <= 0:
    print("GAME OVER")
else:
    print("Keep playing!")

# A secret password door:
password = input("Say the magic word to enter the castle: ")

if password == "dragon":
    print("The gate opens! Welcome inside.")
else:
    print("The gate stays shut. Try again!")

# YOUR TURN:
# 1. Change the magic word to something else.
# 2. Ask the player how many coins they have.
#    If they have 100 or more, print "You can buy the golden sword!"
#    Otherwise print "Not enough coins."
