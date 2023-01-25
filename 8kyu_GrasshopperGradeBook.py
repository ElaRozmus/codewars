# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 14:04:37 2023

@author: rozmu
"""

"""
Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

Numerical Score	Letter Grade
90 <= score <= 100	'A'
80 <= score < 90	'B'
70 <= score < 80	'C'
60 <= score < 70	'D'
0 <= score < 60	'F'
Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.
"""

from statistics import mean
 
def get_grade(number1, number2, number3):
    number_list = (number1, number2, number3)
    number = mean(number_list)
    
    if 90 <= number <= 100:
        return "A"
    elif 80 <= number < 90:
        return "B"
    elif 70 <= number < 80:
        return "C"
    elif 60 <= number < 70:
        return "D"
    elif 0 <= number < 60:
        return "F"

# %%
from statistics import mean 

def get_grade(number1, number2, number3):
    number_list = (number1, number2, number3)
    number = mean(number_list)
    
    if number >= 90: return "A"
    if number >= 80: return "B"
    if number >= 70: return "C"    
    if number >= 60: return "D"
    else:
        return "F"
    
print(get_grade(3,588,66))
    