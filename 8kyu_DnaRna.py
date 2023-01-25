# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 13:41:16 2023

@author: rozmu
"""
# "GCAT"  =>  "GCAU"



def dna_to_rna(dna):
    
    if "T" in dna:
        return dna.replace("T", "U")
    else:
        return dna
print(dna_to_rna("GCA"))
# %%
def dna_to_rna(dna):
    return (dna.replace("T", "U") if "T" in dna else dna)
    
    
 
print(dna_to_rna("GCAT"))
# %%
def DNAtoRNA(dna):
    return dna.replace('T', 'U')

print(DNAtoRNA("GCA"))