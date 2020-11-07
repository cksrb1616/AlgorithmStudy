#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    arrpos = [*enumerate(arr)]
    arrpos.sort(key = lambda it : it[1])
    vis = {k : False for k in range(n)}
    ans = 0
    
    for i in range(n):
        if vis[i] or arrpos[i][0] == i:
            print('continue'+str(i))
            continue
        cycle_size = 0
        j = i
         
        while not vis[j]:
            vis[j] = True
            j = arrpos[j][0]
            cycle_size += 1

        if cycle_size > 0:
            ans += (cycle_size - 1)
    return ans
