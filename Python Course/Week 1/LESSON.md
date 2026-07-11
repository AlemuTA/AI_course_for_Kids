# Week 1: Talking to the Computer 🗣️

## Day 1: Your first program — `print()`

In games, the computer shows you messages: "Level Up!", "Game Over". In Python, YOU make the computer talk with `print()`:

```python
print("Hello, I am Abeselom's computer!")
print("Game Over")
```

The text inside the quotes is called a **string** — it's just text.

**Try it:** Open `day1_print.py`, run it, then change the messages to anything you want.

**Mini-challenge:** Make the computer print your gamertag on one line and your favorite game on the next.

## Day 2: Variables — the computer's backpack 🎒

In games, your character has stats: health = 100, coins = 50. Those are **variables** — boxes with names that store things.

```python
health = 100
player_name = "Abeselom"
print(player_name)
print(health)
```

You can change what's in the box:

```python
health = 100
health = health - 30   # you took damage!
print(health)          # shows 70
```

**Rules for variable names:** no spaces (use `_`), and they can't start with a number.

**Try it:** Open `day2_variables.py`.

## Day 3: `input()` — let the player talk back 🎤

Games ask you questions: "Enter your name". `input()` does that:

```python
name = input("What is your name? ")
print("Welcome, " + name + "!")
```

Whatever the player types gets stored in the variable `name`. The `+` glues strings together.

**Try it:** Open `day3_input.py`.

## Weekend Project: Mad Libs Story Game 📖

A Mad Libs game asks for random words, then puts them into a funny story. Open `project_madlibs.py` — part of it is written, and your job is to finish it!

## Week 1 words to remember

- **print()** — show a message
- **string** — text in quotes
- **variable** — a named box that stores a value
- **input()** — ask the player to type something
