"""
Run the WHOLE lemonade adventure, Module 1 -> Module 5, in order.

Just run:   python src/run_all.py
"""

from data import print_notebook
from module1_describe import describe
from module2_probability import probability
from module3_distributions import distributions
from module4_estimation import estimation
from module5_regression import regression


def banner(text):
    print("\n" + "=" * 60)
    print(text)
    print("=" * 60)


if __name__ == "__main__":
    banner("MAYA'S LEMONADE STAND — a whole statistics course in one story")
    print_notebook()

    banner("MODULE 1")
    describe()
    banner("MODULE 2")
    probability()
    banner("MODULE 3")
    distributions()
    banner("MODULE 4")
    estimation()
    banner("MODULE 5")
    regression()

    banner("THE END — you just used all 5 modules on real data. Nice work!")
