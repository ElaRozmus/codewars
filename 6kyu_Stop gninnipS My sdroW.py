# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 15:27:36 2023

@author: rozmu
"""


def spin_words(sentence):
    noChange = []
    for word in sentence.split():
        if len(word) >= 5:
            noChange.append(word[::-1])
        else:
            noChange.append(word)
    return " ".join(noChange) 
        










