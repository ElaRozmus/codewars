# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 13:01:56 2023

@author: rozmu
"""

def friend(x):
    return list(filter(lambda name: len(name) == 4, x))

# %%

def friend(x):
    return [ name for name in x if len(name) == 4]

# %%

def friend(x):
    new_list = []
    for name in x:
        if len(name) == 4:
            new_list.append(name)
    return new_list