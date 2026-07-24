"""
MODULE 2 — Probability, Conditional Probability & Bayes' Theorem
================================================================
Curriculum: sample spaces & events, axioms of probability,
            conditional probability, Bayes' theorem, independence.

Big question a kid can ask:
   "What are the CHANCES my day is a busy one? And if it's a weekend,
    does that change the chances?"

We call a day BUSY if Maya sold 30 or more cups.
Probability here just means:  (days that fit) / (all days).
"""

from data import NOTEBOOK

BUSY_LINE = 30  # 30+ cups = a "busy" day


def probability():
    total_days = len(NOTEBOOK)

    busy_days     = [d for d in NOTEBOOK if d[3] >= BUSY_LINE]
    weekend_days  = [d for d in NOTEBOOK if d[2] is True]
    weekend_busy  = [d for d in weekend_days if d[3] >= BUSY_LINE]
    weekday_days  = [d for d in NOTEBOOK if d[2] is False]
    weekday_busy  = [d for d in weekday_days if d[3] >= BUSY_LINE]

    # --- Simple probability ---
    p_busy    = len(busy_days) / total_days
    p_weekend = len(weekend_days) / total_days

    print("MODULE 2 — What are the chances?\n")
    print(f"  A 'busy day' = selling {BUSY_LINE}+ cups.\n")
    print(f"  P(busy day)          = {len(busy_days)}/{total_days} = {p_busy:.0%}")
    print(f"  P(it's a weekend)    = {len(weekend_days)}/{total_days} = {p_weekend:.0%}\n")

    # --- Conditional probability: busy GIVEN weekend ---
    p_busy_given_weekend = len(weekend_busy) / len(weekend_days)
    p_busy_given_weekday = len(weekday_busy) / len(weekday_days)

    print("  Now the fun part — does the weekend matter?")
    print(f"  P(busy | weekend) = {len(weekend_busy)}/{len(weekend_days)} = {p_busy_given_weekend:.0%}")
    print(f"  P(busy | weekday) = {len(weekday_busy)}/{len(weekday_days)} = {p_busy_given_weekday:.0%}\n")
    print(f"  Weekends are WAY more likely to be busy. So 'busy' and 'weekend'")
    print(f"  are NOT independent — knowing one changes the chance of the other.\n")

    # --- Bayes' theorem: flip the question around ---
    # We know P(busy | weekend). Bayes lets us find P(weekend | busy):
    #   "If today was busy, how likely is it that it's a weekend?"
    p_weekend_given_busy = (p_busy_given_weekend * p_weekend) / p_busy

    print("  Bayes' theorem lets us flip the question:")
    print(f"  P(weekend | busy) = P(busy|weekend) * P(weekend) / P(busy)")
    print(f"                    = {p_busy_given_weekend:.2f} * {p_weekend:.2f} / {p_busy:.2f}")
    print(f"                    = {p_weekend_given_busy:.0%}")
    print(f"  So if Maya just had a busy day, there's a {p_weekend_given_busy:.0%} chance")
    print(f"  it's the weekend. (Quick check against the notebook:")
    print(f"  {len(weekend_busy)} of {len(busy_days)} busy days were weekends"
          f" = {len(weekend_busy)/len(busy_days):.0%}. It matches!)\n")


if __name__ == "__main__":
    probability()
