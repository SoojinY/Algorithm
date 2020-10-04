import sys

command = sys.stdin.readline().strip('\n')
rod = 0
total = 0

for i in range(len(command)):
    if command[i] == '(':
        rod += 1
    else:
        rod -= 1
        if command[i-1] == '(':
            total += rod
        else:
            total += 1

sys.stdout.write(str(total))
