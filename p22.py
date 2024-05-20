# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 13:29:11 2020

@author: jjayanetti
"""


sum=0
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10
limit=4000000
# check if the number of terms is valid
#if nterms <= 0:
#   print("Please enter a positive integer: ")
#else:
#   print("Fibonacci sequence:")
   #for i in range(nterms):
i=0
while(recur_fibo(i)<=limit):
    #print(recur_fibo(i))
    if(recur_fibo(i) % 2 == 0):
        sum+=recur_fibo(i)
    i+=1     
print(sum)