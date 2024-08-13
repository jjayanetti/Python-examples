# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 11:58:58 2024

@author: JJayanetti
"""

import matplotlib.pyplot as plt
import random
position=0
walk=[position]
nsteps=2000
for _ in range(nsteps):
    step=1 if random.randint(0,1) else -1
    position += step
    walk.append(position)

plt.plot(walk[:1000])
plt.grid()
