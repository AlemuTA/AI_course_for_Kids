# 🧪 Module 2 — How Machines Learn

> **📋 Parent note:** This is the first "wow" module. Your child will train a real AI model in the browser in about 5 minutes using **Google's Teachable Machine** — free, no install, no account needed. It works on any laptop/desktop with a webcam. This is the moment AI stops feeling abstract.

## Lesson 2.1 — Learning From Examples

### 🧠 The Big Idea
Machine Learning has two phases:
1. **Training** — you feed the AI lots of labeled examples ("this is a cat 🐱", "this is a dog 🐶"). The AI looks for patterns. This is like *studying*.
2. **Predicting** — you show it something *new* and it makes its best guess. This is like *taking the test*.

The collection of examples is called the **training data**. The pattern-finder it produces is called a **model**. You'll hear those two words constantly.

### 🎮 Do It: Be the Algorithm (no computer)
Have a parent secretly pick a rule (like "words with double letters"). They say words and tell you "yes" or "no" for each:
- "balloon" → yes, "cat" → no, "letter" → yes, "dog" → no...

After a few, *you* try to guess the next answer before they say it. You're doing exactly what an ML model does: spotting the hidden pattern from labeled examples!

### 💬 Think About It
- How many examples did you need before you "got it"?
- What if the parent gave you a few *wrong* labels by mistake? Would you still learn the right rule?

---

## Lesson 2.2 — Train Your First Real AI 🎉

### 🧠 The Big Idea
Time to train an actual image-recognition model. We'll use **Teachable Machine** at:
> 🔗 **teachablemachine.withgoogle.com** → click "Get Started" → "Image Project" → "Standard"

### 🎮 Do It: The "Rock, Paper, Scissors" Classifier
1. Make **3 classes** and name them: `Rock`, `Paper`, `Scissors`.
2. For each class, hold your hand in that shape and click "Hold to Record" to capture ~40–50 webcam images. Move your hand around a bit so it sees different angles.
3. Click **Train Model** and wait a few seconds.
4. Now show your hand live — watch the bars predict which gesture you're making! 🪨📄✂️

**Experiments to try** (this is the real learning):
- Add a 4th class, `Nothing` (empty hand), and retrain. Does it get less confused?
- Train with only 5 images per class instead of 40. Does it get worse? *(It should — this teaches you that more data usually helps.)*
- Train it in bright light, then test in a dark room. What happens? *(This previews "data quality" in Module 3.)*

### 💬 Think About It
- The AI never "knows" what rock or paper *means.* It only matches patterns of pixels. Does that surprise you?
- What would happen if you trained it on your hand but your friend tested it with theirs?

---

## Lesson 2.3 — The Three Flavors of Machine Learning

### 🧠 The Big Idea
ML comes in three main styles. Here's each one with a real-life analogy:

| Flavor | What it means | Real-life analogy |
|--------|---------------|-------------------|
| **Supervised** | Learn from examples *with answers/labels* | Studying flashcards with answers on the back |
| **Unsupervised** | Find hidden groups in data *with no labels* | Sorting a messy Lego pile into groups nobody named |
| **Reinforcement** | Learn by trial, error, and rewards | Training a dog with treats / getting better at a video game |

Your Rock-Paper-Scissors model was **supervised** — you gave it the labels.
A music app grouping "similar listeners" is **unsupervised.**
An AI that learns to play chess by playing millions of games is **reinforcement.**

### 🎮 Do It: Sort Your Stuff (unsupervised, unplugged)
Dump out a drawer (Legos, art supplies, snacks). Without deciding categories first, sort everything into groups that "feel" similar. Then name the groups *after.* Congratulations — you just did unsupervised learning, exactly like an AI clustering algorithm.

### 💬 Think About It
- Could a video game character get *too good* using reinforcement learning and stop being fun to play against?
- For teaching an AI to recognize emotions in faces, which flavor would you use?

### 🏆 Module 2 Check
You trained a real model, and you know the difference between training and predicting, and the three flavors of ML. **Big level up!**

---

⏪ [Previous: Module 1](01-what-is-ai.md) · [Home](README.md) · [Next: Module 3 — Data ⏩](03-data-the-fuel-of-ai.md)
