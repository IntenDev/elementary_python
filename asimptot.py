import math

n = int(input())

tmp = 1
for i in range(2, n+1):
    tmp += 1 / i
tmp = tmp - math.log(n)

print(tmp)
