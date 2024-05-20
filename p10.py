# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:18:59 2018

@author: JJayanetti
"""


def random_function(N1, N2):
    import random
    f=open('count12.txt', 'w')
    for x in range(N1):
        i=random.randint(1, N2)
        print(i)
        f.write(str(i))
        f.write('\n')
        #print randint(1, N2)
    f.close    


random_function(100,100)