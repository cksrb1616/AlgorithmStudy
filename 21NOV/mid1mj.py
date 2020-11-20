#!/bin/python3

import math
import os
import random
import re
import sys


##반정도는 타임 아웃 한 문제는 틀림처리

# Complete the countTriplets function below.
def countTriplets(arr, r):
    nlist = sorted(arr)
    nlist2 = sorted(list(set(arr)))
    count = []
    result = 0
    for i in range(len(nlist)):
        count.append(nlist.count(nlist[i]))
    for i in range(len(nlist2)):
        if nlist2[i]*r in nlist2 and nlist2[i]*r*r in nlist2:
            result += 1
            if count[nlist.index(nlist2[i])] != 1:
                result += (count[nlist.index(nlist2[i])]-1)
            if nlist[i]*r in nlist:
                if count[nlist.index(nlist2[i]*r)] != 1:
                    result += (count[nlist.index(nlist2[i]*r)]-1)
                else:
                    pass
            if nlist[i]*r*r in nlist:
                if count[nlist.index(nlist2[i]*r*r)] != 1:
                    result += (count[nlist.index(nlist2[i]*r*r)]-1)
                else:
                    pass
    return(result)
