# coding: utf-8
# stack
# [입력]
# N : 탑의 수
# a b c d : 탑의 높이
# [출력]
# 자신을 기준으로 왼쪽의 탑 중 키번호가 자기 바로 앞인 탑

import sys
import collections

N = int(sys.stdin.readline())
Height = collections.deque(map(int, sys.stdin.readline().split()))
result = collections.deque([0])
stack = collections.deque([1])
stack.appendleft(Height.popleft())

i = 1
while Height:
    # 스택의 top과 비교하여 작으면 스택에 push
    if not stack or stack[0] > Height[0]:
        p = Height.popleft()
        i += 1
        if stack:
            result.append(stack[1])
        else:
            result.append(0)
        stack.appendleft(i) # 탑 번호 push
        stack.appendleft(p) # 탑 높이 push
    else:
        stack.popleft()
        stack.popleft()

sys.stdout.write(' '.join(map(str, result)) + '\n')