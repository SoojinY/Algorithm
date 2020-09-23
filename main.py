import sys
command = sys.stdin.readline().split(" ")

N = int(command[0])
K = int(command[1])

josephus = []
for i in range(N):
    josephus.append(0)

index = 1
count = 0
order = []

while 0 in josephus:
    if josephus[index-1] < 1:
        if count < K-1:
            count += 1
        else:
            josephus[index-1] = 1
            count = 0
            order.append(index)
    index += 1
    index %= N
    if index < 1:
        index += N

print(order)