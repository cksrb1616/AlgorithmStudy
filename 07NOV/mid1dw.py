#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.



#check if the elemebt is in place.
#if it is not
#   - check distance>2 -> too chaotic
#   - check distance<=2
#   - check how far?
#   - how to prevent duplication
#       - [2,1,5,3,4]

#%%


def checkChaotic(q): 
    distance = 0
    result = True
    for i in q:
        distance = (i)-(q.index(i)+1)
        if(distance>2) : 
            print("Too chaotic")
            return False
            
    return result
def minimumBribes(q):
    count = 0
    result = 0
    if(checkChaotic(q)):
        for i in range(len(q)-1,-1,-1):
            for j in range(max(0, q[i] - 2),i):
                if q[j] > q[i]:
                    result+=1
        print(result)





            
test1 = [1,2,5,3,7,8,6,4]

print("This is test 1 :",minimumBribes(test1))
print("This is test 1 array :",test1)
# test2 = [5,1,2,3,7,8,6,4]
# print("This is test 2 :",minimumBribes(test2))
# print("This is test 2 array :",test2)
# test3 = [2,5,1,3,4]
# print("This is test 3 :",minimumBribes(test3))




# %%
