# 💻 Module 5 — Coding AI

> **📋 Parent note:** This module has **two on-ramps**. If your child is new to coding, start with the block-based path (Scratch + Machine Learning for Kids). If they're comfortable, move to the Python path. Both are free. Python is the real language of professional AI, so reaching it is a milestone — but there's no rush, and blocks teach the same logic.

## Lesson 5.1 — On-Ramp A: AI With Blocks (Scratch)

### 🧠 The Big Idea
**Machine Learning for Kids** (by educator Dale Lane) lets you train a model *and then use it inside a Scratch program* — drag-and-drop coding, no typing required. It's the friendliest bridge from "training a model" to "building an app."

> 🔗 **machinelearningforkids.co.uk** (free; a parent can set up the free account access)

### 🎮 Do It: Build a "Compliment or Insult" Detector Game
1. In ML for Kids, make a **text** project. Create two labels: `kind` and `unkind`.
2. Add example phrases to each ("you're awesome" → kind, etc.). ~10 each to start.
3. Train the model.
4. Switch to Scratch and use the new "recognize text" blocks to make a sprite **smile** for kind messages and **frown** for unkind ones.

You just built an app powered by an AI model *you* trained. That's the real workflow professionals use, just simpler.

### 💬 Think About It
- Add a tricky phrase like "you're *so* bad at this... at being normal." How does your model handle sarcasm? (Spoiler: text AI struggles with sarcasm — even big ones!)

---

## Lesson 5.2 — On-Ramp B: Meet Python 🐍

### 🧠 The Big Idea
**Python** is the most popular language for real AI. It reads almost like English. You don't need to install anything — use a free online editor (a parent can help pick one, like Google Colab or replit.com).

Here are the four building blocks of nearly all code:

```python
# 1. Variables — boxes that hold information
name = "Alex"
age = 12

# 2. Lists — a collection of things
pets = ["dog", "cat", "hamster"]

# 3. Loops — do something repeatedly
for pet in pets:
    print("I have a " + pet)

# 4. If-statements — make decisions
if age >= 13:
    print("Teenager!")
else:
    print("Not quite a teen yet!")
```

### 🎮 Do It: Your First Programs
Type these out yourself (don't copy-paste — muscle memory matters):
1. Make a list of your 5 favorite foods and print each one with a loop.
2. Write an if-statement that prints "Hot!" if a temperature variable is over 30, else "Not hot."
3. **Mini challenge:** make a program that counts from 1 to 10 and prints "Buzz" instead of any number divisible by 3.

### 💬 Think About It
- Notice how the *if-statement* is just a rule, while the AI models you trained learned rules themselves. Real AI programs mix both: human-written code *around* a learned model.

---

## Lesson 5.3 — Building a Real App

### 🧠 The Big Idea
Now combine your skills. **MIT App Inventor** (free, block-based) lets you build actual phone apps — including ones that use AI like image recognition.

> 🔗 **appinventor.mit.edu**

### 🎮 Do It: The Talking Camera
Follow App Inventor's "image classification" tutorial to build an app that looks through the camera and *says out loud* what it sees. You'll connect: a camera input → an AI model → a text-to-speech output. That's a complete AI pipeline, built by you.

### 🏆 Module 5 Check
You've coded with blocks *and* written real Python, and built an AI-powered app. You're not just *using* AI anymore — you're *building* it. 🚀

---

⏪ [Previous: Module 4](04-neural-networks.md) · [Home](README.md) · [Next: Module 6 — Chatbots & Generative AI ⏩](06-chatbots-and-generative-ai.md)
