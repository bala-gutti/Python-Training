#!/usr/bin/python

import sys

n = 10
data = []
for i in range(n):
    a=len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes: {1:4d}',{a},b)
    data.append(n)

