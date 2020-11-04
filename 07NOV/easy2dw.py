#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    temp = a[0:d]
    del a[0:d]
    a.extend(temp)
    return a

    