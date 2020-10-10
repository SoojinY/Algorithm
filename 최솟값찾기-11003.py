# coding: utf-8

import sys
import collections

N, L = map(int, sys.stdin.readline().split())
numList = collections.deque(map(int, sys.stdin.readline().split()))
d = dict()
Min = numList.popleft()
i = 1
d[Min] = i

sys.stdout.write(str(Min)+' ')
while numList:
    i += 1

    new = numList.popleft()
    d[new] = i
    if new < Min:
        Min = new

    if d.get(Min) < i-L+1:
        del d[Min]
        dsort = sorted(d)
        Min = dsort[0]

    sys.stdout.write(str(Min)+' ')