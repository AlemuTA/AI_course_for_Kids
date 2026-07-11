# Week 3: Repeating Things 🔁

## Day 1: `while` loops — repeat until something happens

Games repeat things constantly: enemies keep attacking WHILE you're alive. In Python:

```python
health = 5

while health > 0:
    print("Still alive! Health:", health)
    health = health - 1

print("GAME OVER")
```

The loop keeps running the indented lines **while** the condition is true. When `health` hits 0, the loop stops.

⚠️ **Warning:** if the condition never becomes false, the loop runs FOREVER (an "infinite loop"). If that happens, press the Stop button in Thonny.

Also new: `print("Health:", health)` — a comma lets you print text and a number together.

**Try it:** Open `day1_while.py`.

## Day 2: `random` — dice rolls and surprises 🎲

Games need surprise: loot drops, critical hits, dice rolls. Python has a `random` toolbox:

```python
import random

dice = random.randint(1, 6)   # random number from 1 to 6
print("You rolled:", dice)
```

`import random` at the top unlocks the toolbox. `random.randint(1, 6)` picks a random whole number between 1 and 6.

**Try it:** Open `day2_random.py`.

## Day 3: `for` loops — repeat an exact number of times

When you know HOW MANY times to repeat, use `for`:

```python
for i in range(5):
    print("Attack number", i)
```

This prints 5 lines. Note: `range(5)` counts 0, 1, 2, 3, 4 — computers start counting at 0!

**Try it:** Open `day3_for.py`.

## Weekend Project: Number Guessing Game 🎯

The computer picks a secret number, and the player keeps guessing until they find it — with "higher/lower" hints. Open `project_guessing.py`.

## Week 3 words to remember

- **while loop** — repeat while a condition is true
- **for loop** — repeat an exact number of times
- **import random** — unlock the random toolbox
- **random.randint(a, b)** — random number from a to b
- **infinite loop** — a loop that never stops (press Stop!)
