# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 13:03:59 2023

@author: rozmu
"""

def get_middle(string):
     if len(string) % 2 == 0:
        x =  string[(len(string) -1)// 2], string[(len(string))// 2]
        return "".join(x)
        
     elif len(string) % 2 == 1:
        x = string[(len(string))// 2]
        return "".join(x)