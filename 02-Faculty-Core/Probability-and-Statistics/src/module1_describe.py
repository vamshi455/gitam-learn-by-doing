"""
MODULE 1 — Describing the Data
================================
Curriculum: measures of location & variability, standard deviation,
            coefficient of variation, graphical displays.

Big question a kid can ask:
   "On a normal day, how many cups do I sell — and how bumpy is it?"

We answer with 4 simple ideas:
   * MEAN    -> the average (add them all up, share equally)
   * MEDIAN  -> the middle number when you line them up
   * STD DEV -> how far, typically, a day is from the average (the "wobble")
   * CV      -> the wobble compared to the average, as a percent
"""

import statistics as stats
import matplotlib.pyplot as plt
from data import CUPS_SOLD, DAYS


def describe():
    cups = CUPS_SOLD

    mean   = stats.mean(cups)
    median = stats.median(cups)
    lowest = min(cups)
    highest = max(cups)
    spread = highest - lowest            # the "range"
    std    = stats.pstdev(cups)          # population standard deviation
    cv     = (std / mean) * 100          # coefficient of variation (a percent)

    print("MODULE 1 — Describing Maya's sales\n")
    print(f"  Days counted   : {len(cups)}")
    print(f"  Average (mean) : {mean:.1f} cups per day")
    print(f"  Middle (median): {median:.1f} cups")
    print(f"  Worst day      : {lowest} cups")
    print(f"  Best day       : {highest} cups")
    print(f"  Range (spread) : {spread} cups")
    print(f"  Std deviation  : {std:.1f} cups  <- typical wobble around the average")
    print(f"  Coeff of var   : {cv:.0f}%       <- wobble is about {cv:.0f}% of the average\n")

    print("  In kid words:")
    print(f"    On a typical day Maya sells about {mean:.0f} cups, but any single")
    print(f"    day is usually within ~{std:.0f} cups of that. Some days are")
    print(f"    much busier than others — that's the {cv:.0f}% coefficient of variation.\n")

    # A picture is worth 1000 numbers — bar chart of every day.
    plt.figure(figsize=(9, 4))
    plt.bar(DAYS, cups, color="#f4c542", edgecolor="#b8860b")
    plt.axhline(mean, color="red", linestyle="--", label=f"average = {mean:.0f}")
    plt.title("Cups of lemonade sold each day")
    plt.xlabel("Day")
    plt.ylabel("Cups sold")
    plt.xticks(DAYS)
    plt.legend()
    plt.tight_layout()
    plt.savefig("charts/module1_sales_bar.png", dpi=120)
    print("  Saved a bar chart -> charts/module1_sales_bar.png")


if __name__ == "__main__":
    describe()
