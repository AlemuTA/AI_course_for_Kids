# Week 4: Putting It All Together 🏆

## Day 1: f-strings — a nicer way to print 💬

You've been gluing strings with `+`. There's a cooler way — put an `f` before the quotes and drop variables inside `{ }`:

```python
name = "Abeselom"
level = 7
print(f"Player {name} reached level {level}!")
```

It works with numbers too — no `int()` headaches when printing.

**Try it:** Open `day1_fstrings.py`.

## Day 2: Lists — an inventory for your data 🎒

A **list** stores many things in one variable — like a game inventory:

```python
inventory = ["sword", "shield", "potion"]
print(inventory[0])        # sword  (counting starts at 0!)
inventory.append("map")    # add an item
print(len(inventory))      # 4 items now
```

You can loop through a list:

```python
for item in inventory:
    print(f"You are carrying: {item}")
```

And `random.choice(inventory)` picks a random item!

**Try it:** Open `day2_lists.py`.

## Day 3: Plan your final game 📝

Rock, Paper, Scissors! Before coding, good programmers plan. The game needs to:

1. Ask the player: rock, paper, or scissors?
2. Computer picks randomly (hint: `random.choice`)
3. Compare — who wins? (rock beats scissors, scissors beats paper, paper beats rock)
4. Keep score and play best of 5 (hint: a `while` loop)

Look at `day3_practice.py` for a warm-up that builds one round.

## Weekend Project: Rock, Paper, Scissors — FULL GAME 🎮

Open `project_rps.py`. One round is built for you. Your mission: make it best-of-5 with score tracking. This uses EVERYTHING from the course: variables, input, if/elif/else, while loops, random, and f-strings.

## You did it! What's next? 🚀

After this course, Abeselom can:

- Rebuild the guessing game or quiz from memory (great practice!)
- Learn **functions** and **dictionaries** (the next big topics)
- Try [Invent with Python](https://inventwithpython.com/) — free books about making games
- Eventually try **pygame** to make games with real graphics

## Week 4 words to remember

- **f-string** — `f"text {variable}"` for easy printing
- **list** — one variable holding many items
- **append()** — add to a list
- **len()** — how many items a list has
- **random.choice()** — pick a random item from a list
