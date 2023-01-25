# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 13:05:56 2023

@author: rozmu
"""

def square_digits(number):
     
    listA = [int(x) for x in str(number)]
    listAB = [str(num ** 2) for num in listA]
    return (int( ''.join(listAB)))