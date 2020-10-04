# coding: utf-8

import sys
import collections

testcase = int(sys.stdin.readline())

for i in range(testcase):
    docNum, where = map(int, sys.stdin.readline().split())
    docs = collections.deque(map(int, sys.stdin.readline().split()))
    bound = docs[where]
    size = len(docs)
    cnt = 0

    while 1:
        if docs[0] < max(docs):
            docs.rotate(-1)
        else:
            cnt += 1
            if where == 0:
                break
            docs.popleft()

        where -= 1
        if where < 0:
            where = len(docs)-1

    sys.stdout.write(str(cnt)+'\n')


