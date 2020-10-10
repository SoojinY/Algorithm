import sys, collections

N, L = map(int, sys.stdin.readline().split())
numList = collections.deque(map(int, sys.stdin.readline().split()))
val = collections.deque()

for i in range(N):
    new = numList.popleft()
    while val and new < val[-1][1]:
        val.pop()
    while val and val[0][0] < i - L + 1:
        val.popleft()
    val.append((i, new))
    sys.stdout.write(str(val[0][1]) + ' ')