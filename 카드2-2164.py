import sys
import collections

n = int(sys.stdin.readline())
card = collections.deque(i for i in range(n))
while card:
    last = card.popleft()
    card.rotate(-1)

sys.stdout.write(str(last+1))