import sys, collections

N = int(sys.stdin.readline())
A = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
test = collections.deque(map(int, sys.stdin.readline().split()))


while test:
    t = test.popleft()
    sys.stdout.write('1\n' if t in A else '0\n')
