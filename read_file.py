# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 14:17:39 2020

@author: JJayanetti
"""
filename="input_file.txt"
file=open(filename,'r')
for line in file:
    print(line)

file.close()