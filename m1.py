# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 11:37:27 2024

@author: JJayanetti
"""

D = {'a': 1, 'b': 2, 'c': 3}
Ks = list(D.keys())
Ks.sort()
print(Ks)

for key in Ks:
    print(key, '=>', D[key])