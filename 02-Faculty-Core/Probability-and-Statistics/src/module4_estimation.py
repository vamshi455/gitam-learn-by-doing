"""
MODULE 4 — Estimation & Tests of Significance
=============================================
Curriculum: sampling, standard error, interval estimation,
            tests of inference about means (small-sample t-test).

Big questions a kid can ask:
   1. "From my 20 days, how sure am I about my TRUE average sales?"
      -> a CONFIDENCE INTERVAL ("I'm 95% sure the real average is between _ and _")
   2. "Halfway through, I put up a big colorful SIGN. Did it REALLY help,
       or did I just get lucky?"
      -> a HYPOTHESIS TEST comparing the first 10 days vs the last 10 days.
"""

from scipy import stats
import statistics as pystats
from data import CUPS_SOLD


def estimation():
    cups = CUPS_SOLD
    n = len(cups)

    # ---------- 1. CONFIDENCE INTERVAL for the true average ----------
    mean = pystats.mean(cups)
    sd   = pystats.stdev(cups)              # sample standard deviation
    se   = sd / (n ** 0.5)                  # standard error of the mean
    # t value for 95% confidence with (n-1) degrees of freedom
    t_crit = stats.t.ppf(0.975, df=n - 1)
    low  = mean - t_crit * se
    high = mean + t_crit * se

    print("MODULE 4 — How sure can Maya be?\n")
    print("  (1) A 95% confidence interval for her TRUE average sales")
    print(f"      Sample average   = {mean:.1f} cups")
    print(f"      Standard error   = {se:.2f}")
    print(f"      95% interval     = {low:.1f} to {high:.1f} cups")
    print(f"      Meaning: 'I'm 95% confident my real day-to-day average")
    print(f"               sits somewhere between {low:.0f} and {high:.0f} cups.'\n")

    # ---------- 2. HYPOTHESIS TEST: did the sign help? ----------
    before = cups[:10]   # first 10 days  (no sign)
    after  = cups[10:]   # last 10 days   (with the new sign)

    mean_before = pystats.mean(before)
    mean_after  = pystats.mean(after)

    # Two-sample t-test: is the "after" average really higher?
    t_stat, p_two_sided = stats.ttest_ind(after, before, equal_var=False)
    p_one_sided = p_two_sided / 2  # we only care if AFTER is HIGHER

    print("  (2) Did the colorful SIGN actually boost sales?")
    print(f"      Average BEFORE sign (days 1-10) = {mean_before:.1f} cups")
    print(f"      Average AFTER  sign (days 11-20) = {mean_after:.1f} cups")
    print(f"      t-statistic = {t_stat:.2f},  p-value = {p_one_sided:.3f}\n")

    if p_one_sided < 0.05:
        print(f"      p is below 0.05 -> the jump is UNLIKELY to be luck.")
        print(f"      Conclusion: the sign REALLY did help! Keep it up, Maya.\n")
    else:
        print(f"      p is above 0.05 -> could just be luck. Not enough proof.\n")


if __name__ == "__main__":
    estimation()
