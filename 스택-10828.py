import sys
from collections import deque

opNum = int(sys.stdin.readline())
stack = deque()

for i in range(opNum):
    op = sys.stdin.readline().split()
    if op[0] == 'push':
        stack.append(int(op[1]))
    else:
        if op[0] == 'pop':
            if stack:
                out = str(stack.pop())
            else:
                out = '-1'
        elif op[0] == 'size':
            out = str(len(stack))
        elif op[0] == 'top':
            if stack:
                out = str(stack.pop())
                stack.append(int(out))
            else:
                out = '-1'
        else:
            if stack:
                out = '0'
            else:
                out = '1'

        out += '\n'
        sys.stdout.write(out)
