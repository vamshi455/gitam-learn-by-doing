"""
MODULE 3 — Probability Distributions
====================================
Curriculum: Binomial, Poisson, Geometric (discrete);
            Normal (continuous); their mean & variance and uses.

Big questions a kid can ask:
   * BINOMIAL: "10 people walk up. Each has a 40% chance of buying a LARGE
               cup. What's the chance exactly 4 buy large?"
   * POISSON:  "On average 6 customers come each hour. What's the chance
               a quiet hour brings only 2?"
   * GEOMETRIC:"How many customers until my FIRST large-cup sale?"
   * NORMAL:   "Temperatures wobble around an average in a bell shape.
               What's the chance tomorrow is warmer than 30 C?"
"""

from scipy import stats
from data import TEMPERATURE
import statistics as pystats


def distributions():
    print("MODULE 3 — Four famous distributions, one lemonade stand\n")

    # ---------- BINOMIAL ----------
    # n independent tries, each with the same success chance p.
    n, p = 10, 0.40
    exactly_4 = stats.binom.pmf(4, n, p)
    print("  BINOMIAL — 10 customers, each 40% likely to buy a LARGE cup")
    print(f"    P(exactly 4 buy large) = {exactly_4:.0%}")
    print(f"    Expected large cups    = n*p = {n*p:.0f} out of 10\n")

    # ---------- POISSON ----------
    # Counts of events in a fixed time, given an average rate 'lam'.
    lam = 6  # average customers per hour
    only_2 = stats.poisson.pmf(2, lam)
    print("  POISSON — on average 6 customers arrive each hour")
    print(f"    P(a quiet hour with only 2) = {only_2:.0%}")
    print(f"    Expected customers per hour = {lam}\n")

    # ---------- GEOMETRIC ----------
    # How many tries until the FIRST success (p = 0.40 for a large cup).
    first_on_3rd = stats.geom.pmf(3, 0.40)
    print("  GEOMETRIC — waiting for the first LARGE-cup buyer (p = 40%)")
    print(f"    P(3rd customer is the first large sale) = {first_on_3rd:.0%}")
    print(f"    On average, first large sale by customer #{1/0.40:.1f}\n")

    # ---------- NORMAL ----------
    # Continuous bell curve. We use Maya's real temperatures.
    mu    = pystats.mean(TEMPERATURE)
    sigma = pystats.pstdev(TEMPERATURE)
    warmer_than_30 = 1 - stats.norm.cdf(30, mu, sigma)
    print("  NORMAL — temperatures form a bell curve")
    print(f"    Average temp = {mu:.1f} C, std dev = {sigma:.1f} C")
    print(f"    P(tomorrow warmer than 30 C) = {warmer_than_30:.0%}")
    print(f"    (Warmer days tend to mean more lemonade — see Module 5!)\n")


if __name__ == "__main__":
    distributions()
