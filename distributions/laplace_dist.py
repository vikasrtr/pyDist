"""

Laplace Distribution

__author__ : 'vikas_rtr'
__date__ : June 2015

"""

import numpy as np
from numpy import (exp, sqrt, pi)

import matplotlib.pyplot as plt


class laplace_dist():

    """Laplace Distribution

    location (loc) = mu
    scale = b

    pdf = exp(-abs(x-mu)/b)/(2*b)
    """

    def __init__(self, loc=0, scale=1):
        self.mu = loc
        self.b = scale

    def pdf(self, x):
        return exp(-np.abs(x - self.mu) / self.b) / (2 * self.b)

lplc1 = laplace_dist(loc=0, scale=1)
lplc2 = laplace_dist(loc=0, scale=2)
lplc3 = laplace_dist(loc=0, scale=4)
lplc4 = laplace_dist(loc=-5, scale=4)

fig, ax = plt.subplots(1, 1)
plt.axis([-10.0, 10.0, 0.0, 0.5])
ax.set_autoscale_on(False)

# x = np.linspace(laplace_dst.ppf(0.01), laplace_dst.ppf(0.99), 100)
x = np.linspace(-15.0, 15.0, 400)
plt.plot(x, lplc1.pdf(x), 'c-', lw=1, alpha=0.8, label='laplace (0,1)')
plt.plot(x, lplc2.pdf(x), 'g-', lw=1, alpha=0.8, label='laplace (0,2)')
plt.plot(x, lplc3.pdf(x), 'r-', lw=1, alpha=0.8, label='laplace (0,4)')
plt.plot(x, lplc4.pdf(x), 'k-', lw=1, alpha=0.8, label='laplace (5,4)')


# legend
legend = plt.legend(loc='upper left')
plt.xlabel('x')
plt.ylabel('pdf')
plt.title('pdf of laplace Distribution')
plt.show()
