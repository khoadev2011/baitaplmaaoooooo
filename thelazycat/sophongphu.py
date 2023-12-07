import math
def fact(val):
    f = []
    for x in range(1, val):
        if val % x == 0:
            f.append(x)
    return f

l = int(input())
r = int(input())

count = 0
for x in range(l, r + 1):
    count += 1 if sum(fact(x)) > x else 0
print(count)