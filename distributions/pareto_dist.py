"""

Pareto Distribution

__author__ : 'vikas_rtr'
__date__ : June 2015

"""

import numpy as np
from numpy import (exp, sqrt, pi)

import matplotlib.pyplot as plt


class pareto_dist():

    """Pareto Distribution

    location (loc) = xm = 1 (Assumed)
    scale = alpha = a

    pdf = exp(-(x-loc)**2/2*scale)/sqrt(2*scale*pi)
    """

    def __init__(self, scale=1):
        self.a = scale

    def pdf(self, x):
        return self.a / (x ** (self.a + 1))

prt1 = pareto_dist(scale=1)
prt2 = pareto_dist(scale=2)
prt3 = pareto_dist(scale=3)

fig, ax = plt.subplots(1, 1)
plt.axis([0.0, 5.0, 0.0, 3.0])
ax.set_autoscale_on(False)

# x = np.linspace(pareto_dst.ppf(0.01), pareto_dst.ppf(0.99), 100)
x = np.linspace(1.0, 10.0, 200)
plt.plot(x, prt1.pdf(x), 'r-', lw=1, alpha=0.8, label='pareto (1)')
plt.plot(x, prt2.pdf(x), 'g-', lw=1, alpha=0.8, label='pareto (2)')
plt.plot(x, prt3.pdf(x), 'c-', lw=1, alpha=0.8, label='pareto (2)')

# draw x = 1
plt.plot([1,1],[0,3],'k-')

# legend
legend = plt.legend(loc='upper right')
plt.xlabel('x')
plt.ylabel('pdf')
plt.title('pdf of pareto Distribution x ~ [1,inf)')
plt.show()
