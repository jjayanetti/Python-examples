# -*- coding: utf-8 -*-
"""
Created on Tue May 14 14:53:42 2024

@author: JJayanetti
"""

from random import randrange

def random_list():
    result=[]
    count=randrange(1,20)
    for i in range(count):
        result+=[randrange(-50,50)]
    return result


def rev(lst):
    return [] if len(lst)==0 else rev(lst[1:]) + lst[0:1]

def main():
    for n in range(6):
        lst=random_list();
        print(lst);
        rev_lst=rev(lst);
        print(rev_lst);
        print('=========================')

main()