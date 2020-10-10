# coding: utf-8

import sys
import collections

N, L = map(int, sys.stdin.readline().split())
numList = collections.deque(map(int, sys.stdin.readline().split()))
val = collections.deque([numList.popleft()])
i = 1
iList = collections.deque([i])


def check(left):
    global border, iList, val
    if left:
        if iList[0] < border:
            val.popleft()
            iList.popleft()
            return True
        else:
            return False
    else:
        if iList[len(iList) - 1] < border:
            val.pop()
            iList.pop()
            return True
        else:
            return False


def add(left, addVal, addI):
    if left:
        val.appendleft(addVal)
        iList.appendleft(addI)

    else:
        val.append(addVal)
        iList.append(addI)


sys.stdout.write(str(val[0])+' ')
while numList:
    i += 1
    border = i+1-L
    new = numList.popleft()

    head = val[0] - new
    if head > 0:
        check(True)
        add(True,new,i)

    elif head == 0:
        iList[0] = i

    else:
        tail = val[len(val) - 1] - new
        if tail < 0:
            check(False)
            add(False,new,i)

        elif tail == 0:
            iList[len(iList)-1] = i

        else:

            if head * -1 > tail:
                Rotate = True
                right = True
            elif head * -1 < tail:
                Rotate = True
                right = False
            else:
                mi = int(len(val)/2)
                if val[mi] < new:
                    Rotate = True
                    right = True
                elif val[mi] > new:
                    Rotate = True
                    right = False
                else:
                    iList[mi] = i
                    Rotate = False

            if Rotate:
                c = 0
                if right:
                    while val[len(val)-1] > new:
                        if not check(False):
                            val.rotate(1)
                            iList.rotate(1)
                            c += 1

                    if val[len(val)-1] < new:
                        check(False)
                        add(False,new,i)

                    else:
                        iList[len(iList)-1] = i

                else:
                    while val[0] < new:
                        if not check(True):
                            val.rotate(-1)
                            iList.rotate(-1)
                            c -= 1

                    if val[0] > new:
                        check(True)
                        add(True,new,i)

                    else:
                        iList[0] = i
                val.rotate(-1 * c)
                iList.rotate(-1 * c)

    while check(True):
        pass

    sys.stdout.write(str(val[0])+' ')