import csv
import itertools
import random
import math
import mpm
import time
from itertools import permutations


## Print out the current findings
def info(n, r, p):
    print(f"Hash space {n}, Sample space {r}, probabiliy of collision {p}")

## Calculate the probability of a has collision using the birthday formula
def calcp(n, r):
    fac_n = decimal math.factorial(n)
    fac_r = math.factorial(r)
    fac_nr = math.factorial(n-r)
    p = fac_n / (fac_nr*fac_r)
    info(n,r,p)

## MD5
calcp(pow(2,128),10000000)
