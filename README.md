# 🎓 GITAM · Learn by Doing

**Practical, hands-on guidance for the GITAM B.Tech CSE (AI & ML) curriculum —
one real-world problem at a time.**

> *"Build a dynamic application-oriented education ecosystem."* — GITAM Mission
>
> This repo takes that idea literally. For **every subject** in the degree, it
> answers the question a student actually cares about: *"Okay… but what can I
> DO with this, and why does it matter in the real world?"*

---

## 💡 Why this repo exists

Textbooks tell you the theory. This repo starts from the other end:

1. **A real-world problem** a student can picture and care about.
2. The subject's ideas show up **naturally** while solving it.
3. You **learn by building**, not by memorising.

Every folder maps to a subject in the official GITAM curriculum, and every
subject page gives you plain-language guidance **plus a practical problem to
try.** Some already ship with complete, runnable code — starting with
Probability & Statistics.

---

## 🗂️ How the repo is organised (by subject)

The folders mirror the exact structure of the GITAM curriculum, so a student can
walk straight from their timetable to the matching folder:

| Folder | Category | What you'll find |
|--------|----------|------------------|
| [01-University-Core/](01-University-Core/) | Common to all GITAM students | Critical thinking, entrepreneurship, personal finance, environment, constitution |
| [02-Faculty-Core/](02-Faculty-Core/) | Science & engineering base | Maths, physics, chemistry, programming — **incl. a full working Statistics project** ✅ |
| [03-Programme-Core/](03-Programme-Core/) | The AI/ML heart | Data structures, algorithms, DBMS, networks, AI, ML, NLP, deep learning |
| [04-Programme-Electives/](04-Programme-Electives/) | Choose your path | Themed bundles: Computational Biology, FinTech, Telecom, and 40+ general electives |
| [05-Open-Electives/](05-Open-Electives/) | Broaden out | Courses from within & beyond the School + Minor/Honors info |
| [curriculum/](curriculum/CURRICULUM.md) | The map | A friendly summary of the whole 160-credit degree |

---

## ⭐ Featured, fully-built project — Probability & Statistics 🍋

The first subject is done end-to-end so you can see exactly what "learn by doing"
looks like: **[Maya's Lemonade Stand](02-Faculty-Core/Probability-and-Statistics/)**.

One fun dataset (weather → lemonade sales) teaches an entire Probability &
Statistics course — descriptive stats, probability & Bayes, distributions,
confidence intervals, hypothesis testing, and regression — all in runnable,
heavily-commented Python.

```bash
cd 02-Faculty-Core/Probability-and-Statistics
pip install -r requirements.txt
python src/run_all.py
```

Every other subject folder currently ships **guidance + a practical problem to
try** — a clear on-ramp, and an open invitation to build the worked version next.

---

## 🧭 How a student should use this

- **Following a class?** Open the matching subject folder and read the "practical
  real-world problem" — it makes the lectures click.
- **Bored and curious?** Pick any folder and build the suggested project.
- **Want to contribute?** Turn a "guidance only" folder into a full worked
  example like the Statistics one. That's the whole point. 🚀

---

## 📌 About

Built as a hands-on companion to the **GITAM School of Computer Science and
Engineering** curriculum — *UCSEN03: B.Tech CSE (Artificial Intelligence and
Machine Learning)*, 2025–26 batch. Not an official GITAM publication; a
student-friendly learning aid. Official regulations:
https://www.gitam.edu/academics/academic-regulations

*Learn the theory. Then go build something. 🛠️*
