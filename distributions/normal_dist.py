"""

Normal Distribution

__author__ : 'vikas_rtr'
__date__ : June 2015

"""

import numpy as np
from numpy import (exp, sqrt, pi)

import matplotlib.pyplot as plt


class normal_dist():

    """Normal (Gaussian Distribution)

    location (loc) = mu
    scale = Variance = (sigma)**2

    pdf = exp(-(x-loc)**2/2*scale)/sqrt(2*scale*pi)
    """

    def __init__(self, loc=0, scale=1):
        self.loc = loc
        self.scale = scale

    def pdf(self, x):
        return exp(-(x - self.loc) ** 2 / (2. * self.scale)) / sqrt(2. * self.scale * pi)

nrm1 = normal_dist(loc=0, scale=1)
nrm2 = normal_dist(loc=1, scale=1)
nrm3 = normal_dist(loc=0, scale=0.5)
nrm4 = normal_dist(loc=-3, scale=5)
nrm5 = normal_dist(loc=2, scale=3)

fig, ax = plt.subplots(1, 1)
plt.axis([-6.50, 6.50, 0.0, 0.7])
ax.set_autoscale_on(False)

# x = np.linspace(normal_dst.ppf(0.01), normal_dst.ppf(0.99), 100)
x = np.linspace(-10.0, 10.0, 200)
plt.plot(x, nrm1.pdf(x), 'k-', lw=5, alpha=0.8, label='Normal (0,1)')
plt.plot(x, nrm2.pdf(x), 'g-', lw=2, alpha=0.6, label='Normal (1,1)')
plt.plot(x, nrm3.pdf(x), 'r-', lw=2, alpha=0.6, label='Normal (0,0.5)')
plt.plot(x, nrm4.pdf(x), 'y-', lw=2, alpha=0.6, label='Normal (-3,5)')
plt.plot(x, nrm5.pdf(x), 'c-', lw=2, alpha=0.6, label='Normal (2,3)')


# legend
legend = plt.legend(loc='upper left')
plt.xlabel('x')
plt.ylabel('pdf')
plt.title('pdf of Normal Distribution')
plt.show()
