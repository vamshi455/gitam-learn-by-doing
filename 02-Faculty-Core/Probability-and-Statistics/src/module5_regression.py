"""
MODULE 5 — Correlation & Regression
===================================
Curriculum: correlation, simple linear regression, standard error of
            the estimate, using regression to make predictions.

Big questions a kid can ask:
   * "Do hotter days REALLY mean more lemonade sold?" (correlation)
   * "Can I draw ONE straight line that predicts sales from temperature?"
     (linear regression)
   * "Tomorrow the forecast is 28 C — how many cups should I make?"
     (prediction)
"""

from scipy import stats
import matplotlib.pyplot as plt
from data import TEMPERATURE, CUPS_SOLD


def regression():
    temp = TEMPERATURE
    cups = CUPS_SOLD

    # ---------- CORRELATION ----------
    r, _ = stats.pearsonr(temp, cups)
    print("MODULE 5 — Do hotter days sell more lemonade?\n")
    print(f"  Correlation r = {r:.2f}")
    print(f"  r is close to +1, so YES: hotter day -> more cups. Strong link!\n")

    # ---------- LINEAR REGRESSION ----------
    # Find the best straight line:  cups = slope * temp + intercept
    result = stats.linregress(temp, cups)
    slope, intercept = result.slope, result.intercept

    print("  Best-fit line:  cups = {:.2f} * temp + ({:.1f})".format(slope, intercept))
    print(f"    slope = {slope:.2f}  -> each extra degree adds ~{slope:.1f} cups sold")
    print(f"    r-squared = {result.rvalue**2:.0%}  -> temperature explains "
          f"{result.rvalue**2:.0%} of the ups and downs\n")

    # ---------- PREDICTION ----------
    forecast_temp = 28
    predicted = slope * forecast_temp + intercept
    print(f"  Tomorrow's forecast is {forecast_temp} C.")
    print(f"  Predicted sales = {slope:.2f} * {forecast_temp} + ({intercept:.1f})"
          f" = {predicted:.0f} cups")
    print(f"  So Maya should squeeze enough lemons for about {predicted:.0f} cups!\n")

    # ---------- PICTURE: dots + the line ----------
    line_x = [min(temp), max(temp)]
    line_y = [slope * x + intercept for x in line_x]
    plt.figure(figsize=(8, 5))
    plt.scatter(temp, cups, color="#2a9d8f", label="each day")
    plt.plot(line_x, line_y, color="red", label="best-fit line")
    plt.scatter([forecast_temp], [predicted], color="orange", s=120,
                zorder=5, label=f"prediction ({forecast_temp}C)")
    plt.title("Temperature vs Cups Sold")
    plt.xlabel("Temperature (C)")
    plt.ylabel("Cups sold")
    plt.legend()
    plt.tight_layout()
    plt.savefig("charts/module5_regression.png", dpi=120)
    print("  Saved a scatter + line chart -> charts/module5_regression.png")


if __name__ == "__main__":
    regression()
