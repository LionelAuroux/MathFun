#!/usr/bin/env python3
from random import *
import matplotlib.pyplot as plt

# Seed the random number generator
seed(42)

# Initialize random numbers: random_numbers
random_numbers = [None] * 100000

# Generate random numbers by looping over range(100000)
for i in range(100000):
    random_numbers[i] = random()

# Plot a histogram
plt.hist(random_numbers)

# Show the plot
plt.show()
