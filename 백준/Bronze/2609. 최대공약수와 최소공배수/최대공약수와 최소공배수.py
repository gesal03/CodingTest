import sys
import math
input = sys.stdin.readline

a, b = input().split()
a=int(a)
b=int(b)

if a > b:
    big = a
    small = b
else:
    big = b
    small = a

while(True):
    if big == 0:
        break
    elif (big - small) < 0:
        tmp = big
        big = small
        small = tmp
    else:
        big -= small


max = b * (a / small)
print(small)
print(int(max))