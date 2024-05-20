# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 11:05:29 2017

@author: JJayanetti
"""


entry = 0 # Ensure the loop is entered
sum = 0 # Initialize sum

 # Request input from the user
print("Enter numbers to sum, negative number ends list:")

while entry >= 0: # A negative number exits the loop
    entry = eval(input()) # Get the value
    if entry >= 0: # Is number non-negative?
        sum += entry # Only add it if it is non-negative

print("Sum =", sum) # Display the sum