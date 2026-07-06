# ⛽ Module 3 — Data: The Fuel of AI

> **📋 Parent note:** This is arguably the most important module for raising a *thoughtful* AI user, not just a skilled one. The theme of **bias** is introduced gently and concretely. These conversations matter as much as any coding skill.

## Lesson 3.1 — What Even Is Data?

### 🧠 The Big Idea
**Data** is just information stored in a form a computer can use. It comes in many types:
- **Images** (your Rock-Paper-Scissors photos)
- **Text** (every comment, message, and book)
- **Numbers** (temperatures, scores, prices)
- **Sound** (voice recordings, music)
- **Categories** (yes/no, cat/dog, red/blue/green)

AI is *only as good as the data it learns from.* There's a famous saying in computing:

> **"Garbage in, garbage out."** Feed an AI messy or wrong examples, and it learns messy, wrong patterns.

### 🎮 Do It: Build a Mini Dataset
Pick something you love (Pokémon, sneakers, dog breeds). Make a small spreadsheet or table of 10 examples, each with 3–4 **features** (columns). For dogs that might be: *size, fur length, ear shape, energy level.* You just created structured data — the same kind real AIs train on.

### 💬 Think About It
- What's a "feature" that would help an AI tell a husky from a chihuahua? What feature would be useless (like "the dog's name")?

---

## Lesson 3.2 — When Data Goes Wrong: Bias

### 🧠 The Big Idea
Here's a true and important fact: **AI learns whatever is in its data — including unfairness.**

Imagine training a "recognize a shoe" AI, but every photo you used was of sneakers. Show it a high heel or a sandal and it'll be confused or wrong — not because shoes are hard, but because your data was **biased** (one-sided).

This happens in real, serious ways:
- A face-recognition AI trained mostly on one group of people works worse on everyone else.
- A hiring AI trained on a company's past hires can copy the company's past unfairness.

The AI isn't "being mean" — it's faithfully copying patterns in flawed data. That's why people who build AI have to think hard about *where their data comes from.*

### 🎮 Do It: The Biased Classifier Experiment
Go back to Teachable Machine. Train a "happy vs. sad face" classifier, but **only record yourself** making the faces. Then ask a family member to test it with *their* face. Does it work as well? You just created — and then witnessed — data bias firsthand.

### 💬 Think About It
- If an AI's data only includes one type of person, place, or example, who might it fail for?
- How could the people building an AI catch bias *before* it causes harm?

---

## Lesson 3.3 — More Data, Better Data

### 🧠 The Big Idea
Two things make AI better:
1. **More examples** (so it sees more variety)
2. **Better, more representative examples** (so it sees the *right* variety)

But there's a catch — quantity can't fix bias. A million photos of only sneakers still won't teach an AI about sandals. You need *variety*, not just *volume.*

### 🎮 Do It: Fix Your Biased AI
Retrain your happy/sad classifier, but this time include several people (or photos of varied faces from a parent's approved source). Test again. Better? That improvement *is* the lesson.

### 🏆 Module 3 Check
You understand data, features, bias, and why representative data matters. You're now thinking like a responsible AI builder. 🌟

---

⏪ [Previous: Module 2](02-how-machines-learn.md) · [Home](README.md) · [Next: Module 4 — Neural Networks ⏩](04-neural-networks.md)
