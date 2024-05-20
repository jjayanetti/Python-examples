# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 14:47:35 2018

@author: JJayanetti
"""

import numpy as np
import matplotlib.pyplot as plt
import sklearn.cluster

# Fixing random state for reproducibility
np.random.seed(19680801)


N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()