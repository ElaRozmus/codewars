# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 13:05:15 2023

@author: rozmu
"""

def disemvowel(string):
    vowel_list = ["a", "e", "i", "o", "u", 'A', 'E', 'I', 'O', 'U']
    result = ""
    for i in range(len(string)):
        if string[i] not in vowel_list:
            result = result + string[i]
    return result