# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 13:21:05 2020

@author: jjayanetti
"""
i=0
sum=0
while i < 999:
    i=i+1
    if(i % 3 == 0 or i % 5 == 0):
        sum=sum+i

print(sum)
print(i)