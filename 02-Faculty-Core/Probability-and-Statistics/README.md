# 🍋 Maya's Lemonade Stand — Statistics You Can Taste

A tiny, friendly Python project that teaches a whole college **Probability &
Statistics for Engineering** course (MATH2561) using ONE fun story a kid
actually cares about: *running a lemonade stand.*

Maya recorded 4 things in her notebook for 20 days — how hot it was, whether
it was a weekend, and how many cups she sold. That single, real-feeling
notebook is enough to practice **every one of the 5 course modules.** No scary
textbook data — just "what happened at the stand."

> **The whole idea:** don't teach a formula and then go looking for a problem.
> Start with a problem a kid *wants* to solve, and let the statistics fall out
> of it naturally.

---

## 🚀 How to run it (2 steps)

```bash
pip install -r requirements.txt      # one-time setup

python src/run_all.py                # runs Module 1 → 5 as one story
```

Or run any single module on its own:

```bash
cd src
python data.py                 # see Maya's notebook
python module1_describe.py     # Module 1
python module2_probability.py  # Module 2
python module3_distributions.py
python module4_estimation.py
python module5_regression.py
```

Two pictures get saved into `charts/` so kids can *see* the math.

---

## 🗺️ How the story maps to the course

| Course Module | Real question Maya asks | What the kid learns |
|---|---|---|
| **1. Descriptive Statistics** | "On a normal day, how much do I sell — and how bumpy is it?" | mean, median, range, standard deviation, coefficient of variation, bar charts |
| **2. Probability** | "What are the chances of a busy day? Does the weekend change it?" | probability, conditional probability, independence, **Bayes' theorem** |
| **3. Probability Distributions** | "How many buy the large cup? How many customers per hour? How hot will it be?" | **Binomial, Poisson, Geometric, Normal** distributions |
| **4. Estimation & Tests** | "How sure am I of my true average? Did my new SIGN really boost sales?" | standard error, **confidence interval**, **t-test / hypothesis testing** |
| **5. Correlation & Regression** | "Do hotter days sell more? How many cups for a 28°C day?" | correlation, **linear regression**, prediction, R² |

---

## 🍋 A peek at what it prints

**Module 1 — describing sales**
```
Average (mean) : 32.5 cups per day
Std deviation  : 13.2 cups  <- typical wobble around the average
Coeff of var   : 41%        <- some days are much busier than others
```

**Module 2 — Bayes in real life**
```
P(busy | weekend) = 100%      P(busy | weekday) = 17%
If today was busy, there's an 80% chance it's the weekend.
```

**Module 5 — the payoff prediction**
```
Correlation r = 0.94  -> hotter day, more cups. Strong link!
Tomorrow's forecast is 28 C  ->  make about 34 cups!
```

---

## 🧠 The honesty lesson in Module 4

Maya *thinks* her colorful new sign boosted sales. The average did go up
(29.7 → 35.2 cups)... but the hypothesis test says **the jump could still just
be luck** (p ≈ 0.19, not below 0.05).

That's on purpose. Real statistics teaches you: *a bigger number isn't proof.*
It's a perfect, gentle first lesson in not fooling yourself — try changing the
data in `src/data.py` and see how much of a jump it takes before the test is
finally convinced!

---

## 🛠️ Things to try (turn reading into doing)

- **Add your own days** to `NOTEBOOK` in `src/data.py`, then re-run — every
  number updates automatically.
- Change the "busy day" line in `module2_probability.py` from 30 to 40 cups.
- Change the forecast temperature in `module5_regression.py` and predict a new day.
- Make the sign in Module 4 *really* work by bumping up the last 10 days'
  sales — how big does the boost need to be before the test believes it?

---

## 📁 Project layout

```
lemonade-stats-for-kids/
├── README.md
├── requirements.txt
├── charts/                    # pictures saved when you run the code
└── src/
    ├── data.py                # Maya's notebook (the one dataset everything uses)
    ├── module1_describe.py    # Descriptive statistics
    ├── module2_probability.py # Probability + Bayes
    ├── module3_distributions.py
    ├── module4_estimation.py  # Confidence interval + hypothesis test
    ├── module5_regression.py  # Correlation + regression
    └── run_all.py             # runs the whole story at once
```

Built as a hands-on companion to **MATH2561 – Probability and Statistics for
Engineering**. Happy squeezing! 🍋
