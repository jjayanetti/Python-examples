# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 11:34:19 2018

@author: jjayanetti
"""
def random_print(n):
    from random import randrange, seed
    seed(25)

    for i in range(0,n):
        print(randrange(1,1000),end='\n')
        

random_print(10)
