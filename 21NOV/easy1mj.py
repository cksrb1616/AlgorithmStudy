#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    try:
        for i in note:
            magazine.remove(i)
            ##### magazine.remove(i for i in note) 는 왜 안 되지?##
            ##### 한 문제 타임 아웃
    except:
        print("No")
    else:
        print("Yes")
