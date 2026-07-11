# Week 2: Making Decisions 🤔

## Day 1: Numbers and math ➕

Python is a super calculator:

```python
print(5 + 3)    # 8
print(10 - 4)   # 6
print(6 * 7)    # 42 (* means multiply)
print(20 / 4)   # 5.0 (/ means divide)
```

One catch: `input()` always gives you **text**, even if the player types a number. To turn it into a real number, wrap it with `int()`:

```python
age = int(input("How old are you? "))
print(age + 10)   # now math works!
```

**Try it:** Open `day1_math.py`.

## Day 2: `if` — the computer makes choices 🚦

Games are full of decisions: IF health is 0, THEN game over. Python does exactly that:

```python
health = 0

if health <= 0:
    print("GAME OVER")
else:
    print("Keep playing!")
```

Two important things:

1. The line after `if` ends with a colon `:`
2. The next line is pushed in with 4 spaces (called **indentation**) — that's how Python knows it belongs to the `if`.

Comparison signs: `==` equals (two = signs!), `!=` not equal, `>` greater, `<` less, `>=` at least, `<=` at most.

**Try it:** Open `day2_if.py`.

## Day 3: `elif` — more than two choices 🎯

What if there are 3 or more options? Use `elif` (short for "else if"):

```python
score = 85

if score >= 90:
    print("Rank: S — LEGENDARY!")
elif score >= 70:
    print("Rank: A — Great job!")
elif score >= 50:
    print("Rank: B — Not bad!")
else:
    print("Rank: C — Keep practicing!")
```

**Try it:** Open `day3_elif.py`.

## Weekend Project: Quiz Game 🏆

Build a quiz that keeps score! Open `project_quiz.py` and finish it.

## Week 2 words to remember

- **int()** — turn text into a whole number
- **if / elif / else** — let the computer choose what to do
- **==** — "is equal to" (don't confuse with `=` which stores a value!)
- **indentation** — the 4 spaces that show what belongs to the `if`
