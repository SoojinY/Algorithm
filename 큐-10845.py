import sys
from collections import deque


que = deque()
opNum = int(sys.stdin.readline())
for i in range(opNum):
    op = sys.stdin.readline().split()
    print(op)
    if op[0] == 'push':
        que.append(int(op[1]))
    else:
        if op[0] == 'pop':
            if que:
                out = -1
            else:
                out = que.popleft()
        elif op[0] == 'size':
            out = len(que)
        elif op[0] == 'empty':
            if que:
                out = 0
            else:
                out = 1
        elif op[0] == 'front':
            if que:
                out = que.popleft()
                que.appendleft(out)
            else:
                out = -1
        else:
            if que:
                out = que.pop()
                que.append(out)
            else:
                out = -1
        sys.stdout.write(str(out)+'\n')
    print(que)