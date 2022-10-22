import random

import numpy as np


def monte_carlo_pi(n_samples):
    acc = 0
    for i in range(n_samples):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
    return 4.0 * acc / n_samples


def get_areas(radii, n_samples):
    a = np.zeros_like(radii)
    for i, r in enumerate(radii):
        pi = monte_carlo_pi(n_samples)
        a[i] = pi * r ** 2
