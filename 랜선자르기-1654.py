import sys, collections

K, N = map(int, sys.stdin.readline().split())
lines = collections.deque()
for _ in range(K):
    lines.append(int(sys.stdin.readline()))

L = 1
R = max(lines)

while L <= R:
    x = (L+R)//2
    total = 0
    for l in lines:
        total += l//x
    if total < N:
        R = x - 1
    else:
        L = x + 1


sys.stdout.write(str(R))
