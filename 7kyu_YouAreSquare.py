# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 13:03:23 2023

@author: rozmu
"""

import math

def is_square(n):
    if n >= 0:
        print(str(math.sqrt(n)))
        print(str(math.sqrt(n))[-2::])
    if n >= 0 and str(math.sqrt(n))[-2::] == ".0":
        return True
    else:
        return False