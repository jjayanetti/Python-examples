# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 12:37:50 2024

@author: JJayanetti
"""
import math
import random

f = open('data.txt', 'w')
#f.write('This is a test.\n')
num1=str(math.sin(2 * math.pi / 180));

limit=100;

for x in range(limit):
    num=str(math.sin((random.random() * math.pi) / 180));
    f.write(num+'\n');
f.close()