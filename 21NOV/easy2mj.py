#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    if set(s1)&set(s2) != set():
        return "YES"
    else:
        return "NO"
