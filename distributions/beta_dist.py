"""

Beta Distribution

__author__ : 'vikas_rtr'
__date__ : June 2015

"""

import numpy as np
from numpy import (exp, sqrt, pi)
from scipy.special import gamma

import matplotlib.pyplot as plt


class beta_dist():

    """Beta Distribution

    Interval : [0,1]
    loc = alpha = a
    scale = beta = b

    pdf = (gamma(a+b)* (x**(a-1))*((1-x)**(b-1)))/(gamma(a)*gamma(b))
    """

    def __init__(self, loc=0, scale=1):
        self.a = loc
        self.b = scale

    def pdf(self, x):
        return (gamma(self.a + self.b) * (x ** (self.a - 1)) * ((1 - x) ** (self.b - 1))) / (gamma(self.a) * gamma(self.b))

bta1 = beta_dist(loc=0.5, scale=0.5)
bta2 = beta_dist(loc=5.0, scale=1.0)
bta3 = beta_dist(loc=1.0, scale=3.0)
bta4 = beta_dist(loc=2.0, scale=2.0)
bta5 = beta_dist(loc=2.0, scale=5.0)

fig, ax = plt.subplots(1, 1)
plt.axis([0.0, 1.0, 0.0, 2.5])
ax.set_autoscale_on(False)

x = np.linspace(0.01, 1.0, 200)
plt.plot(x, bta1.pdf(x), 'r-', lw=1, alpha=0.8, label='beta (0.5,0.5)')
plt.plot(x, bta2.pdf(x), 'm-', lw=1, alpha=0.8, label='beta (5,1)')
plt.plot(x, bta3.pdf(x), 'g-', lw=1, alpha=0.8, label='beta (1,3)')
plt.plot(x, bta4.pdf(x), 'k-', lw=1, alpha=0.8, label='beta (2,2)')
plt.plot(x, bta5.pdf(x), 'y-', lw=1, alpha=0.8, label='beta (2,5)')

# legend
legend = plt.legend(loc='upper right')
plt.xlabel('x')
plt.ylabel('pdf')
plt.title('pdf of Beta Distribution')
plt.show()
