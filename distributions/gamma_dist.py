"""

Gamma Distribution

__author__ : 'vikas_rtr'
__date__ : June 2015

"""

import numpy as np
from numpy import (exp, sqrt, pi)
from scipy.special import gamma

import matplotlib.pyplot as plt


class gamma_dist():

    """Gamma Distribution

    shape = k = a
    scale = theta = 1/rate

    pdf = ((b**a)*(x**(a-1))*exp(-b*x))/gamma(a)
    """

    def __init__(self, shape=1, scale=1):
        self.shape = shape
        self.rate = 1. / scale

    def pdf(self, x):
        return ((self.rate ** self.shape) * (x ** (self.shape - 1)) * exp(-self.rate * x)) / gamma(self.shape)

gma1 = gamma_dist(shape=1.0, scale=2.0)
gma2 = gamma_dist(shape=2.0, scale=2.0)
gma3 = gamma_dist(shape=3.0, scale=2.0)
gma4 = gamma_dist(shape=5.0, scale=1.0)
gma5 = gamma_dist(shape=9.0, scale=0.5)
gma6 = gamma_dist(shape=7.5, scale=1.0)
gma7 = gamma_dist(shape=0.5, scale=1.0)

fig, ax = plt.subplots(1, 1)
plt.axis([0.0, 20.0, 0.0, 0.5])
ax.set_autoscale_on(False)

x = np.linspace(0.01, 20.0, 800)
plt.plot(x, gma1.pdf(x), 'k-', lw=2, alpha=0.8, label='gamma (1,2)')
plt.plot(x, gma2.pdf(x), 'm-', lw=1, alpha=0.8, label='gamma (2,2)')
plt.plot(x, gma3.pdf(x), 'g-', lw=1, alpha=0.8, label='gamma (3,2)')
plt.plot(x, gma4.pdf(x), 'r-', lw=1, alpha=0.8, label='gamma (5,1)')
plt.plot(x, gma5.pdf(x), 'y-', lw=1, alpha=0.8, label='gamma (9,0.5)')
plt.plot(x, gma6.pdf(x), 'b-', lw=1, alpha=0.8, label='gamma (7.5,1)')
plt.plot(x, gma7.pdf(x), 'c-', lw=1, alpha=0.8, label='gamma (0.5,1)')


# legend
legend = plt.legend(loc='upper right')
plt.xlabel('x')
plt.ylabel('pdf')
plt.title('pdf of gamma Distribution')
plt.show()
