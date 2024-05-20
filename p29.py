# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:03:07 2020

@author: JJayanetti
"""

def median(a,b,c):
    if a<b and b<c or a>b and b>c:
        return b
    if b<a and a<c or b>a and a>c:
        return a
    if c<a and b<c or c>a and b>c:
        return c

def main():
    x=float(input("Enter the first value: " ))
    y=float(input("Enter the second value: "))
    z=float(input("Enter the third value: "))
    print("The median value is:",median(x,y,z))
    
main()