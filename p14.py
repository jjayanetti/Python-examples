# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 11:29:24 2018

@author: jjayanetti
"""

from random import randrange, seed
seed(25)

for i in range(0,100):
    print(randrange(1,100),end=' ')
print("Finished processing.")