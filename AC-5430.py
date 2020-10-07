# coding: utf-8
# input:    testcase 수 T
#           함수 p
#           배열 크기 n
#           배열 ([a,b,c] 형태)
# output:   함수 수행 결과

from sys import stdout, stdin
import collections


def preprocessArray(a):
    a = a[1:len(a) - 1]
    pre = collections.deque(a.split(','))
    return pre


T = int(stdin.readline())
for i in range(T):
    p = collections.deque(stdin.readline().strip())
    n = int(stdin.readline())
    array = preprocessArray(stdin.readline().strip())
    Error = False
    Reverse = False

    while p and not Error:
        c = p.popleft()

        if c == 'R':
            Reverse = not Reverse
        else:
            n -= 1
            if n < 0:
                Error = True
            elif Reverse:
                array.pop()
            else:
                array.popleft()
    if Error:
        out = 'error'
    elif array:
        if Reverse:
            array.reverse()
        out = '[' + ','.join(array) + ']'
    else:
        out = '[]'
    stdout.write(out + '\n')

