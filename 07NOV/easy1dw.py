#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    check = -63
    rowPointer = 0
    colPointer = 0
    while (rowPointer < 4):
        result = arr[rowPointer][colPointer]+arr[rowPointer][colPointer+1]+arr[rowPointer][colPointer+2]+arr[rowPointer+1][colPointer+1]+arr[rowPointer+2][colPointer]+arr[rowPointer+2][colPointer+1]+arr[rowPointer+2][colPointer+2]
        if (result > check):
            check = result
        colPointer+=1
        if (colPointer == 4):
            colPointer=0
            rowPointer += 1
    return check



