# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 15:59:09 2018

@author: JJayanetti
"""

def count_to_20():
    for i in range(1, 21):
        print(i)

def count_to_10():
    for i in range(1, 11):
        print(i)

def count_to_n(n):
    for i in range(1, n+1):
        print(i)

def count_to_n_print_to_file(n):
    #f=open('count9.txt', 'w')
    f=open('count10.txt', 'a')
    for i in range(1, n+1):
        print(i)
        f.write(str(i))
        f.write('\n')
    f.close
#print("Going to count to twenty . . .")
#count_to_20()
#print("Going to count to twenty again. . .")
#count_to_20()

#print("Going to count to ten . . .")
#count_to_10()

#count_to_n(100)

count_to_n_print_to_file(1000)