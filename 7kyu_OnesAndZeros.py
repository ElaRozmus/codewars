# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 13:00:05 2023

@author: rozmu
"""

def binary_array_to_number(arr):
    total = 0
    number = 1
    for num in arr[::-1]:
        total += (number*num)
        number *= 2
    return total