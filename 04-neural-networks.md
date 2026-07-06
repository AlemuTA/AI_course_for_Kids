# 🧠 Module 4 — How AI "Thinks": Neural Networks

> **📋 Parent note:** We now open the "black box." The math is kept entirely out — your child will *play* with a real neural network in the browser (**TensorFlow Playground**) and build intuition visually. The goal is a feel for *weights, layers, and learning from mistakes,* not equations.

## Lesson 4.1 — Brains Made of Math

### 🧠 The Big Idea
Many modern AIs use **neural networks** — software loosely inspired by how brain cells (neurons) connect.

Here's the whole idea in plain language. A single artificial **neuron**:
1. Takes in some numbers (inputs),
2. Multiplies each by a **weight** (think of weights as *volume knobs* — turn one up and that input matters more),
3. Adds them up,
4. and "fires" a result to the next neuron.

Stack lots of neurons into **layers**, connect them, and you get a network that can recognize wildly complex patterns — faces, speech, handwriting.

### 🎮 Do It: The Human Neural Network (unplugged, needs a few people)
Line up 3 "neurons" (people). Person 1 gets a secret number and a rule ("if my number is over 5, pass a thumbs-up; else thumbs-down"). Person 2 combines what they receive with their own rule, and so on. The final person announces the output. Now tweak one person's rule ("weight") and watch the whole answer change. *That's* a neural network adjusting its weights.

### 💬 Think About It
- A real network can have *millions* of these neurons. Why might that let it learn harder things?

---

## Lesson 4.2 — Learning From Mistakes

### 🧠 The Big Idea
How does a network actually *learn*? Through a feedback loop, a bit like learning to shoot a basketball:

1. **Guess** — the network makes a prediction.
2. **Check** — compare it to the right answer. How far off was it? (This gap is called the **error** or **loss.**)
3. **Adjust** — nudge the weights a little to reduce the error next time. Aim was too far left? Adjust right.
4. **Repeat** — thousands or millions of times until guesses get good.

Each full round through the examples is called an **epoch.** Watching the error shrink over epochs is one of the most satisfying things in AI.

### 🎮 Do It: Play With a Real Neural Network
Go to:
> 🔗 **playground.tensorflow.org**

You'll see colored dots the network is trying to separate. Press the ▶️ **play button** and watch it learn in real time — the background colors shift as it figures out the pattern.

**Experiments:**
- Watch the "Test loss" number. It should *drop* as training runs. That's learning, visualized.
- Add more neurons or layers (the + buttons). Does it solve the hard "spiral" dataset better?
- Pick the spiral dataset (bottom-left). Try to get it to learn the spiral. *Hard, right?* More layers help — this is literally what "deep learning" means: **more layers = deeper network = more complex patterns.**

### 💬 Think About It
- When you added too many neurons, did it sometimes look like it "memorized" the dots instead of learning the real shape? That's a real problem called **overfitting** — like cramming exact answers for a test instead of understanding the topic. It does great on the practice questions and fails the real exam.

### 🏆 Module 4 Check
You can explain neurons, weights, layers, and learning-from-error in your own words — and you've watched a real network learn. You've seen inside the "brain." 🧠⚡

---

⏪ [Previous: Module 3](03-data-the-fuel-of-ai.md) · [Home](README.md) · [Next: Module 5 — Coding AI ⏩](05-coding-ai.md)
