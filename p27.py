# -*- coding: utf-8 -*-
"""
Created on Wed May  6 09:08:01 2020

@author: JJayanetti
"""

print("------------------") # table heading
C = -20 # start value for C
dC = 5 # increment of C in loop
while C <= 100: # loop heading with condition
    F = (9.0/5)*C + 32 # 1st statement inside loop
    print(C, F) # 2nd statement inside loop
    C = C + dC # 3rd statement inside loop
print("------------------") # end of table line (after loop)