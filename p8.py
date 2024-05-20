# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 15:43:11 2018

@author: JJayanetti
"""

sum = 0 # Initialize sum
print('Please enter an integer value:')
N = int(input())

for i in range(1, N):
    sum += i
print('Sum=' + str(sum))
