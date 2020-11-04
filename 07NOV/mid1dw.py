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

def minimumBribes(q):
    distance = 0
    temp = []
    count = 0
    result = 0
    for i in q:
        #check distance if the element is in place
        if(i != q.index(i)+1):
            distance = abs((i)-(q.index(i)+1))
            if(distance >2):
                print('Too chaotic')
                return
        count+=1
    print(result)
    
        
            


#return3
test1 = [2,5,1,3,4]
#return too chaotic
print(minimumBribes(test1))
test2 = [1,2,3,5,4]
print(minimumBribes(test2))
test3 = [2,1,5,3,4]
print(minimumBribes(test3))
test4 = [1,2,5,3,4,7,8,6]
print(minimumBribes(test4))
test5 = [5,1,2,3,7,8,6,4]
print(minimumBribes(test5))


            