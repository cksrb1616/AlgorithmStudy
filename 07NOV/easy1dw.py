#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    #    rowPointer = len(arr)
    # colPointer = len(arr[0]) 
    rowPointer = 0
    colPointer = 0
    while rowPointer == len(arr)-2:
        sum = arr[rowPointer][colPointer]+arr[rowPointer+1][colPointer]+arr[rowPointer+2][colPointer]
        +arr[rowPointer+1][colPointer+1]+arr[rowPointer+2][colPointer]+arr[rowPointer+2][colPointer+1]+arr[rowPointer+2][colPointer+2]
        if colPointer == 4:
            colPointer=0
            rowPointer+=1
        return sum


    

    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
