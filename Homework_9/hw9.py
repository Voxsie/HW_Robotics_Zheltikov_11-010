import colorsys
import math

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='polar')

# Radius of 1, distance from center to outer edge
rho = np.linspace(0, 1, 100)
# in radians, one full circle
phi = np.linspace(0, math.pi * 2.0, 1000)

# get every combination of rho and phi
RHO, PHI = np.meshgrid(rho, phi)

# use angle to determine hue, normalized from 0-1
h = (PHI - PHI.min()) / (PHI.max() - PHI.min())
h = np.flip(h)
# saturation is set as a function of radias
s = RHO
# value is constant
v = np.ones_like(RHO)

h, s, v = h.flatten().tolist(), s.flatten().tolist(), v.flatten().tolist()
c = [colorsys.hsv_to_rgb(*x) for x in zip(h, s, v)]
c = np.array(c)

ax.scatter(PHI, RHO, c=c)
res = ax.axis('off')

plt.show()
