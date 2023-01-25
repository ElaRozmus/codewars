# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 13:07:11 2023

@author: rozmu
"""

def what_century(year):
    centuryend = 1 + (int(year) - 1)// 100
    centuryEnds = str(centuryend)
    if 4 <= centuryend <= 20:
        return f'{centuryEnds}th'
        
    elif centuryend > 20:    
            
        if centuryEnds.endswith("1"):
            return f'{centuryEnds}st'
        elif centuryEnds.endswith("2"):
            return f'{centuryEnds}nd'
        elif centuryEnds.endswith("3"):
            return f'{centuryEnds}rd'
        elif centuryEnds.endswith("4") or centuryEnds.endswith("5") or centuryEnds.endswith("6") or centuryEnds.endswith("7") or centuryEnds.endswith("8") or  centuryEnds.endswith("9") or centuryEnds.endswith("0") :
            return f'{centuryEnds}th'