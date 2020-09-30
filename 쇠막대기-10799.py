import sys
import collections

command = sys.stdin.readline().strip('\n')
rod = collections.deque()
total = 0

for i in range(len(command)):
    if command[i] == '(':
        rod.append(1)
    else:
        if command[i-1] == '(':
            rod.pop()
            for j in range(len(rod)):
                rod[j] += 1
        else:
            total += rod.pop()

sys.stdout.write(str(total))