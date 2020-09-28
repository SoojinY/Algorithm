import sys
from collections import deque

edit = deque(sys.stdin.readline())  # given string as deque
edit.pop()
window = len(edit)


def left():
    global window
    if window > 0:
        edit.rotate(1)
        window -= 1


def right():
    global window
    if window < len(edit):
        edit.rotate(-1)
        window += 1


def delete():
    global window
    if window > 0:
        edit.pop()
        window -= 1


def push(c):
    global window
    edit.append(c)
    window += 1


opNum = int(sys.stdin.readline())  # number of operation

for i in range(opNum):
    op = sys.stdin.readline()  # operation and push character
    if op[0] == 'L':
        left()
    elif op[0] == 'D':
        right()
    elif op[0] == 'B':
        delete()
    elif op[0] == 'P':
        push(op[2])
    else:
        sys.stdout.write("! Wrong Operation !")

while window < len(edit):
    right()

while edit:
    sys.stdout.write(edit.popleft())
