def d(n):
    num = n
    self = 0
    while num > 0:
        self += num % 10
        num = int(num / 10)
    self += n

    return self


self_num = dict()

for i in range(1, 10000):
    n = d(i)
    while 10000 > n > 0:
        if str(n) not in self_num:
            self_num[str(n)] = n
        n = d(n)

for i in range(1, 10000):
    if str(i) not in self_num:
        print(i)
