# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 14:04:47 2020

@author: jjayanetti
"""

num=510

# check for factors
for i in range(2,num):
    if (num % i) == 0:
       print(num,"is not a prime number")
       print(i,"times",num//i,"is",num)
       break
else:
    print(num,"is a prime number")