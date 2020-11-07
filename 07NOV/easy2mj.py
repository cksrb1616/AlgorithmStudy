#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    for i in range(d):
        a.append(a[i])
    return a[d:]
