import math
import os
import random
import re
import sys
from datetime import datetime

def time_delta(t1, t2):
    fmt = "%a %d %b %Y %H:%M:%S %z"
    time1 = datetime.strptime(t1, fmt)
    time2 = datetime.strptime(t2, fmt)

    diff = abs(int((time1 - time2).total_seconds()))
    return str(diff)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input().rstrip()

        t2 = input().rstrip()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
