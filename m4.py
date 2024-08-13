# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 12:16:34 2024

@author: JJayanetti
"""

import numpy as np

points=np.arange(-5,5,0.01);
xs, ys = np.meshgrid(points,points);
z=np.sqrt(xs**2 + ys**2);

import matplotlib.pyplot as plt;

plt.imshow(z,cmap=plt.cm.gray,extent=[-5,5,-5,5])
plt.colorbar()
plt.show()


