import sys
import collections

parenthesis = collections.deque()
T = int(sys.stdin.readline())

for i in range(T):
    string = sys.stdin.readline()
    underflow = 0
    for j in range(len(string)-1):
        back = string[j]
        if back == '(':
            parenthesis.append(back)
        elif back == ')':
            if parenthesis:
                parenthesis.pop()
            else:
                underflow = 1
                break
    if underflow:
        out = 'NO'
    elif parenthesis:
        out = 'NO'
    else:
        out = 'YES'
    sys.stdout.write(out+'\n')
    parenthesis.clear()
