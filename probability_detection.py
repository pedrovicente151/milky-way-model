# Calculating Probability of Detection for a Range of Civilizations #
#  Drake equation : N = R * fp * ne * fl * fi * fc * L
#  ===========================================================================
from random import randint
from collections import Counter
import numpy
import matplotlib.pyplot as plt

NUM_EQUIV_VOLUMES = 1000  # Number of locations in which to place civilizations.
MAX_CIVS = 5000  # Maximum number of advanced civilizations.
TRIALS = 1000  # Number of times to model a given number of civilizations.
CIV_STEP_SIZE = 100  # Civilizations count step size.

x = []
y = []

for num_civs in range(2, MAX_CIVS + 2, CIV_STEP_SIZE):
    civs_per_vol = num_civs / NUM_EQUIV_VOLUMES
    num_single_civs = 0
    for trial in range(TRIALS):
        locations = []  # Equivalent volumes containing a civilization
        while len(locations) < num_civs:
            location = randint(1, NUM_EQUIV_VOLUMES)
            locations.append(location)

        overlap_count = Counter(locations)
        over_lap_rollup = Counter(overlap_count.values())
        num_single_civs += over_lap_rollup[1]

    prob = 1 - (num_single_civs / (num_civs * TRIALS))

    #  Print ratio of civs-per-volume vs. probability of 2+ civs per location.
    print("{:.4f}  {:.4f}".format(civs_per_vol, prob))
    x.append(civs_per_vol)
    y.append(prob)

#  Predictive Formula
    coefficients = numpy.polyfit(x, y, 4)
    p = numpy.poly1d(coefficients)
    print("\n{}".format(p))
    xp = numpy.linspace(0, 5)
    _ = plt.plot(x, y, ".", xp, p(xp), "-")
    plt.ylim(-0.5, 1.5)
    plt.show()
