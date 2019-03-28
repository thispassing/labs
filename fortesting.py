#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice = 0
    bob = 0
    score = [alice,bob]
    for x,y in zip(a,b):
        if x > y:
            alice += 1
        elif y > x:
            bob += 1
        else:
            continue
    print(alice,bob)

compareTriplets((5,6,7), (3,6,10))