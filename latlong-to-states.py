from __future__ import print_function  # PY2 or PY3
import os, sys
from collections import defaultdict

A = defaultdict(dict)

def Decimalize(s):
    x = float(s)
    x, sign = abs(int(x)), (-1 if int(x)<0 else 1)
    seconds = x % 100
    minutes = int(x / 100) % 100
    degrees = int(x / 10000)
    return sign * (degrees + minutes/60.0 + seconds/3600.0)

def Process(line):
    parts = line.split(';')
    if len(parts) != 4: return
    state, city, lat, lon = parts
    state = state.upper()
    city = city.upper()
    A[state][city] = Decimalize(lat), Decimalize(lon)

for line in sys.stdin:
    Process(line.strip())

for s, d in sorted(A.items()):
    sumlat, sumlon, n = 0.0, 0.0, 0
    for c, (lat, lon) in sorted(d.items()):
        # print ((s, c, lat, lon))
        sumlat += lat
        sumlon += lon
        n += 1
    print (str((s[0], s, sumlat/n, sumlon/n)).replace('(', '[').replace(')', ']') + ',')
