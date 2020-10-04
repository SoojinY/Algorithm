# coding: utf-8

from sys import stdin, stdout
import collections

command = collections.deque(stdin.readline().strip())
rounds = 0
squares = 0
stack = collections.deque()
underflow = False


# 닫는 괄호 처리 하는 함수
def close(bracket, i):
    global stack, command, rounds, squares

    # 변수 설정
    if bracket == 'square':
        if squares < 0:
            return
        openBracket = '['
        val = 3
    else:
        if rounds < 0:
            return
        openBracket = '('
        val = 2

    # 처리
    # 단일 괄호 경우
    if command[i - 1] == openBracket:
        stack.pop()
        stack.append(val)
    # 확장 괄호 경우
    else:
        add = 0
        while 1:
            temp = stack.pop()
            if type(temp) is int:
                add += temp
            else:
                stack.append(add * val)
                break


for i in range(len(command)):
    c = command[i]
    if c == '(':
        rounds += 1
        stack.append(c)
    elif c == ')':
        rounds -= 1
        close('round', i)

    elif c == '[':
        squares += 1
        stack.append(c)

    else:  # c == ']'
        squares -= 1
        close('square', i)

    if squares < 0 or rounds < 0:
        underflow = True
        break


if underflow or rounds+squares > 0:
    out = 0
else:
    out = sum(stack)

stdout.write(str(out))

