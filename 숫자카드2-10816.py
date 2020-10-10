import collections
import sys

N = int(sys.stdin.readline())
Nlist = collections.Counter(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
Mlist = collections.deque(map(int,sys.stdin.readline().split()))

while Mlist:
    sys.stdout.write(str(Nlist[Mlist.popleft()])+' ')