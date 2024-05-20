# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 14:14:20 2020

@author: jjayanetti
"""

##num = input('Enter any number : ')
#from array import *
#import numpy as np
#from numpy import array
num_array=[]

for x in range(100,999):
    try:
        #val = int(num)
        #x = int(x)
        if str(x) == str(x)[::-1]:
            #print('The given number is PALINDROME')
            num_array.append(x)
        
    except ValueError:
        print("That's not a valid number, Try Again !")

#print(num_array[0])
print(num_array)
#print(max(np))

def palindrome(x):
    if str(x) == str(x)[::-1]:
        return 1
            
        

for x in range(100,999):
    for y in range(100,999):
        if(palindrome(x*y)):
            num_array.append(x*y)
            

print(num_array)
print(max(num_array))
