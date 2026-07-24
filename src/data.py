"""
Maya's Lemonade Stand — the data we collected.

Every summer weekend, Maya opened a lemonade stand outside her house.
For 20 days she wrote down 4 things in her notebook:

  1. day        -> which day number it was (1 to 20)
  2. temperature -> how hot it was outside (in degrees Celsius)
  3. weekend     -> was it a weekend? (True = Sat/Sun, False = weekday)
  4. cups_sold   -> how many cups of lemonade she sold that day

Everything we learn in this whole project comes from THIS notebook.
No scary made-up numbers — just Maya writing down what happened.
"""

# Each row is one day: (day, temperature_C, weekend, cups_sold)
NOTEBOOK = [
    (1,  22, False, 18),
    (2,  24, False, 21),
    (3,  26, True,  34),
    (4,  27, True,  38),
    (5,  21, False, 15),
    (6,  23, False, 20),
    (7,  29, False, 30),
    (8,  31, True,  45),
    (9,  33, True,  52),
    (10, 25, False, 24),
    (11, 20, False, 12),
    (12, 28, False, 29),
    (13, 30, True,  44),
    (14, 32, True,  50),
    (15, 24, False, 19),
    (16, 26, False, 25),
    (17, 34, False, 41),
    (18, 35, True,  58),
    (19, 30, True,  46),
    (20, 27, False, 28),
]

# Handy separate lists (columns) so the module scripts can grab what they need.
DAYS         = [row[0] for row in NOTEBOOK]
TEMPERATURE  = [row[1] for row in NOTEBOOK]
IS_WEEKEND   = [row[2] for row in NOTEBOOK]
CUPS_SOLD    = [row[3] for row in NOTEBOOK]


def print_notebook():
    """Print Maya's notebook as a neat table."""
    print("Maya's Lemonade Stand Notebook")
    print("-" * 44)
    print(f"{'Day':>4} {'Temp(C)':>8} {'Weekend':>9} {'Cups':>6}")
    print("-" * 44)
    for day, temp, weekend, cups in NOTEBOOK:
        print(f"{day:>4} {temp:>8} {str(weekend):>9} {cups:>6}")
    print("-" * 44)
    print(f"{len(NOTEBOOK)} days recorded.\n")


if __name__ == "__main__":
    print_notebook()
