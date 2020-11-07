  
#!/bin/python3

import math
import os
import random
import re
import sys

import Numpy as np
# Complete the hourglassSum function below.
def hourglassSum(arr):
    sumarr = np.arange(16).reshape(4,4)
    for a in range(4):
         for i in range(4):
            sumarr[a][i] = sum(arr[a][i:i+3])+arr[a+1][i+1]+sum(arr[a+2][i:i+3])
    max_value = np.max(sumarr)
    return max_value
