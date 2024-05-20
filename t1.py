# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 10:34:22 2019

@author: JJayanetti
"""

import numpy
nums = [1, 4.5, 6.25, 8, 10, 15]
a = numpy.array(nums)
print(a)
print(a+1)
b = numpy.zeros(shape=10,dtype=float)
print(b)
grid = numpy.zeros(shape=(10,10),dtype=float)
print(grid)
grid[2:4] = 1
print(grid)
    