
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
    check = -63
    result = 0
    for a in range(4):
         for i in range(4):
            sumarr = sum(arr[a][i:i+3])+arr[a+1][i+1]+sum(arr[a+2][i:i+3])
            if check < sumarr:
                check = sumarr
    return(check)
