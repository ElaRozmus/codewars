# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 12:56:41 2023

@author: rozmu
"""
# first method
def get_count(sentence):
    vowel = ["a", "e", "i", "o", "u"]
    new_list = []
    result = [new_list.append(letter) for letter in sentence if letter in vowel]
    return(len(new_list))

